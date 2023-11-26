import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Translations for each language
translations = {
    "English": {
        "title": "Product Sales Dashboard",
        "filter": "Filter Data",
        "average_price": "Average Price",
        "average_margin": "Average Margin",
        "select_sku": "Select SKU",
        "overview_tab": "Overview",
        "analysis_tab": "Detailed Analysis",
        "data_view_tab": "Data View",
        "sales_over_time": "Sales Over Time",
        "margin_analysis": "Margin Analysis",
        "top_selling_products": "Top Selling Products",
        "data_table": "Data Table",
        "download_csv": "Download data as CSV",
        "show_summary": "Show Summary Statistics",
    },
    "Français": {
        "title": "Tableau de Bord des Ventes de Produits",
        "filter": "Filtrer les Données",
        "average_price": "Prix Moyen",
        "average_margin": "Marge Moyenne",
        "select_sku": "Sélectionner le SKU",
        "overview_tab": "Aperçu",
        "analysis_tab": "Analyse Détaillée",
        "data_view_tab": "Vue des Données",
        "sales_over_time": "Ventes au Fil du Temps",
        "margin_analysis": "Analyse de la Marge",
        "top_selling_products": "Produits les Plus Vendus",
        "data_table": "Tableau de Données",
        "download_csv": "Télécharger les données en CSV",
        "show_summary": "Afficher les Statistiques Résumées",
    },
    "العربية": {
        "title": "لوحة مبيعات المنتجات",
        "filter": "تصفية البيانات",
        "average_price": "متوسط السعر",
        "average_margin": "متوسط الهامش",
        "select_sku": "اختر الرقم التسلسلي",
        "overview_tab": "نظرة عامة",
        "analysis_tab": "تحليل مفصل",
        "data_view_tab": "عرض البيانات",
        "sales_over_time": "المبيعات على مر الزمن",
        "margin_analysis": "تحليل الهامش",
        "top_selling_products": "المنتجات الأكثر مبيعا",
        "data_table": "جدول البيانات",
        "download_csv": "تحميل البيانات بصيغة CSV",
        "show_summary": "عرض الإحصائيات الخلاصة",
    },
    "ⵜⴰⵎⴰⵣⵉⵖⵜ": {
        "title": "ⵜⴰⴽⵡⵉⵍⵜ ⵏ ⵜⵓⴳⴳⴰⵔⴰ ⵏ ⵉⵎⴰⵍⵢⴰⵏ",
        "filter": "ⴰⵣⵔⵣⵉ ⵏ ⵜⵓⵙⴷⴰⵜ",
        "average_price": "ⵜⴰⵎⵓⵍⵜ ⵏ ⵜⴰⵙⴰⵖⵜ",
        "average_margin": "ⵜⴰⵎⵓⵍⵜ ⵏ ⵜⴰⴳⴻⵔⵎⵜ",
        "select_sku": "ⴰⴼⴰⵏ ⵏ ⵙⴽⵓ",
        "overview_tab": "ⵜⴰⵏⵎⵉⵔⵜ",
        "analysis_tab": "ⵜⴰⵏⵎⵉⵔⵜ ⵏ ⵜⴰⵎⴰⵡⴰⵙⵜ",
        "data_view_tab": "ⴰⵙⴰⵡⴰⵏ ⵏ ⵉⵎⴰⵍⵢⴰⵏ",
        "sales_over_time": "ⵜⴰⵎⵓⵍⵜ ⵏ ⵉⵎⴰⵍⵢⴰⵏ ⵏ ⵜⵓⴳⴳⴰⵔⴰ",
        "margin_analysis": "ⵜⴰⵏⵎⵉⵔⵜ ⵏ ⵜⴰⴳⴻⵔⵎⵜ",
        "top_selling_products": "ⵉⵎⴰⵍⵢⴰⵏ ⵏ ⵜⵓⴳⴳⴰⵔⴰ ⵏ ⵜⴰⵡⵓⵔⵉ",
        "data_table": "ⵜⴰⴽⵡⵉⵍⵜ ⵏ ⵉⵎⴰⵍⵢⴰⵏ",
        "download_csv": "ⴰⵣⴳⴰⵔⵡⴰ ⵏ ⵉⵎⴰⵍⵢⴰⵏ ⴳ ⴰⴱⴱⴰⵡⵏ ⵏ ⵙⵉⵙⵡⴰⵖⵜ",
        "show_summary": "ⴰⵙⵏⵓⵔⵓ ⵏ ⵜⵓⴳⴳⴰⵔⴰ ⵏ ⵉⵎⴰⵍⵢⴰⵏ",
    },
}



