import streamlit as st
from data_processor import load_data, process_data
from tabs import overview, analysis, data_view
from utils import css_injector, translator
from components import cards, graphs
from utils.translator import Translator
import pandas as pd

# Set page config
st.set_page_config(page_title="Product Sales Dashboard", layout="wide")


# Instantiate the Translator
translator = Translator()


def convert_to_float(value):
    # If it's already a numeric type, return it as is
    if isinstance(value, (int, float)):
        return value

    # If it's None or a variant of NaN, return 0.0
    if pd.isnull(value):
        return 0.0

    # If the value is 'Non Numérique' or an empty string, return 0.0
    if value in ['Non Numérique', '', 'nan', 'NaN']:
        return 0.0

    # If the value is a string, attempt to clean and convert it
    if isinstance(value, str):
        # Remove common non-numeric characters
        non_numeric_chars = [',', '%', '$', '€', '£', 'Dhs']
        for char in non_numeric_chars:
            value = value.replace(char, '')

        # Strip whitespace and convert to float
        try:
            return float(value.strip())
        except ValueError:
            # Log an error if conversion fails
            st.error(f"Could not convert value to float: {value}")
            return 0.0

    # If value is some other type, log an error and return 0.0
    st.error(f"Encountered unexpected data type: {type(value)}")
    return 0.0

def validate_data(data):
    # Check if any NaN values are present after conversion
    data = data.fillna(0)
    if data.isnull().any().any():
        st.error("Some columns contain non-numeric values that could not be converted.")
        # Handle NaN values as required, such as replacing with zeros

    return data



def main():
    # Inject custom CSS
    css_injector.add_custom_css()

    # Sidebar language selector
    language = st.sidebar.selectbox(
        "Language",
        list(translator.translations.keys())
    )

    # Retrieve translations for the selected language
    translation = {key: translator.get_translation(language, key) for key in translator.translations["English"].keys()}

    # Initialize data
    data = None

    # Initialize data and upload file section
    uploaded_file = st.file_uploader(
    translation["upload_prompt"], 
    type=["csv", "xls", "xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]
)

    
    if uploaded_file is not None:
        # Check the file extension and process accordingly
        file_extension = uploaded_file.name.split('.')[-1].lower()
        if file_extension in ['csv', 'xls', 'xlsx']:
            data = process_data(uploaded_file, file_extension)
        else:
            st.error(translation["file_type_error"])  # Provide a translation for unsupported file types

        if data is None:
            st.error(translation["process_error"])
        else:
            # Show this warning if no file is uploaded
            st.warning(translation["please_upload"])

    # # Now use the translation dict to access the translations
    # uploaded_file = st.file_uploader(translation["upload_prompt"], type="csv")  # Assuming you have a key "upload_prompt"

    # if uploaded_file is not None:
    #     # Process the uploaded file
    #     data = process_data(uploaded_file)
    #     if data is None:
    #         st.error(translation("Error: Could not process the uploaded file. Please check the file and try again."))
    #         return

    # Ensure data is not empty
    if data is None or data.empty:
        st.warning(translation["please_upload"])
        return

    # Replace the title
    st.title(translation["title"])
    # Replace the sidebar header
    st.sidebar.header(translation["filter"])

    # Filtering options in sidebar
    if 'Produit' in data.columns:
        selected_sku = st.sidebar.multiselect(translation["select_sku"], options=data['Produit'].unique())
        if selected_sku:
            data = data[data['Produit'].isin(selected_sku)]
            # Reset index after filtering
            data.reset_index(drop=True, inplace=True)

    # Tabs setup
    tab1, tab2, tab3 = st.tabs([translation["overview_tab"], translation["analysis_tab"], translation["data_view_tab"]])

    # Apply this function to your data columns that require numeric conversion
    data['Coût'] = data['Coût'].apply(convert_to_float)
    data['Marge'] = data['Marge'].apply(convert_to_float)
    data['Total'] = data['Total'].apply(convert_to_float)
    # Overview Tab Content
    with tab1:
        validation_result = validate_data(data)
        if validation_result is None:
            st.error(translation["data_error"])
            return
        overview.show(data, translation)

    # Detailed Analysis Tab Content
    with tab2:
        analysis.show(data, translation)

    # Data View Tab Content
    with tab3:
        data_view.show(data, translation)

    # Download CSV button
    st.download_button(
        label=translation["download_csv"],
        data=graphs.convert_df_to_csv(data),
        file_name='sales_data.csv',
        mime='text/csv'
    )

    # Display statistical summary
    if st.checkbox(translation["show_summary"]):
        st.write(data.describe())

# Run the main function
if __name__ == "__main__":
    main()
