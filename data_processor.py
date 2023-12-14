import pandas as pd
import streamlit as st

def process_data(uploaded_file, file_extension):
    """
    Process the uploaded CSV file.

    Parameters:
    - uploaded_file: The uploaded file object from Streamlit's file_uploader.

    Returns:
    - A pandas DataFrame if successful, None otherwise.
    """
    if uploaded_file is not None:
        try:
            if file_extension == 'csv':
                data = pd.read_csv(uploaded_file)
            elif file_extension in ['xls', 'xlsx']:
                data = pd.read_excel(uploaded_file)
            else:
                return None  # Handle other file formats or raise an error

            data.rename(columns={"Produit": "SKU", "Quantité": "Quantity", "Coût": "Price", "Marge": "Margin"}, inplace=True)
            # Perform some basic validation
            if 'Produit' not in data.columns:
                st.error("The uploaded file must have an 'Produit' column.")
                return None
            # Add additional necessary validations as needed
            return data
        except pd.errors.EmptyDataError:
            st.error("The uploaded file is empty.")
        except pd.errors.ParserError:
            st.error("The uploaded file could not be parsed.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    return None


def load_data(file_path):
    """
    Load data from a CSV file at the given file path.

    Parameters:
    - file_path: The path to the CSV file.

    Returns:
    - A pandas DataFrame if successful, None otherwise.
    """
    try:
        data = pd.read_csv(file_path)
        # Perform some basic validation
        if 'Produit' not in data.columns:
            st.error("The CSV file must have an 'Produit' column.")
            return None
        # Add additional necessary validations as needed
        return data
    except pd.errors.EmptyDataError:
        st.error("The CSV file is empty.")
    except pd.errors.ParserError:
        st.error("The CSV file could not be parsed.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
    return None
