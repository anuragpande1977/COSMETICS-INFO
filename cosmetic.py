import pandas as pd
import streamlit as st

# URL to your CSV file on GitHub
csv_url = "https://raw.githubusercontent.com/anuragpande1977/COSMETICS-INFO/main/cosmetics.csv"

# Read CSV file from GitHub
df = pd.read_csv(csv_url)

# Assuming that the "FORMULATION FORMAT" column contains both product type (LEAVE ON, RINSE OFF) and individual formats in parentheses
df['FORMULATION FORMAT'] = df['FORMULATION FORMAT'].apply(lambda x: str(x).replace(')', '').replace('(', '').split(',') if pd.notna(x) else [])

# Initialize empty sets to store unique product types and formats
all_product_types = set()
all_formats = set()

# Separate product types (LEAVE ON, RINSE OFF) and individual formats (serum, cream, etc.)
for format_list in df['FORMULATION FORMAT']:
    if isinstance(format_list, list):
        for format_item in format_list:
            format_item = format_item.strip()
            # Check if the format contains "LEAVE ON" or "RINSE OFF" to classify
            if "LEAVE ON" in format_item or "RINSE OFF" in format_item:
                all_product_types.add(format_item)
            else:
                all_formats.add(format_item)

# Convert the sets to sorted lists for the dropdown
product_type_options = sorted(list(all_product_types))
format_options = sorted(list(all_formats))

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

# User inputs: Select product type (LEAVE ON/RINSE OFF) and formulation format
product_type = st.selectbox("Select a product type (LEAVE ON/RINSE OFF):", product_type_options, key="product_type_selectbox")
format = st.selectbox("Select a formulation format:", format_options, key="format_selectbox")

# Filter the data based on user input
filtered_df = df[df['FORMULATION FORMAT'].apply(lambda x: product_type in [f.strip() for f in x]) & df['FORMULATION FORMAT'].apply(lambda x: format in [f.strip() for f in x])]

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

