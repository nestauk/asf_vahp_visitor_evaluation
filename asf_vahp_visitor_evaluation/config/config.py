# Lookup for linkage
MAIN_LOOKUP = ""

# Lookups to exclude
EXCLUDE_FROM_LOOKUP = ""

# Pre-Visit Survey
PRE_VISIT_SURVEY = ""

# Post-visit survey
POST_VISIT_SURVEY = ""

# Follow-up survey
FOLLOW_UP_SURVEY = ""

# Anonymised data
ANONYMISED_DATA_ROOT = ""

PRE_VISIT_SCHEMA = {
    "Response ID": "int32",
    "Time Started": str,
    "Date Submitted": str,
    "Status": str,
    "Your email address": str,
    "I agree to participate in this survey for the 'visit a heat pump' service. In doing so, I acknowledge: \
- the purpose and nature of the study as described above; \
- that I understand I can withdraw at any time, without repercussions; \
- that Nesta will only use my data for research on the 'visit a heat pump' service; \
- My data will be confidential and held securely.": str,
    # Reasons for Visiting a Heat Pump
    "Why are you planning to visit a heat pump? (Select the most relevant option)": str,
    "Being more environmentally friendly:What motivates you to consider a heat pump for your home heating? (Select all that apply)": str,
    "Saving money on energy bills:What motivates you to consider a heat pump for your home heating? (Select all that apply)": str,
    "Taking advantage of a grant or subsidy (like the Boiler Upgrade Scheme):\
What motivates you to consider a heat pump for your home heating? (Select all that apply)": str,
    "Improving the quality of my heating system:What motivates you to consider a heat pump for your home heating? (Select all that apply)": str,
    "Improving the quality of my hot water:What motivates you to consider a heat pump for your home heating? (Select all that apply)": str,
    "My existing system is old and will require replacement soon:\
What motivates you to consider a heat pump for your home heating? (Select all that apply)": str,
    "Future proofing my home:What motivates you to consider a heat pump for your home heating? (Select all that apply)": str,
    "Removing the need for fuel storage (e.g. oil, lpg, wood, coal):\
What motivates you to consider a heat pump for your home heating? (Select all that apply)": str,
    "Other - Write In:What motivates you to consider a heat pump for your home heating? (Select all that apply)": str,
    "Other - Write In:What motivates you to consider a heat pump for your home heating? (Select all that apply).1": str,
    "How a heat pump works:What are you hoping to find out by visiting a heat pump? (Select all that apply)": str,
    "What a heat pump looks like:What are you hoping to find out by visiting a heat pump? (Select all that apply)": str,
    "How much a heat pump costs to install:What are you hoping to find out by visiting a heat pump? (Select all that apply)": str,
    "How much a heat pump costs to run:What are you hoping to find out by visiting a heat pump? (Select all that apply)": str,
    "How much noise a heat pump makes:What are you hoping to find out by visiting a heat pump? (Select all that apply)": str,
    "How much space a heat pump needs:What are you hoping to find out by visiting a heat pump? (Select all that apply)": str,
    "How easy a heat pump is to control:What are you hoping to find out by visiting a heat pump? (Select all that apply)": str,
    "About the installation process:What are you hoping to find out by visiting a heat pump? (Select all that apply)": str,
    "About changes that might be required to my home:What are you hoping to find out by visiting a heat pump? (Select all that apply)": str,
    "About the experience of living with a heat pump:What are you hoping to find out by visiting a heat pump? (Select all that apply)": str,
    "About decommissioning my current heating system:What are you hoping to find out by visiting a heat pump? (Select all that apply)": str,
    "Other - Write In:What are you hoping to find out by visiting a heat pump? (Select all that apply)": str,
    "Other - Write In:What are you hoping to find out by visiting a heat pump? (Select all that apply).1": str,
    "How did you find out about 'visit a heat pump'? (Select the most relevant option)": str,
    "Other - Write In:How did you find out about 'visit a heat pump'? (Select the most relevant option)": str,
    "Have you ever previously visited a property with a heat pump?": str,
    # Your Heat Pump Journey
    "I understand how a heat pump works.": str,
    "I can imagine what it would be like to have a heat pump in my home.\xa0\xa0": str,
    "I am confident that a heat pump would be an effective choice for my home.\xa0\xa0": str,
    "I have a clear understanding of the likely\xa0installation costs\xa0of a heat pump.\xa0\xa0": str,
    "I have a clear understanding of the likely\xa0running costs\xa0of a heat pump.\xa0\xa0": str,
    "My next heating system will use a heat pump as the main heat source.\xa0": str,
    "I know what steps I would need to take to install a heat pump in my own home.\xa0\xa0": str,
    "I have already taken steps to install a heat pump in my home": str,
    # Your Current Heating System
    "What type of central heating does your home have?  Central heating is a system that generates heat for multiple rooms.  \
If you have multiple systems, choose the one that provides your main source of space heating in winter.": str,
    "Other - Write In:What type of central heating does your home have?  Central heating is a system that generates heat for multiple rooms.  \
If you have multiple systems, choose the one that provides your main source of space heating in winter.": str,
    "Radiators:How does your central heating system distribute heat? (Select all that apply)": str,
    "Underfloor heating:How does your central heating system distribute heat? (Select all that apply)": str,
    "Other - Write In:How does your central heating system distribute heat? (Select all that apply)": str,
    "Other - Write In:How does your central heating system distribute heat? (Select all that apply).1": str,
    # You and Your Home
    "What type of property do you live in?": str,
    "Other - Write In:What type of property do you live in?": str,
    "Which of these house and bungalow types best describes your property?": str,
    "Other - Write In:Which of these house and bungalow types best describes your property?": str,
    "Which of these\xa0flat, apartment or maisonette\xa0types best describes your property?": str,
    "Other - Write In:Which of these\xa0flat, apartment or maisonette\xa0types best describes your property?": str,
    "When was your property built?  (for converted properties record when built, not when converted)": str,
    "How many bedrooms does your property have?Please include all rooms intended to be used as a bedroom even if they are currently \
not being used as a bedroom.\xa0\xa0": str,
    "Which of the following best describes your current housing tenure?\xa0\xa0": str,
    "Other - Write In:Which of the following best describes your current housing tenure?\xa0\xa0": str,
    "What is your gender?": str,
    "Other - Write In:What is your gender?": str,
    "How old are you?": str,
    "Which of these ethnic groups do you most identify with?": str,
    "Other - Write In:Which of these ethnic groups do you most identify with?": str,
}

