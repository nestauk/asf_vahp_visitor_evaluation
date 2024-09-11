# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     comment_magics: true
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import datetime

from asf_vahp_visitor_evaluation.pipeline.load_data import (
    create_anonymous_id,
    make_pre_visit_analysis_ready,
    make_post_visit_analysis_ready,
    # make_follow_up_visit_analysis_ready,
    make_linked_data,
)

from asf_vahp_visitor_evaluation.config import config


# %% [markdown]
# ## Visit a Heat Pump Visitor Evaluation
# ### Create Anonymised Analysis Ready Data
#
# **Step 1**
# Download latest pre- post- and follow-up surveys (as applicable) to secure drive.
#
# **Step 2**
# Update `asf_vahp_visitor_evaluation.config.config.py` with filepaths for latest surveys.
#
# **Step 3**
# Run `create_anonymous_id()` function to update main visitor id lookup.
#
# This creates a link between identifiable visitor email addresses and an anonymous random id that we can use for linkage across surveys.
#
# **Step 4**
# Run relevant `make_` functions.
#
# **Step 5**
# Save out anonymised analysis ready data.

# %%
# Run this to create and update main visitor linkage table.
create_anonymous_id(exclude_from_linkage=True)

# %%
# Analysis ready pre-visit data
pre = make_pre_visit_analysis_ready()

# %%
# Analysis ready post-visit data
post = make_post_visit_analysis_ready()

# %%
# Analysis ready pre- and post- linked data
linked = make_linked_data([pre, post])

# %%
# Save out datasets
anonymous_data_root = config.ANONYMISED_DATA_ROOT

date = datetime.datetime.now().strftime("%Y%m%d")

# %%
# Pre visit
pre.to_parquet(f"{anonymous_data_root}{date}_pre_visit_survey.parquet")

# %%
# Post visit
post.to_parquet(f"{anonymous_data_root}{date}_post_visit_survey.parquet")

# %%
# linked
linked.to_parquet(f"{anonymous_data_root}{date}_linked_pre_post_visit_survey.parquet")
