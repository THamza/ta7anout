import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def show(data, translations):
    """
    Displays the analysis tab in the Streamlit app.

    Parameters:
    - data: The processed DataFrame that contains the data to display.
    - translations: A dictionary containing translation mappings for text.
    """

    st.markdown("## " + translations["analysis_tab"])

    # Conditional rendering of analysis components based on the data
    if 'Margin' in data.columns and 'Quantity' in data.columns:
        # Display margin analysis
        display_margin_analysis(data, translations)
        
        # Display price-quantity correlation
        display_price_quantity_correlation(data, translations)
        
        # Display top selling products analysis
        display_top_selling_products(data, translations)
    else:
        st.error(translations["data_error"])


def display_margin_analysis(data, translations):
    """
    Display margin analysis as a histogram.
    """
    st.markdown("### " + translations["margin_analysis"])
    fig, ax = plt.subplots()
    sns.histplot(data['Margin'], bins=20, kde=True, ax=ax)
    st.pyplot(fig)


def display_price_quantity_correlation(data, translations):
    """
    Display a scatter plot showing the correlation between price and quantity.
    """
    st.markdown("### " + translations["correlation_analysis"])
    fig, ax = plt.subplots()
    sns.scatterplot(x='Price', y='Quantity', data=data, ax=ax)
    st.pyplot(fig)


def display_top_selling_products(data, translations):
    """
    Display a bar chart of the top-selling products.
    """
    st.markdown("### " + translations["top_selling_products"])
    top_selling = data.groupby('SKU')['Quantity'].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots()
    sns.barplot(x=top_selling.values, y=top_selling.index, palette="viridis", ax=ax)
    ax.set_xlabel(translations["quantity"])
    ax.set_ylabel(translations["sku"])
    st.pyplot(fig)