PRE_VISIT_DATE_COLS = ["Time Started", "Date Submitted"]

PRE_VISIT_CATEGORIES = {
    "Status": (["Complete", "Partial"], False),
    "I agree to participate in this survey for the 'visit a heat pump' service. In doing so, I acknowledge: \
- the purpose and nature of the study as described above; \
- that I understand I can withdraw at any time, without repercussions; \
- that Nesta will only use my data for research on the 'visit a heat pump' service; \
- My data will be confidential and held securely.": (
        ["Yes", "No"],
        False,
    ),
    "Why are you planning to visit a heat pump? (Select the most relevant option)": (
        [
            "I'm interested in installing a heat pump into the property I currently live in.",
            "I'm interested in installing a heat pump in a self-build or conversion project.",
            "I'm interested in buying a new-build property that has a heat pump installed.",
            "I'm interested in buying a property with a heat pump already installed, or installing one prior to moving in.",
            "Other - Write In",
        ],
        False,
    ),
    "How did you find out about 'visit a heat pump'? (Select the most relevant option)": (
        [
            "Specific online search",
            "Digital advertisement",
            "Social media post",
            "News article (print or online)",
            "Nesta",
            "Word of mouth recommendation",
            "British Gas",
            "Octopus Energy",
            "EDF",
            "Scottish Power",
            "Snugg",
            "Aira",
            "Loop",
            "Other - Write In",
        ],
        False,
    ),
    "Have you ever previously visited a property with a heat pump?": (
        ["Yes", "No", "Don't know"],
        False,
    ),
    "I understand how a heat pump works.": (["1", "2", "3", "4", "5"], True),
    "I can imagine what it would be like to have a heat pump in my home.": (
        ["1", "2", "3", "4", "5"],
        True,
    ),
    "I am confident that a heat pump would be an effective choice for my home.": (
        ["1", "2", "3", "4", "5"],
        True,
    ),
    "I have a clear understanding of the likely installation costs of a heat pump.": (
        ["1", "2", "3", "4", "5"],
        True,
    ),
    "I have a clear understanding of the likely running costs of a heat pump.": (
        ["1", "2", "3", "4", "5"],
        True,
    ),
    "My next heating system will use a heat pump as the main heat source.": (
        ["1", "2", "3", "4", "5"],
        True,
    ),
    "I know what steps I would need to take to install a heat pump in my own home.": (
        ["1", "2", "3", "4", "5"],
        True,
    ),
    "I have already taken steps to install a heat pump in my home": (
        ["Yes", "No"],
        False,
    ),
    "What type of central heating does your home have?  Central heating is a system that generates heat for multiple rooms.  \
If you have multiple systems, choose the one that provides your main source of space heating in winter.": (
        [
            "No central heating",
            "Gas boiler",
            "Oil boiler",
            "LPG boiler",
            "Direct electric heating (storage heaters, panel heaters)",
            "Other - Write In",
        ],
        False,
    ),
    "What type of property do you live in?": (
        [
            "A whole house",
            "A bungalow",
            "A flat or apartment",
            "A maisonette",
            "Other - Write In",
        ],
        False,
    ),
    "Which of these house and bungalow types best describes your property?": (
        ["Detached", "Semi-Detached", "Mid-terrace", "End-terrace", "Other - Write In"],
        False,
    ),
    "Which of these flat, apartment or maisonette types best describes your property?": (
        [
            "In a purpose-built block of flats or tenement",
            "Part of a converted or shared house",
            "Part of another converted building (e.g. former school, church, or warehouse)",
            "In a commercial building (e.g. in an office building, hotel or over a shop)",
            "Other - Write In",
        ],
        False,
    ),
    "When was your property built?  (for converted properties record when built, not when converted)": (
        [
            "Don't know",
            "Before 1919",
            "1919-1929",
            "1930-1944",
            "1945-1964",
            "1965-1982",
            "1983-1992",
            "1993-2011",
            "2012 or later",
        ],
        True,
    ),
    "How many bedrooms does your property have?Please include all rooms intended to be used as a bedroom even if they are currently \
not being used as a bedroom.": (
        ["1", "2", "3", "4", "5", "6", "7+"],
        True,
    ),
    "Which of the following best describes your current housing tenure?": (
        [
            "Owned outright",
            "Owned with mortgage or loan",
            "Shared ownership",
            "Social rent",
            "Private rent",
            "Other - Write In",
        ],
        False,
    ),
    "What is your gender?": (["Female", "Male", "Prefer not to say"], False),
    "How old are you?": (
        ["Prefer not to say", "18-24", "25-34", "35-44", "44-54", "55-64", "65+"],
        True,
    ),
    "Which of these ethnic groups do you most identify with?": (
        [
            "Asian or Asian British",
            "Black, Black British, Caribbean or African",
            "Mixed or multiple ethnic groups",
            "White",
            "Prefer not to say",
            "Other - Write In",
        ],
        False,
    ),
}

