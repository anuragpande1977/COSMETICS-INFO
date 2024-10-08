import pandas as pd
import streamlit as st

# URL to your CSV file on GitHub
csv_url = "https://raw.githubusercontent.com/anuragpande1977/COSMETICS-INFO/main/cosmetics.csv"

# Read CSV file from GitHub
df = pd.read_csv(csv_url)

# Split the "FUNCTION/ACTIVITY" column by commas where applicable
df['FUNCTION/ACTIVITY'] = df['FUNCTION/ACTIVITY'].apply(lambda x: str(x).split(',') if pd.notna(x) else [])

# Initialize an empty set to store unique functions
all_functions = set()

# Populate unique functions
for function_list in df['FUNCTION/ACTIVITY']:
    if isinstance(function_list, list):
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

# User inputs: Select function/activity
function = st.selectbox("Select a cosmetic function/activity:", function_options, key="function_selectbox")

# Filter the data based on user input
filtered_df = df[df['FUNCTION/ACTIVITY'].apply(lambda x: function in [f.strip() for f in x])]

# Display the results
if not filtered_df.empty:
    for index, row in filtered_df.iterrows():
        st.subheader(f"Product: {row['PRODUCT NAME']}")
        st.write(f"**INCI Name**: {row['INCI NAME']}")
        st.write(f"**Source**: {row['SOURCE (NAME AND PART)']}")
        st.write(f"**Bioactive Percentage**: {row['BIOACTIVE PERCENTAGE']}")
        st.write(f"**Appearance**: {row['APPEARANCE']}")
        st.write(f"**Suggested Concentration**: {row['SUGGESTED CONCENTRATION']}")
        st.write(f"**Marketing Claims**: {row['MARKETING CLAIMS']}")
        st.write(f"**Formulation Type**: {row['FORMULATION FORMAT']}")
else:
    st.write("No products found matching your criteria. Please try a different selection.")

# Footer with the data source
st.write("Data sourced from cosmetics.csv uploaded on GitHub")
