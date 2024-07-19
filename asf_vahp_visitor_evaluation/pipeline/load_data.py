import numpy
import pandas
import random
import unicodedata
import unidecode

from collections import Counter
from collections.abc import Iterable
from typing import Union

from asf_vahp_visitor_evaluation.config import config

from asf_vahp_visitor_evaluation.utils.lookups import (
    PreVisitQuestionNumbers as previsitq,
    PostVisitQuestionNumbers as postvisitq,
)


def create_anonymous_id(
    main_lookup: str = config.MAIN_LOOKUP,
    input_surveys: Iterable[str] = [
        config.PRE_VISIT_SURVEY,
        config.POST_VISIT_SURVEY,
        config.FOLLOW_UP_SURVEY,
    ],
) -> None:
    """Create anonymous IDs from emails for linkage."""
    # Get main file
    main = pandas.read_csv(main_lookup, dtype={"email": str, "visitor_id": int})
    # Get unique candidate emails from surveys
    # Must have agreed to participate.
    input_surveys = [survey for survey in input_surveys if survey != ""]
    candidate_emails = list(
        set(
            [
                email.lower().strip()
                for survey in input_surveys
                for email in pandas.read_csv(survey)
                .loc[lambda df: df[previsitq.q0e] == "Yes", "Your email address"]
                .to_list()
            ]
        )
    )
    # Remove previously seen emails
    keep_emails = numpy.isin(
        candidate_emails, main["email"], assume_unique=True, invert=True
    )
    # Filter candidates to just unseen emails
    candidate_emails = numpy.array(candidate_emails)[keep_emails]
    # Generate a random integer id
    new_ids = []
    while len(new_ids) < len(candidate_emails):
        candidate_id = random.randint(100_000_000, 999_999_999)
        if (candidate_id not in new_ids) and (candidate_id not in main["visitor_id"]):
            new_ids.append(candidate_id)
    # Append emails and ids to main list.
    new_lookup = pandas.DataFrame(
        data={"email": candidate_emails, "visitor_id": new_ids}
    )
    new_lookup.to_csv(main_lookup, mode="a", index=False, header=False)
    return None


def _fix_column_names(cols: list) -> list:
    """Replace unicode characters and trim whitespace from column names."""
    # Normalize
    cols = [unicodedata.normalize("NFC", col) for col in cols]
    # Now decode
    cols = [unidecode.unidecode(col) for col in cols]
    # Now strip
    cols = [col.strip() for col in cols]
    return cols


def _fix_cell(cell: Union[str, float]) -> str:
    """Replace unicode characters and trim whitespace from cell values."""
    if isinstance(cell, str):
        # Normalize
        cell = unicodedata.normalize("NFC", cell)
        # Now decode
        cell = unidecode.unidecode(cell)
        # Now strip
        cell = cell.strip()
    return cell


def _parse_dates(df: pandas.DataFrame, date_cols: list) -> pandas.DataFrame:
    """Convert date cols from strings to datetime objects."""
    for col in date_cols:
        df[col] = pandas.to_datetime(df[col])
    return df


def _parse_categories(df: pandas.DataFrame, category_vars: dict) -> pandas.DataFrame:
    """Convert category columns from string to categorical datatype."""
    for col, (categories, ordered) in category_vars.items():
        df[col] = pandas.Categorical(df[col], categories=categories, ordered=ordered)
    return df


def _parse_binaries(df: pandas.DataFrame, binary_cols: list) -> pandas.DataFrame:
    """Convert binary columns from strings to bools."""
    for col in binary_cols:
        value = col.split(":", maxsplit=1)[0]
        df[col] = df[col].map({value: True, numpy.nan: False}).astype("boolean")
    return df