PRE_VISIT_BINARIES = [
    "Being more environmentally friendly:What motivates you to consider a heat pump for your home heating? (Select all that apply)",
    "Saving money on energy bills:What motivates you to consider a heat pump for your home heating? (Select all that apply)",
    "Taking advantage of a grant or subsidy (like the Boiler Upgrade Scheme):What motivates you to consider a heat pump for your home heating? (Select all that apply)",
    "Improving the quality of my heating system:What motivates you to consider a heat pump for your home heating? (Select all that apply)",
    "Improving the quality of my hot water:What motivates you to consider a heat pump for your home heating? (Select all that apply)",
    "My existing system is old and will require replacement soon:What motivates you to consider a heat pump for your home heating? (Select all that apply)",
    "Future proofing my home:What motivates you to consider a heat pump for your home heating? (Select all that apply)",
    "Removing the need for fuel storage (e.g. oil, lpg, wood, coal):What motivates you to consider a heat pump for your home heating? (Select all that apply)",
    "Other - Write In:What motivates you to consider a heat pump for your home heating? (Select all that apply)",
    "How a heat pump works:What are you hoping to find out by visiting a heat pump? (Select all that apply)",
    "What a heat pump looks like:What are you hoping to find out by visiting a heat pump? (Select all that apply)",
    "How much a heat pump costs to install:What are you hoping to find out by visiting a heat pump? (Select all that apply)",
    "How much a heat pump costs to run:What are you hoping to find out by visiting a heat pump? (Select all that apply)",
    "How much noise a heat pump makes:What are you hoping to find out by visiting a heat pump? (Select all that apply)",
    "How much space a heat pump needs:What are you hoping to find out by visiting a heat pump? (Select all that apply)",
    "How easy a heat pump is to control:What are you hoping to find out by visiting a heat pump? (Select all that apply)",
    "About the installation process:What are you hoping to find out by visiting a heat pump? (Select all that apply)",
    "About changes that might be required to my home:What are you hoping to find out by visiting a heat pump? (Select all that apply)",
    "About the experience of living with a heat pump:What are you hoping to find out by visiting a heat pump? (Select all that apply)",
    "About decommissioning my current heating system:What are you hoping to find out by visiting a heat pump? (Select all that apply)",
    "Other - Write In:What are you hoping to find out by visiting a heat pump? (Select all that apply)",
    "Radiators:How does your central heating system distribute heat? (Select all that apply)",
    "Underfloor heating:How does your central heating system distribute heat? (Select all that apply)",
    "Other - Write In:How does your central heating system distribute heat? (Select all that apply)",
]

