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

# Step 1: User selects function/activity
st.title("Cosmetic Ingredient Finder")
function = st.selectbox("Select a cosmetic function/activity:", function_options, key="function_selectbox")

# Step 2: Filter products based on function/activity
filtered_products = df[df['FUNCTION/ACTIVITY'].apply(lambda x: function in [f.strip() for f in x])]

if not filtered_products.empty:
    # Step 3: Display the product names for the user to select
    product_names = filtered_products['PRODUCT NAME'].unique()
    selected_product = st.selectbox("Select a product:", product_names, key="product_selectbox")
    
    # Step 4: Filter formulation formats based on the selected product
    product_filtered_df = filtered_products[filtered_products['PRODUCT NAME'] == selected_product]
    formulation_formats = product_filtered_df['FORMULATION FORMAT'].unique()
    selected_format = st.selectbox("Select a formulation format:", formulation_formats, key="format_selectbox")
    
    # Step 5: Display the details for the selected product and format
    final_product_details = product_filtered_df[product_filtered_df['FORMULATION FORMAT'] == selected_format]
    
    if not final_product_details.empty:
        row = final_product_details.iloc[0]  # Assuming only one row matches the selection

        # Create a styled table with product details split into two rows
        product_data_row1 = {
            "INCI Name": [row['INCI NAME']],
            "Source": [row['SOURCE (NAME AND PART)']],
            "Bioactive Percentage": [row['BIOACTIVE PERCENTAGE']],
        }
        
        product_data_row2 = {
            "Appearance": [row['APPEARANCE']],
            "Suggested Concentration": [row['SUGGESTED CONCENTRATION']],
            "Marketing Claims": [row['MARKETING CLAIMS']]
        }
        
        # Display the first row of product details
        st.subheader(f"Product Details for {row['PRODUCT NAME']}")
        st.write("Product Information (Row 1):")
        st.dataframe(pd.DataFrame(product_data_row1).style.set_properties(**{
            'background-color': '#F5F5F5',
            'color': '#000000',
            'border-color': 'white',
            'font-size': '14px',
            'text-align': 'left',
        }))
        
        # Display the second row of product details
        st.write("Product Information (Row 2):")
        st.dataframe(pd.DataFrame(product_data_row2).style.set_properties(**{
            'background-color': '#F5F5F5',
            'color': '#000000',
            'border-color': 'white',
            'font-size': '14px',
            'text-align': 'left',
        }))
else:
    st.write("No products found matching your selection.")

# Footer with the data source
st.write("Data sourced from cosmetics.csv uploaded on GitHub")
