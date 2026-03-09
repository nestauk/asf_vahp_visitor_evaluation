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
# ## Make dataframes for each question with applicable respondents

# %%
df_wide[
    "Please confirm that you have visited a heat pump in person, at the property of a host, as part of the 'Visit a Heat Pump' service."
]

# %%
df_what_people_done = df_wide[
    "Which of the following most applies to you since you visited a heat pump?"
]

# %%
mask = df_wide[
    "Which of the following most applies to you since you visited a heat pump?"
][
    "I have taken steps towards installing a heat pump and still intend to install a heat pump in my home"
]
df_how_likely = df_wide[
    "How likely is it that you will install an air-source heat pump when when you next need to change your heating system or boiler?"
][mask]

# %%
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

df_help_steps = df_wide[
    "Did visiting a heat pump, talking to a host, or any other use of Visit a Heat Pump help you when taking steps to install a heat pump in your home?"
][mask]

# %%
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

df_help_install = df_wide[
    "Did visiting a heat pump, talking to a host, or any other use of Visit a Heat Pump help you when installing your heat pump in your home?"
][mask]

# %%
mask = df_wide[
    "Which of the following most applies to you since you visited a heat pump?"
]["I have installed a heat pump in my home since visiting a heat pump"]

df_install_anyway = df_wide[
    "Would you have installed a heat pump anyway, even if you had not used Visit a Heat Pump?"
]

# %% [markdown]
# ## Build dataframe with proportions / counts of each response

# %%
def get_question_summary(question_name, df):
    data = df.dropna()

    # Calculate Counts (Sum of True) and Percentages (Mean of True)
    counts = data.sum()
    percentages = data.mean()

    summary_df = pd.DataFrame({"Count": counts, "Percentage": percentages})

    # Add a column with question name
    summary_df["Question"] = question_name

    return summary_df


# %%
survey_questions = {
    "Which of the following most applies to you since you visited a heat pump?": df_what_people_done,
    "How likely is it that you will install an air-source heat pump when when you next need to change your heating system or boiler?": df_how_likely,
    "Did visiting a heat pump, talking to a host, or any other use of Visit a Heat Pump help you when taking steps to install a heat pump in your home?": df_help_steps,
    "Did visiting a heat pump, talking to a host, or any other use of Visit a Heat Pump help you when installing your heat pump in your home?": df_help_install,
    "Would you have installed a heat pump anyway, even if you had not used Visit a Heat Pump?": df_install_anyway,
}

# Process all dataframes and stack them together
all_results = []
for name, df in survey_questions.items():
    all_results.append(get_question_summary(name, df))

response_df = pd.concat(all_results)

response_df

# %%
# Save to CSV
# response_df.to_csv('vahp_eval_survey_analysis.csv', index_label='option')
