import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from components.cards import create_card, create_statistic_card
import locale

# Set the locale to the desired format
locale.setlocale(locale.LC_ALL, 'en_US')

def convert_percentage_to_float(percentage_str):
    """
    Convert a percentage string to a float.
    Example: '16%' becomes 16.0
    """
    if isinstance(percentage_str, str):
        return float(percentage_str.strip('%'))
    return percentage_str

def format_all_currencies(value):
    """
    Formats and converts the value into Dirhams, Ryals, and Centimes,
    and presents them in a more readable format.
    """
    value_in_ryal = value * 20  # 1 Dirham = 20 Ryals
    value_in_centime = value * 100  # 1 Dirham = 100 Centimes

    formatted_dirham = locale.format_string("%.2f Dhs", value, grouping=True)
    formatted_ryal = locale.format_string("%.2f Ryals", value_in_ryal, grouping=True)
    formatted_centime = locale.format_string("%.2f Centimes", value_in_centime, grouping=True)

    # Separate the currencies by line breaks for better readability
    return f"{formatted_dirham}<br>{formatted_ryal}<br>{formatted_centime}"



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
    # Convert 'Margin' to numeric format after stripping the '%' character
    data['Margin'] = data['Margin'].apply(convert_percentage_to_float)

    average_price = data['Price'].mean()
    average_margin = data['Margin'].mean()
    total_sales = data['Total'].sum()

    # Calculating total profit
    total_profit = (data['Total'] * (data['Margin'] / 100)).sum()
    total_items_sold = data['Quantity'].sum()

    col1, col2 = st.columns(2)

    with col1:
        create_statistic_card(translations["average_price"], format_all_currencies(average_price), style="primary")
        create_statistic_card(translations["average_margin"], f"{average_margin:.2f}%", style="success")
        create_statistic_card(translations["total_profit"], format_all_currencies(total_profit), style="warning")

    with col2:
        create_statistic_card(translations["total_sales"], format_all_currencies(total_sales), style="info")
        create_statistic_card(translations["total_items_sold"], f"{total_items_sold}", style="danger")



def generate_sales_over_time_chart(data, translations):
    st.markdown("### " + translations["sales_over_sku"])
    fig, ax = plt.subplots()
    sns.barplot(x=data['SKU'], y=data['Total'], ax=ax)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