# Move the language selector to the bottom of the sidebar
with st.sidebar:
    st.markdown("<br><br><br>", unsafe_allow_html=True)  # Add space
    st.markdown(
        """
        <style>
            .selectbox-container {
                margin-top: 20px;
                padding: 10px;
                border-radius: 10px;
                background-color: #f1f1f1;
            }
            .selectbox-container label {
                font-weight: bold;
            }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown('<div class="selectbox-container">', unsafe_allow_html=True)
    language = st.selectbox(
        "Choose a language / Choisissez une langue / اختر لغة / ⴰⴱⴰⵢⵏ ⵜⵓⵜⵍⴰⵢⵜ",
        list(translations.keys())
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # Custom CSS to handle RTL languages like Arabic
    if language == "العربية":
        st.markdown(
            """
            <style>
                /* Add RTL support */
                .main, .sidebar .sidebar-content {
                    direction: rtl;
                }
                /* Other RTL-specific styles if needed */
            </style>
            """,
            unsafe_allow_html=True
        )

    # Get the translation dictionary for the selected language
    _ = translations[language]
# For Tifinagh, you'd add similar RTL support or other font-specific adjustments

# Custom CSS to inject into the Streamlit app
def custom_css():
    st.markdown(
        """
        <style>
            .main {
                font-family: 'Helvetica Neue', sans-serif;
            }
            h1 {
                color: #0b5ed7;
            }
            .stDataFrame, .stButton, .stSelectbox, .stExpander, .stMarkdown {
                font-size: 14px;
            }
            .stButton>button {
                width: 100%;
            }
            .card {
                position: relative;
                border: none;
                border-radius: 10px;
                padding: 20px;
                margin: 10px 0;
                background-color: #f9f9f9;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                transition: 0.3s;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            .card:hover {
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            }
            .card-title {
                font-size: 18px;
                color: #666;
                margin-bottom: 5px;
            }
            .card-value {
                font-size: 36px;
                font-weight: bold;
                color: #333;
            }
            .stFileUploader {
            border: 2px dashed #0b5ed7;
            border-radius: 5px;
            padding: 20px;
            transition: border .3s ease-in-out;
            text-align: center;  /* Center the text */
        }
        .stFileUploader:hover {
            border-color: #0a4ea2;
        }
        .stFileUploader label {
            color: #0b5ed7;
            font-weight: bold;
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Function to process uploaded data
def process_data(uploaded_file):
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
            # Check for required columns
            if 'SKU' not in data.columns:
                st.error("SKU column not found in the data.")
                return None
            return data
        except Exception as e:
            st.error(f"Error processing file: {e}")
            return None
    return None

# File uploader
uploaded_file = st.file_uploader("Drag and Drop or Click to Upload a CSV file", type="csv")
data = process_data(uploaded_file)

# Function to load data with caching to improve performance
@st.cache_data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        # Optional: Check if 'SKU' column exists
        if 'SKU' not in data.columns:
            st.error("SKU column not found in the data.")
            return pd.DataFrame()
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# Inject custom CSS
custom_css()

# Load your CSV data
data = load_data('data.csv')  # Update with your file path

# Check if data is loaded
if data.empty:
    st.stop()

# Replace the title
st.title(_["title"])

# Replace the sidebar header
st.sidebar.header(_["filter"])

# In the sidebar for filtering
if 'SKU' in data.columns:
    selected_sku = st.sidebar.multiselect(_["select_sku"], options=data['SKU'].unique())
    if selected_sku:
        data = data[data['SKU'].isin(selected_sku)]

# Using tabs for organizing content
tab1, tab2, tab3 = st.tabs([_["overview_tab"], _["analysis_tab"], _["data_view_tab"]])


with tab1:
    # First row of cards
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        st.markdown('<div class="card">'
                    '<div class="card-title">Average Price</div>'
                    f'<div class="card-value">${data["Price"].mean():,.2f}</div>'
                    '</div>', unsafe_allow_html=True)

    with row1_col2:
        st.markdown('<div class="card">'
                    '<div class="card-title">Average Margin</div>'
                    f'<div class="card-value">${data["Margin"].mean():,.2f}</div>'
                    '</div>', unsafe_allow_html=True)

    # Second row of cards
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        st.markdown('<div class="card">'
                    '<div class="card-title">Price-Quantity Correlation</div>'
                    f'<div class="card-value">{data["Price"].corr(data["Quantity"]):.2f}</div>'
                    '</div>', unsafe_allow_html=True)

    with row2_col2:
        st.markdown('<div class="card">'
                    '<div class="card-title">Unique Products</div>'
                    f'<div class="card-value">{data["SKU"].nunique()}</div>'
                    '</div>', unsafe_allow_html=True)
with tab2:
    # Dynamic rendering of graphs
    def render_graphs(data_frame):
        if 'Date' in data_frame.columns:
            st.subheader(_["sales_over_time"])
            fig, ax = plt.subplots()
            sns.lineplot(x='Date', y='Total', data=data_frame, ax=ax)
            st.pyplot(fig)

        if 'Margin' in data_frame.columns:
            st.subheader(_["margin_analysis"])
            fig, ax = plt.subplots()
            sns.histplot(data_frame['Margin'], bins=20, kde=True, ax=ax)
            st.pyplot(fig)

        if 'Name' in data_frame.columns and 'Quantity' in data_frame.columns:
            st.subheader(_["top_selling_products"])
            top_selling = data_frame.groupby('Name')['Quantity'].sum().sort_values(ascending=False).head(10)
            fig, ax = plt.subplots()
            top_selling.plot(kind='barh', ax=ax)
            st.pyplot(fig)

    # Call to render graphs
    render_graphs(data)

with tab3:
    st.subheader(_["data_table"])
    st.dataframe(data)  # Display the full data table here



# Download data as CSV
@st.cache_data
def convert_df_to_csv(download_df):
    return download_df.to_csv().encode('utf-8')


# Download data as CSV
csv = convert_df_to_csv(data)
st.download_button(label=_["download_csv"], data=csv, file_name='dl_data.csv', mime='text/csv')

# Display statistical summary
if st.checkbox(_["show_summary"]):
    st.write(data.describe())