POST_VISIT_SCHEMA = {
    "Response ID": "int32",
    "Time Started": str,
    "Date Submitted": str,
    "Status": str,
    "Your email address": str,
    "I agree to participate in this survey for the 'visit a heat pump' service. In doing so, I acknowledge: \
- the purpose and nature of the study as described above; \
- that I understand I can withdraw at any time, without repercussions; \
- that Nesta will only use my data for research on the 'visit a heat pump' service; \
- My data will be confidential and held securely.": str,
    "Visiting a heat pump was a worthwhile experience:Your visit": str,
    "I feel more informed about what it is like to live with a heat pump:Your visit": str,
    "I feel more informed about the process of choosing and installing a heat pump.:Your visit": str,
    "Visiting a heat pump has given me more confidence to explore my home heating options.:Your visit": str,
    "The heat pump owner was welcoming.:The host": str,
    "The heat pump owner was knowledgeable.:The host": str,
    "The heat pump owner was able to answer my questions.:The host": str,
    "The heat pump owner gave useful insight on owning a heat pump.:The host": str,
    "The ‘visit a heat pump’ website was easy to use.:The website": str,
    "The ‘visit a heat pump’ website was clear and easy to understand.:The website": str,
    "The ‘visit a heat pump’ website provides an important service.:The website": str,
    "The ‘visit a heat pump’ website had all the information I needed for the visit.:The website": str,
    "I went on my own:Did you attend 'visit a heat pump' with anyone else? (Select all that apply)": str,
    "I went with a partner/spouse:Did you attend 'visit a heat pump' with anyone else? (Select all that apply)": str,
    "I went with a parent or older relative:Did you attend 'visit a heat pump' with anyone else? (Select all that apply)": str,
    "I went with a child or younger relative (over the age of 18):Did you attend 'visit a heat pump' with anyone else? (Select all that apply)": str,
    "I went with a friend or colleague:Did you attend 'visit a heat pump' with anyone else? (Select all that apply)": str,
    "Other - Write In:Did you attend 'visit a heat pump' with anyone else? (Select all that apply)": str,
    "Other - Write In:Did you attend 'visit a heat pump' with anyone else? (Select all that apply).1": str,
    "How many people have you spoken to about visiting a heat pump? (Please exclude anyone you visited with)": str,
    "Considering your 'visit a heat pump' experience, how likely are you to recommend it to a friend or colleague?": "Int64",
    "How did you find out about Visit A Heat Pump?": str,
    "I understand how a heat pump works.": str,
    "I can imagine what it would be like to have a heat pump in my home.\xa0\xa0": str,
    "I am confident that a heat pump would be an effective choice for my home.\xa0\xa0": str,
    "I have a clear understanding of the likely\xa0installation costs\xa0of a heat pump.\xa0\xa0": str,
    "I have a clear understanding of the likely\xa0running costs\xa0of a heat pump.\xa0\xa0": str,
    "My next heating system will use a heat pump as the main heat source.\xa0\xa0": str,
    "I know what steps I would need to take to install a heat pump in my own home.\xa0\xa0": str,
    "I have already taken steps to install a heat pump in my home": str,
    "Are you missing any information about installing or living with a heat pump that you feel you need to take action?": str,
    "What barriers, if any, do you feel you need to overcome before you can install a heat pump in your home?": str,
    "In the UK, the way we heat almost all of our homes will need to change to help address climate change.:The home energy transition": str,
    "Homeowners have a responsibility to upgrade their homes to use low carbon heating technologies, like heat pumps.:The home energy transition": str,
    "The Government has a duty to ensure all UK households adopt low carbon heating technologies, like heat pumps.:The home energy transition": str,
    "Comments.1": str,
}

