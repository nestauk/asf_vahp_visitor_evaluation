# %% [markdown]
# ## VAHP Visitor Evaluation survey
#
# notebook to analyse responses to the 'Your experience visiting a heat pump' survey

# %%
import pandas as pd

# %%
filepath = "20260302_vahp_eval_surveys.csv"

df = pd.read_csv(filepath)

# Pivoting creates an interesting multi-index column structure.
df_wide = df.loc[
    lambda df: df["survey_title"] == "Your experience visiting a heat pump"
].pivot(index="id", columns=["title", "option"], values="selected")

# %%
# here I'm just printing the questions asked so I can get the exact wording for use later

df_survey = df.loc[
    lambda df: df["survey_title"] == "Your experience visiting a heat pump"
]
for i, line in enumerate(df_survey["title"].unique()):
    print(line)

# %% [markdown]
# ## Looking at the question responses

# %%
# why are these all false ?????

df_wide[
    "Please confirm that you have visited a heat pump in person, at the property of a host, as part of the 'Visit a Heat Pump' service."
]

# %%
df_wide["Which of the following most applies to you since you visited a heat pump?"]

# %%
df_wide[
    "How likely is it that you will install an air-source heat pump when when you next need to change your heating system or boiler?"
]

# %%
df_wide[
    "Did visiting a heat pump, talking to a host, or any other use of Visit a Heat Pump help you when taking steps to install a heat pump in your home?"
]

# %%
df_wide[
    "Did visiting a heat pump, talking to a host, or any other use of Visit a Heat Pump help you when installing your heat pump in your home?"
]

# %%
df_wide[
    "Would you have installed a heat pump anyway, even if you had not used Visit a Heat Pump?"
]

# %%
# function to get counts/ proportions of the True responses to each question


def get_option_counts_and_proportions(question_title: str, mask=None):
    """
    Finds number and proportion of eligible respondents who answered True for each response

    Args:
        question_title (str): question you want to find the response to
        mask (optional, bool, default = None): mask to filter df to only eligible respondents
    """
    if mask is not None:
        question_of_interest = (
            df_wide.loc[mask]
            .loc[:, question_title]
            .stack()
            .dropna()
            .loc[lambda s: s]
            .reset_index()
            .drop(columns=0)
        )
    else:
        question_of_interest = (
            df_wide.loc[:, question_title]
            .stack()
            .dropna()
            .loc[lambda s: s]
            .reset_index()
            .drop(columns=0)
        )
    print(f"eligible respondents: {len(question_of_interest)}")
    return question_of_interest["option"].value_counts(), question_of_interest[
        "option"
    ].value_counts(normalize=True)


# %% [markdown]
# ## What have people done?

# %%
question_title = (
    "Which of the following most applies to you since you visited a heat pump?"
)
print(question_title)
get_option_counts_and_proportions(question_title)

# %% [markdown]
# ## Likelihood of installing an ASHP

# %%
question_title = "How likely is it that you will install an air-source heat pump when when you next need to change your heating system or boiler?"
mask = df_wide[
    "Which of the following most applies to you since you visited a heat pump?"
][
    "I have taken steps towards installing a heat pump and still intend to install a heat pump in my home"
]
print(question_title)
get_option_counts_and_proportions(question_title, mask)

# %% [markdown]
# ## Did VAHP help (taking steps)?

# %%
question_title = "Did visiting a heat pump, talking to a host, or any other use of Visit a Heat Pump help you when taking steps to install a heat pump in your home?"
mask = (
    df_wide[
        "Which of the following most applies to you since you visited a heat pump?"
    ][
        "I have taken steps towards installing a heat pump and still intend to install a heat pump in my home"
    ]
    | df_wide[
        "Which of the following most applies to you since you visited a heat pump?"
    ][
        "I have taken steps towards installing a heat pump but no longer wish to install a heat pump in my home"
    ]
)
print(question_title)
get_option_counts_and_proportions(question_title, mask)

# %% [markdown]
# ## Did VAHP help (installing)?

# %%
question_title = "Did visiting a heat pump, talking to a host, or any other use of Visit a Heat Pump help you when installing your heat pump in your home?"
mask = (
    df_wide[
        "Which of the following most applies to you since you visited a heat pump?"
    ][
        "I have taken steps towards installing a heat pump and still intend to install a heat pump in my home"
    ]
    | df_wide[
        "Which of the following most applies to you since you visited a heat pump?"
    ]["I have installed a heat pump in my home since visiting a heat pump"]
)
print(question_title)
get_option_counts_and_proportions(question_title, mask)

# %% [markdown]
# ## Heat pump installation intention

# %%
question_title = "Would you have installed a heat pump anyway, even if you had not used Visit a Heat Pump?"
mask = df_wide[
    "Which of the following most applies to you since you visited a heat pump?"
]["I have installed a heat pump in my home since visiting a heat pump"]
print(question_title)
get_option_counts_and_proportions(question_title, mask)

# %%
