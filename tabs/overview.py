import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from components.cards import create_card, create_statistic_card

def show(data, translations):
    """
    Displays the overview tab in the Streamlit app.

    Parameters:
    - data: The processed DataFrame that contains the data to display.
    - translations: A dictionary containing translation mappings for text.
    """

    # Ensure that the necessary columns are present
    required_columns = ['SKU', 'Price', 'Margin', 'Quantity', 'Total']
    if not all(column in data.columns for column in required_columns):
        st.error(translations['data_error'])
        return

    # Convert 'Price', 'Margin', and 'Total' columns to numeric format
    data['Price'] = pd.to_numeric(data['Price'], errors='coerce')
    data['Margin'] = pd.to_numeric(data['Margin'], errors='coerce')
    data['Total'] = pd.to_numeric(data['Total'], errors='coerce')

    # Handle NaN values that arise from conversion (optional, based on your data handling strategy)
    data.fillna(0, inplace=True)

    st.markdown("## " + translations["overview_tab"])

    # Generate a statistics card for average price and margin
    generate_stats_cards(data, translations)

    # Generate sales over time line chart
    generate_sales_over_time_chart(data, translations)

    # Display any other relevant information or statistics

def generate_stats_cards(data, translations):
    """
    Generate statistic cards for displaying average price and average margin.
    """
    average_price = data['Price'].mean()
    average_margin = data['Margin'].mean()
    total_sales = data['Total'].sum()

    col1, col2 = st.columns(2)

    with col1:
        create_statistic_card(translations["average_price"], f"{average_price:.2f} Dhs", style="primary")
        create_statistic_card(translations["average_margin"], f"{average_margin:.2f}%", style="success")

    with col2:
        create_statistic_card(translations["total_sales"], f"{total_sales:.2f} Dhs", style="info")

def generate_sales_over_time_chart(data, translations):
    st.markdown("### " + translations["sales_over_sku"])
    fig, ax = plt.subplots()
    sns.barplot(x=data['SKU'], y=data['Total'], ax=ax)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