POST_VISIT_DATE_COLS = ["Time Started", "Date Submitted"]

POST_VISIT_CATEGORIES = {
    "Status": (["Complete", "Partial"], False),
    "I agree to participate in this survey for the 'visit a heat pump' service. In doing so, I acknowledge: \
- the purpose and nature of the study as described above; \
- that I understand I can withdraw at any time, without repercussions; \
- that Nesta will only use my data for research on the 'visit a heat pump' service; \
- My data will be confidential and held securely.": (
        ["Yes", "No"],
        False,
    ),
    "Visiting a heat pump was a worthwhile experience:Your visit": (
        [
            "Disagree Strongly",
            "Disagree",
            "Neither Agree nor Disagree",
            "Agree",
            "Agree Strongly",
        ],
        True,
    ),
    "I feel more informed about what it is like to live with a heat pump:Your visit": (
        [
            "Disagree Strongly",
            "Disagree",
            "Neither Agree nor Disagree",
            "Agree",
            "Agree Strongly",
        ],
        True,
    ),
    "I feel more informed about the process of choosing and installing a heat pump.:Your visit": (
        [
            "Disagree Strongly",
            "Disagree",
            "Neither Agree nor Disagree",
            "Agree",
            "Agree Strongly",
        ],
        True,
    ),
    "Visiting a heat pump has given me more confidence to explore my home heating options.:Your visit": (
        [
            "Disagree Strongly",
            "Disagree",
            "Neither Agree nor Disagree",
            "Agree",
            "Agree Strongly",
        ],
        True,
    ),
    "The heat pump owner was welcoming.:The host": (
        [
            "Disagree strongly",
            "Disagree",
            "Neither agree nor disagree",
            "Agree",
            "Agree strongly",
        ],
        True,
    ),
    "The heat pump owner was knowledgeable.:The host": (
        [
            "Disagree strongly",
            "Disagree",
            "Neither agree nor disagree",
            "Agree",
            "Agree strongly",
        ],
        True,
    ),
    "The heat pump owner was able to answer my questions.:The host": (
        [
            "Disagree strongly",
            "Disagree",
            "Neither agree nor disagree",
            "Agree",
            "Agree strongly",
        ],
        True,
    ),
    "The heat pump owner gave useful insight on owning a heat pump.:The host": (
        [
            "Disagree strongly",
            "Disagree",
            "Neither agree nor disagree",
            "Agree",
            "Agree strongly",
        ],
        True,
    ),
    "The 'visit a heat pump' website was easy to use.:The website": (
        [
            "Disagree strongly",
            "Disagree",
            "Neither agree nor disagree",
            "Agree",
            "Agree strongly",
        ],
        True,
    ),
    "The 'visit a heat pump' website was clear and easy to understand.:The website": (
        [
            "Disagree strongly",
            "Disagree",
            "Neither agree nor disagree",
            "Agree",
            "Agree strongly",
        ],
        True,
    ),
    "The 'visit a heat pump' website provides an important service.:The website": (
        [
            "Disagree strongly",
            "Disagree",
            "Neither agree nor disagree",
            "Agree",
            "Agree strongly",
        ],
        True,
    ),
    "The 'visit a heat pump' website had all the information I needed for the visit.:The website": (
        [
            "Disagree strongly",
            "Disagree",
            "Neither agree nor disagree",
            "Agree",
            "Agree strongly",
        ],
        True,
    ),
    "How many people have you spoken to about visiting a heat pump? (Please exclude anyone you visited with)": (
        [
            "Don't know",
            "No one",
            "1 person",
            "2 or 3 people",
            "4 or 5 people",
            "6 to 10 people",
            "More than 10 people",
        ],
        True,
    ),
    "How did you find out about Visit A Heat Pump?": (
        [
            "British Gas",
            "Octopus",
            "EDF",
            "Scottish Power",
            "Snugg",
            "Aira",
            "Loop",
            "Other",
        ],
        False,
    ),
    "I understand how a heat pump works.": (["1", "2", "3", "4", "5"], True),
    "I can imagine what it would be like to have a heat pump in my home.": (
        ["1", "2", "3", "4", "5"],
        True,
    ),
    "I am confident that a heat pump would be an effective choice for my home.": (
        ["1", "2", "3", "4", "5"],
        True,
    ),
    "I have a clear understanding of the likely installation costs of a heat pump.": (
        ["1", "2", "3", "4", "5"],
        True,
    ),
    "I have a clear understanding of the likely running costs of a heat pump.": (
        ["1", "2", "3", "4", "5"],
        True,
    ),
    "My next heating system will use a heat pump as the main heat source.": (
        ["1", "2", "3", "4", "5"],
        True,
    ),
    "I know what steps I would need to take to install a heat pump in my own home.": (
        ["1", "2", "3", "4", "5"],
        True,
    ),
    "I have already taken steps to install a heat pump in my home": (
        ["Yes", "No"],
        False,
    ),
    "In the UK, the way we heat almost all of our homes will need to change to help address climate change.\
:The home energy transition": (
        [
            "Disagree strongly",
            "Disagree",
            "Neither agree nor disagree",
            "Agree",
            "Agree strongly",
        ],
        True,
    ),
    "Homeowners have a responsibility to upgrade their homes to use low carbon heating technologies, like heat pumps.\
:The home energy transition": (
        [
            "Disagree strongly",
            "Disagree",
            "Neither agree nor disagree",
            "Agree",
            "Agree strongly",
        ],
        True,
    ),
    "The Government has a duty to ensure all UK households adopt low carbon heating technologies, like heat pumps.\
:The home energy transition": (
        [
            "Disagree strongly",
            "Disagree",
            "Neither agree nor disagree",
            "Agree",
            "Agree strongly",
        ],
        True,
    ),
}

