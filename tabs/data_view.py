import streamlit as st

def show(data, translations):
    """
    Displays the data view tab in the Streamlit app.

    Parameters:
    - data: The processed DataFrame that contains the data to display.
    - translations: A dictionary containing translation mappings for text.
    """
    st.markdown("## " + translations["data_view_tab"])

    # You can add options for the user to choose columns to display, sort the data, or apply additional filters.
    st.markdown("### " + translations["data_table"])
    # Display a snapshot of the data or use a custom table component.
    st.dataframe(data)
    
    # Additional features like downloading the data as a CSV file can also be included.
    st.markdown("### " + translations["download_csv"])
    st.download_button(
        label=translations["download_csv"],
        data=data.to_csv().encode('utf-8'),
        file_name='detailed_data.csv',
        mime='text/csv',
        key='download-csv'
    )
    
    # If your dataset is large, consider adding a paginator to view data in chunks.
    # paginator = Paginator(data)
    # page = st.number_input(label="Page Number", min_value=1, max_value=paginator.max_page, value=1)
    # st.dataframe(paginator.get_page(page))
    
    # If data is very large, you can provide options to display only a subset of data.
    # For example, you could add a slider to let the user decide how many rows to view.
    # row_count = st.slider("Number of rows to display", 1, len(data), 50)
    # st.dataframe(data.head(row_count))

# A paginator class (optional) to handle large datasets
# class Paginator:
#     def __init__(self, dataframe, rows_per_page=50):
#         self.dataframe = dataframe
#         self.rows_per_page = rows_per_page
#         self.max_page = (len(dataframe) - 1) // rows_per_page + 1

#     def get_page(self, page_number):
#         start_row = (page_number - 1) * self.rows_per_page
#         end_row = start_row + self.rows_per_page
#         return self.dataframe.iloc[start_row:end_row]
