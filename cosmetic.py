import pandas as pd
import streamlit as st

# URL to your CSV file on GitHub
csv_url = "https://raw.githubusercontent.com/anuragpande1977/COSMETICS-INFO/main/cosmetics.csv"

# Read CSV file from GitHub
df = pd.read_csv(csv_url)

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

# User inputs: Select function and formulation format using the correct column names
function = st.selectbox("Select a cosmetic function/activity:", df['FUNCTION/ACTIVITY'].unique(), key="function_selectbox")
format = st.selectbox("Select a formulation format:", df['FORMULATION FORMAT'].unique(), key="format_selectbox")

# Filter the data based on user input
filtered_df = df[(df['FUNCTION/ACTIVITY'] == function) & (df['FORMULATION FORMAT'] == format)]

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