POST_VISIT_BINARIES = [
    "I went on my own:Did you attend 'visit a heat pump' with anyone else? (Select all that apply)",
    "I went with a partner/spouse:Did you attend 'visit a heat pump' with anyone else? (Select all that apply)",
    "I went with a parent or older relative:Did you attend 'visit a heat pump' with anyone else? (Select all that apply)",
    "I went with a child or younger relative (over the age of 18):Did you attend 'visit a heat pump' with anyone else? (Select all that apply)",
    "I went with a friend or colleague:Did you attend 'visit a heat pump' with anyone else? (Select all that apply)",
    "Other - Write In:Did you attend 'visit a heat pump' with anyone else? (Select all that apply)",
]

FOLLOW_UP_SCHEMA = {
    "Response ID": "int32",
    "Time Started": str,
    "Date Submitted": str,
    "Status": str,
    "Your email address": str,
    "I agree to participate in this survey for the 'visit a heat pump' service. In doing so, I acknowledge: \
- the purpose and nature of the study as described above; \
- that I understand I can withdraw at any time, without repercussions; \
- that Nesta will only use my data for research on the 'visit a heat pump' service; \
- My data will be confidential and held securely.": str,
    "Thinking back to your 'visit a heat pump' experience, did you it to recommend it to a friend or colleague?": str,
    "Since you visited a heat pump, have you done any of the following? (Select the thing you've done most recently if multiple options apply)": str,
    "What is your main source of home heating?": str,
    "Other - Write In:What is your main source of home heating?": str,
    "Comments.1": str,
    "I understand how a heat pump works.\xa0\xa0": str,
    "I can imagine what it would be like to have a heat pump in my home.\xa0\xa0": str,
    "I am confident that a heat pump would be an effective choice for my home.\xa0\xa0": str,
    "My next heating system will use a heat pump as the main heat source.\xa0\xa0": str,
    "I know what steps I would need to take to install a heat pump in my own home.\xa0\xa0": str,
    "I anticipate replacing my current heating system within the next:": str,
    "I have made energy efficiency improvements (e.g. draught proofing, glazing, insulation) to ensure my home is ready for a heat pump in the future.": str,
    "I have taken financial steps (e.g. begun saving, earmarked savings, explored financing) towards buying a heat pump.": str,
    "I have contacted one or more installers to inquire about heat pumps.\xa0\xa0": str,
    "I have instructed one or more installers to provide a quote for a heat pump.\xa0\xa0": str,
    "I have had a heat loss survey conducted for the purpose of specifying a heat pump installation.\xa0\xa0": str,
    "Comments.2": str,
}