def _anonymise_visitors(df: pandas.DataFrame, visitor_lookup: str) -> pandas.DataFrame:
    """Replace email identifier with anonymised id."""
    visitor_ids = pandas.read_csv(visitor_lookup)
    # clean emails
    df["Your email address"] = df["Your email address"].str.lower().str.strip()
    # Join ids
    df = df.merge(
        visitor_ids, how="left", left_on="Your email address", right_on="email"
    )
    # drop emails
    df = df.drop(columns=["Your email address", "email"])
    # Move visitor_id to front of dataframe
    col = df.pop("visitor_id")
    df.insert(3, col.name, col)
    return df


def _drop_duplicates(df: pandas.DataFrame) -> pandas.DataFrame:
    """Retain first complete response if available or first response otherwise."""
    # Get list of duplicates
    duplicate_ids = (
        df["visitor_id"].value_counts()[df["visitor_id"].value_counts().gt(1)].index
    )
    drop = []
    for duplicate_id in duplicate_ids:
        candidates = df.loc[
            df["visitor_id"] == duplicate_id, ["Date Submitted", "Status"]
        ]
        if len(candidates.loc[candidates["Status"] == "Complete", :]) > 1:
            # If multiple complete, use first by time submitted
            drop.extend(
                candidates.loc[candidates["Status"] == "Complete", ["Date Submitted"]]
                .sort_values("Date Submitted")
                .index[1:]
                .to_list()
            )
        elif len(candidates.loc[candidates["Status"] == "Complete", :]) == 1:
            # if only 1 complete, use that one
            drop.extend(
                candidates.loc[candidates["Status"] != "Complete", :].index.to_list()
            )
        else:
            # Otherwise use the earliest partial
            drop.extend(candidates["Date Submitted"].sort_values().index[1:].to_list())
    # Drop duplicate indices
    df = df.drop(index=drop).reset_index(drop=True)
    return df


def make_analysis_ready(
    source: str,
    usecols: Iterable,
    dtype: dict,
    date_cols: list,
    categories: dict,
    binaries: list,
    wave_id: str,
    visitor_lookup: str,
) -> pandas.DataFrame:
    """Generic function for loading VAHP survey data.

    Fixes issues with unicode characters and strips whitespace.
    Converts data to datetime, categorical and binary where relevant.
    Anonymises data for analysis by removing email identifier and adding
    numerical id for linkage. Removes non-consenting responses.

    Args:
        source: Filepath to survey data to be processed.
        usecols: Iterable of column names to load from source.
        dtype: Schema dictionary for columns at read.
        data_cols: List of columns to interpret as datetime objects.
        categories: Dictionary of categorical columns (keys) with a tuple
          of categories and order (e.g. {"col": (['cat1', 'cat2'], False),})
        binaries: List of columns to be convert to boolean.
        wave_id: String to indicate wave of data loaded.
        visitor_lookup: Filepath to lookup file.

    Returns:
        A pandas DataFrame that is the processed analysis-ready version
        of the input raw survey data.
    """
    # 1. Load raw data
    data = pandas.read_csv(
        source,
        usecols=usecols,
        dtype=dtype,
    )
    # 2. Fix column names
    data.columns = _fix_column_names(list(data.columns))
    # 3. Fix responses
    data.loc[:, data.dtypes == "object"] = data.loc[:, data.dtypes == "object"].map(
        _fix_cell
    )
    # 4. Convert dates
    data = _parse_dates(data, date_cols)
    # 5. Convert categories
    data = _parse_categories(data, categories)
    # 6. Convert binaries
    data = _parse_binaries(data, binaries)
    # 7. Add wave identifier at start of table
    col = pandas.Series(data=numpy.repeat(wave_id, repeats=len(data)), name="wave")
    data.insert(3, col.name, col)
    # 8. Remove non-consenting responses
    data = data.loc[
        data[data.columns[data.columns.str.startswith("I agree to participate")][0]]
        == "Yes",
        :,
    ]
    # 9. Remove any responses that are missing on email address
    data = data.loc[data["Your email address"].notnull(), :]
    # 10. Replace email with anonymous ID
    data = _anonymise_visitors(data, visitor_lookup)
    # 11. Drop duplicates
    data = _drop_duplicates(data)

    return data


