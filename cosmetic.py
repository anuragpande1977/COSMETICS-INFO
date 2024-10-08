import pandas as pd
import streamlit as st

# URL to your CSV file on GitHub
csv_url = "https://raw.githubusercontent.com/anuragpande1977/COSMETICS-INFO/main/cosmetics.csv"

# Read CSV file from GitHub
df = pd.read_csv(csv_url)

# Split the "FUNCTION/ACTIVITY" column by commas and create a set of unique functions
df['FUNCTION/ACTIVITY'] = df['FUNCTION/ACTIVITY'].str.split(',')
all_functions = set()
for function_list in df['FUNCTION/ACTIVITY']:
    for function in function_list:
        all_functions.add(function.strip())

# Convert the set to a sorted list for the dropdown
function_options = sorted(list(all_functions))

# Set the page style to add some color to the input widgets
st.markdown("""
    <style>
    .stSelectbox, .stButton {
        background-color: #F0F8FF;
        border: 2px solid #ADD8E6;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit app title
st.title("Cosmetic Ingredient Finder")

# User inputs: Select a unique function and formulation format
function = st.selectbox("Select a cosmetic function/activity:", function_options, key="function_selectbox")
format = st.selectbox("Select a formulation format:", df['FORMULATION FORMAT'].unique(), key="format_selectbox")

# Filter the data based on user input
filtered_df = df[df['FUNCTION/ACTIVITY'].apply(lambda x: function in [f.strip() for f in x]) & (df['FORMULATION FORMAT'] == format)]

# Display the results
for index, row in filtered_df.iterrows():
    st.subheader(f"Product: {row['PRODUCT NAME']}")
    st.write(f"**INCI Name**: {row['INCI NAME']}")
    st.write(f"**Source**: {row['SOURCE (NAME AND PART)']}")
    st.write(f"**Bioactive Percentage**: {row['BIOACTIVE PERCENTAGE']}")
    st.write(f"**Appearance**: {row['APPEARANCE']}")
    st.write(f"**Suggested Concentration**: {row['SUGGESTED CONCENTRATION']}")
    st.write(f"**Marketing Claims**: {row['MARKETING CLAIMS']}")

# Footer with the data source
st.write("Data sourced from cosmetics.csv uploaded on GitHub")