FOLLOW_UP_DATE_COLS = ["Time Started", "Date Submitted"]

FOLLOW_UP_CATEGORIES = {
    "Status": (["Complete", "Partial"], False),
    "I agree to participate in this survey for the 'visit a heat pump' service. In doing so, I acknowledge: \
- the purpose and nature of the study as described above; \
- that I understand I can withdraw at any time, without repercussions; \
- that Nesta will only use my data for research on the 'visit a heat pump' service; \
- My data will be confidential and held securely.": (
        ["Yes", "No"],
        False,
    ),
    "Thinking back to your 'visit a heat pump' experience, did you it to recommend it to a friend or colleague?": (
        ["Yes", "No", "Not sure"],
        False,
    ),
    "Since you visited a heat pump, have you done any of the following? (Select the thing you've done most recently if multiple options apply)": (
        [
            "Replaced, changed or upgraded the main heating source in your house (or a landlord has taken equivalent action).",
            "Built a new home (self-build).",
            "Bought a new build home from a developer.",
            "Bought a home that is new to you (but not a new build).",
            "Moved into a new private or socially rented property.",
            "Renovated or extended my property.",
            "None of the above",
        ],
        False,
    ),
    "What is your main source of home heating?": (
        [
            "A heat pump",
            "Another low carbon heat source",
            "Gas boiler",
            "Oil Boiler",
            "LPG Boiler",
            "Direct electric heating (e.g. storage heaters, panel heaters)",
            "Other - Write In",
        ],
        False,
    ),
    "I understand how a heat pump works.": (["1", "2", "3", "4", "5"], True),
    "I can imagine what it would be like to have a heat pump in my home.": (
        ["1", "2", "3", "4", "5"],
        True,
    ),
    "I am confident that a heat pump would be an effective choice for my home.": (
        ["1", "2", "3", "4", "5"],
        True,
    ),
    "My next heating system will use a heat pump as the main heat source.": (
        ["1", "2", "3", "4", "5"],
        True,
    ),
    "I know what steps I would need to take to install a heat pump in my own home.": (
        ["1", "2", "3", "4", "5"],
        True,
    ),
    "I anticipate replacing my current heating system within the next:": (
        ["Don't know", "Year", "2 years", "5 years", "10 years"],
        True,
    ),
    "I have made energy efficiency improvements (e.g. draught proofing, glazing, insulation) to ensure my home is ready for a heat pump in the future.": (
        ["Yes", "No", "Not applicable"],
        False,
    ),
    "I have taken financial steps (e.g. begun saving, earmarked savings, explored financing) towards buying a heat pump.": (
        ["Yes", "No", "Not applicable"],
        False,
    ),
    "I have contacted one or more installers to inquire about heat pumps.": (
        ["Yes", "No", "Not applicable"],
        False,
    ),
    "I have instructed one or more installers to provide a quote for a heat pump.": (
        ["Yes", "No", "Not applicable"],
        False,
    ),
    "I have had a heat loss survey conducted for the purpose of specifying a heat pump installation.": (
        ["Yes", "No", "Not applicable"],
        False,
    ),
}

