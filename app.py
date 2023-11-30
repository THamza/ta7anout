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

    # Inject Google Analytics script
    google_analytics_script = """
    <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-JQ58XEGTNZ"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-JQ58XEGTNZ');
        </script>
    """
    st.markdown(google_analytics_script, unsafe_allow_html=True)


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
    uploaded_file = st.file_uploader(translation["upload_prompt"], type="csv")
    if uploaded_file is not None:
        data = process_data(uploaded_file)
        if data is None:
            st.error(translation["process_error"])  # Assuming you have a key "process_error" in your translations

    # Check if data is loaded and not empty
    if data is None or data.empty:
        st.warning(translation["please_upload"])  # Assuming you have a key "please_upload" in your translations
        return  # If data is None or empty, return to prevent executing the rest of the code


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
        st.warning(translation("Please upload a CSV file to view the dashboard."))
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