def make_pre_visit_analysis_ready(
    source: str = config.PRE_VISIT_SURVEY,
    usecols: Iterable = config.PRE_VISIT_SCHEMA.keys(),
    dtype: dict = config.PRE_VISIT_SCHEMA,
    date_cols: list = config.PRE_VISIT_DATE_COLS,
    categories: dict = config.PRE_VISIT_CATEGORIES,
    binaries: list = config.PRE_VISIT_BINARIES,
    wave_id: str = "PRE",
    visitor_lookup: str = config.MAIN_LOOKUP,
) -> pandas.DataFrame:
    """Pre-filled function for pre-event visit a heat pump visitor surveys."""
    return make_analysis_ready(
        source, usecols, dtype, date_cols, categories, binaries, wave_id, visitor_lookup
    )


def make_post_visit_analysis_ready(
    source: str = config.POST_VISIT_SURVEY,
    usecols: Iterable = config.POST_VISIT_SCHEMA.keys(),
    dtype: dict = config.POST_VISIT_SCHEMA,
    date_cols: list = config.POST_VISIT_DATE_COLS,
    categories: dict = config.POST_VISIT_CATEGORIES,
    binaries: list = config.POST_VISIT_BINARIES,
    wave_id: str = "POST",
    visitor_lookup: str = config.MAIN_LOOKUP,
):
    """Pre-filled function for post-event visit a heat pump visitor surveys."""
    return make_analysis_ready(
        source, usecols, dtype, date_cols, categories, binaries, wave_id, visitor_lookup
    )


def make_follow_up_visit_analysis_ready(
    source: str = config.FOLLOW_UP_SURVEY,
    usecols: Iterable = config.FOLLOW_UP_SCHEMA.keys(),
    dtype: dict = config.FOLLOW_UP_SCHEMA,
    date_cols: list = config.FOLLOW_UP_DATE_COLS,
    categories: dict = config.FOLLOW_UP_CATEGORIES,
    wave_id: str = "FOLLOW_UP",
    visitor_lookup: str = config.MAIN_LOOKUP,
) -> pandas.DataFrame:
    """Pre-filled function for follow up visit a heat pump visitor surveys."""
    return make_analysis_ready(
        source, usecols, dtype, date_cols, categories, [], wave_id, visitor_lookup
    )


def _get_matching_ids(ids: list, required_matches: int = None) -> list:
    """Get matching ids from list of id Series."""
    # Number of matches required for inclusion
    if not required_matches:
        required_matches = len(ids)
    # Count instances of each ID
    matches = Counter()
    for wave_ids in ids:
        matches.update(wave_ids)
    # filter matches for those present in all waves
    matches = [key for key, value in matches.items() if value >= required_matches]
    return matches


def make_linked_data(
    datasets: list, columns: list = config.LINKED_COLUMNS, required_matches: int = None
) -> pandas.DataFrame:
    """Create linked data for analysis in long/tidy format.

    Args:
      datasets: list of participating datasets.
      columns: list of columns required in output linked dataset.
      required_matches: matches requires for linking (default: len(datasets))

    Returns:
      pandas DataFrame of matching data in long (tidy) format.
    """
    # Get matches for each dataset
    matching_ids = _get_matching_ids([dataset["visitor_id"] for dataset in datasets])
    matched_datasets = [
        dataset.loc[lambda df: df["visitor_id"].isin(matching_ids), :]
        for dataset in datasets
    ]

    # Create long (or 'tidy') data
    matched_columns = [col for dataset in matched_datasets for col in dataset.columns]
    columns = [col for col in config.LINKED_COLUMNS if col in matched_columns]
    linked_data = pandas.concat(matched_datasets, axis=0).loc[:, columns]
    return linked_data