LINKED_COLUMNS = [
    "Response ID",
    "Time Started",
    "Date Submitted",
    "visitor_id",
    "wave",
    "Status",
    "I agree to participate in this survey for the 'visit a heat pump' service. In doing so, I acknowledge: \
- the purpose and nature of the study as described above; \
- that I understand I can withdraw at any time, without repercussions; \
- that Nesta will only use my data for research on the 'visit a heat pump' service; \
- My data will be confidential and held securely.",
    "I understand how a heat pump works.",
    "I can imagine what it would be like to have a heat pump in my home.",
    "I am confident that a heat pump would be an effective choice for my home.",
    "I have a clear understanding of the likely installation costs of a heat pump.",
    "I have a clear understanding of the likely running costs of a heat pump.",
    "My next heating system will use a heat pump as the main heat source.",
    "I know what steps I would need to take to install a heat pump in my own home.",
    "I have already taken steps to install a heat pump in my home",
    "What type of central heating does your home have?  Central heating is a system that generates heat for multiple rooms.  \
If you have multiple systems, choose the one that provides your main source of space heating in winter.",
    "Other - Write In:What type of central heating does your home have?  Central heating is a system that generates heat for multiple rooms.  \
If you have multiple systems, choose the one that provides your main source of space heating in winter.",
    "Radiators:How does your central heating system distribute heat? (Select all that apply)",
    "Underfloor heating:How does your central heating system distribute heat? (Select all that apply)",
    "Other - Write In:How does your central heating system distribute heat? (Select all that apply)",
    "Other - Write In:How does your central heating system distribute heat? (Select all that apply).1",
    "What type of property do you live in?",
    "Other - Write In:What type of property do you live in?",
    "Which of these house and bungalow types best describes your property?",
    "Other - Write In:Which of these house and bungalow types best describes your property?",
    "Which of these flat, apartment or maisonette types best describes your property?",
    "Other - Write In:Which of these flat, apartment or maisonette types best describes your property?",
    "When was your property built?  (for converted properties record when built, not when converted)",
    "How many bedrooms does your property have?Please include all rooms intended to be used as a bedroom even if they are currently not being used as a bedroom.",
    "Which of the following best describes your current housing tenure?",
    "Other - Write In:Which of the following best describes your current housing tenure?",
    "What is your gender?",
    "Other - Write In:What is your gender?",
    "How old are you?",
    "Which of these ethnic groups do you most identify with?",
    "Other - Write In:Which of these ethnic groups do you most identify with?",
    "What is your main source of home heating?",
    "Other - Write In:What is your main source of home heating?",
    "I anticipate replacing my current heating system within the next:",
    "I have made energy efficiency improvements (e.g. draught proofing, glazing, insulation) to ensure my home is ready for a heat pump in the future.",
    "I have taken financial steps (e.g. begun saving, earmarked savings, explored financing) towards buying a heat pump.",
    "I have contacted one or more installers to inquire about heat pumps.",
    "I have instructed one or more installers to provide a quote for a heat pump.",
    "I have had a heat loss survey conducted for the purpose of specifying a heat pump installation.",
]
