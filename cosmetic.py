import pandas as pd
import streamlit as st

# Corrected URL to your Excel file on GitHub
excel_url = "https://raw.githubusercontent.com/anuragpande1977/COSMETICS-INFO/main/Cosmetic%20book.xlsx"

# Read Excel file from GitHub
df = pd.read_excel(excel_url, sheet_name="Sheet1")

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

# User inputs: Select function and formulation format
function = st.selectbox("Select a cosmetic function/activity:", df['Function/Activity'].unique(), key="function_selectbox")
format = st.selectbox("Select a formulation format:", df['Formulation Format'].unique(), key="format_selectbox")

# Filter the data based on user input
filtered_df = df[(df['Function/Activity'] == function) & (df['Formulation Format'] == format)]

# Display the results
for index, row in filtered_df.iterrows():
    st.subheader(f"Product: {row['Product Name']}")
    st.write(f"**INCI Name**: {row['INCI Name']}")
    st.write(f"**Source**: {row['Source (Name and Part)']}")
    st.write(f"**Bioactive Percentage**: {row['Bioactive Percentage']}")
    st.write(f"**Appearance**: {row['Appearance']}")
    st.write(f"**Suggested Concentration**: {row['Suggested Concentration']}")
    st.write(f"**Marketing Claims**: {row['Marketing Claims']}")

# Footer with the data source
st.write("Data sourced from Cosmetic Book Excel uploaded on GitHub")
