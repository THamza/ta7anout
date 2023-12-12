import streamlit as st
from data_processor import load_data, process_data
from tabs import overview, analysis, data_view
from utils import css_injector, translator
from components import cards, graphs
from utils.translator import Translator

# Set page config
st.set_page_config(page_title="Product Sales Dashboard", layout="wide")


# Instantiate the Translator
translator = Translator()

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
    if 'SKU' in data.columns:
        selected_sku = st.sidebar.multiselect(translation["select_sku"], options=data['SKU'].unique())
        if selected_sku:
            data = data[data['SKU'].isin(selected_sku)]
            # Reset index after filtering
            data.reset_index(drop=True, inplace=True)

    # Tabs setup
    tab1, tab2, tab3 = st.tabs([translation["overview_tab"], translation["analysis_tab"], translation["data_view_tab"]])

    # Overview Tab Content
    with tab1:
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
