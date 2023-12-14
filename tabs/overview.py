import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from components.cards import create_card, create_statistic_card
import locale


try:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_ALL, 'C')  # Fallback to the standard C locale



def format_all_currencies(value):
    """
    Formats and converts the value into Dirhams, Ryals, and Centimes,
    and presents them in a more readable format.
    """
    value_in_ryal = value * 20  # 1 Dirham = 20 Ryals
    value_in_centime = value * 100  # 1 Dirham = 100 Centimes

    formatted_dirham = locale.format_string("%.2f Dhs", value, grouping=True)
    # formatted_ryal = locale.format_string("%.2f Ryals", value_in_ryal, grouping=True)
    # formatted_centime = locale.format_string("%.2f Centimes", value_in_centime, grouping=True)

    # Separate the currencies by line breaks for better readability
    # return f"{formatted_dirham}<br>{formatted_ryal}<br>{formatted_centime}"
    return f"{formatted_dirham}<br>"



def show(data, translations):
    """
    Displays the overview tab in the Streamlit app.
    """
    # ... existing checks and data conversion ...

    st.markdown("## " + translations["overview_tab"])

    # Top Section - KPIs
    generate_kpi_cards(data, translations)

    # Middle Section - Detailed Analysis
    generate_detailed_analysis(data, translations)

    # Bottom Section - Sales Over Time Chart
    generate_sales_over_time_chart(data, translations)



def generate_kpi_cards(data, translations):
    """
    Generate KPI cards for displaying key metrics.
    """
    # Calculate KPI values
    average_price = data['Coût'].mean()
    average_margin = data['Marge'].mean()
    total_sales = data['Total'].sum()
    total_profit = (data['Total'] * (data['Marge'] / 100)).sum()
    total_items_sold = data['Quantité'].sum()

    # Create columns for each card
    col1, col2, col3 = st.columns(3)

    with col1:
        create_statistic_card(translations["average_price"], f"{format_all_currencies(average_price)}", style="primary")
        create_statistic_card(translations["total_profit"], f"{format_all_currencies(total_profit)}", style="warning")

    with col2:
        create_statistic_card(translations["average_margin"], f"{average_margin:.2f}%", style="success")
        create_statistic_card(translations["total_items_sold"], f"{total_items_sold}", style="danger")

    with col3:
        create_statistic_card(translations["total_sales"], f"{format_all_currencies(total_sales)}", style="info")


def generate_detailed_analysis(data, translations):
    generate_unit_price_distribution_chart(data, translations)
    generate_profit_margin_chart(data, translations)

def generate_unit_price_distribution_chart(data, translations):
    st.markdown("### " + translations["unit_price_distribution"])
    fig, ax = plt.subplots()
    sns.histplot(data['Coût'], bins=20, kde=True, ax=ax)
    ax.set_title(translations["unit_price_distribution"])
    st.pyplot(fig)

def generate_profit_margin_chart(data, translations):
    st.markdown("### " + translations["profit_margin_by_sku"])
    fig, ax = plt.subplots()
    sns.barplot(x='Produit', y='Marge', data=data, ax=ax)
    ax.set_title(translations["profit_margin_by_sku"])
    plt.xticks(rotation=45)
    st.pyplot(fig)

def generate_sales_over_time_chart(data, translations):
    if data.empty:
        st.warning("No data to display. Please adjust the filters.")
        return
        
    # Set a reasonable figure size
    fig, ax1 = plt.subplots(figsize=(10, 6))  # Adjust as needed

    # Plot the total sales bars
    barplot = sns.barplot(x='Produit', y='Total', data=data, ax=ax1, color='blue', label='Total Sales')

    # Create the secondary y-axis for the total quantity sold
    ax2 = ax1.twinx()
    lineplot_quantity = sns.lineplot(x='Produit', y='Quantité', data=data, ax=ax2, color='green', marker='o', label='Total Quantity Sold')
    lineplot_profit = sns.lineplot(x='Produit', y='Profit', data=data, ax=ax2, color='red', marker='x', label='Total Profit Made')

    # Annotate bars with unitary price
    for index, row in data.iterrows():
        unit_price = row['Coût']  # Assuming 'Price' is the unitary price column in your dataset
        ax1.text(
            x=index, 
            y=row['Total'], 
            s=f"{unit_price:.2f}",  # Format to 2 decimal places
            color='black',
            ha="center",
            va='bottom'  # To position the text at the top of the bar
        )

    # Set axis labels and legend
    ax1.set_xlabel('Produit')
    ax1.set_ylabel('Total Sales (Dhs)', color='blue')
    ax2.set_ylabel('Total Quantity Sold / Total Profit Made', color='green')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax2.tick_params(axis='y', labelcolor='green')

    # Set the legend
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax2.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

    plt.xticks(rotation=45)
    plt.tight_layout()
    # Call tight_layout to optimize the layout
    plt.tight_layout()
    st.pyplot(fig)



# ARCHIVED CODE
# def generate_stats_cards(data, translations):
#     """
#     Generate statistic cards for displaying average price and average margin.
#     """
#     # Convert 'Margin' to numeric format after stripping the '%' character
#     data['Marge'] = data['Marge'].apply(convert_percentage_to_float)

#     average_price = data['Coût'].mean()
#     average_margin = data['Marge'].mean()
#     total_sales = data['Total'].sum()

#     # Calculating total profit
#     total_profit = data['Profit'].sum()
#     total_items_sold = data['Quantité'].sum()

#     col1, col2 = st.columns(2)

#     with col1:
#         create_statistic_card(translations["average_price"], format_all_currencies(average_price), style="primary")
#         create_statistic_card(translations["average_margin"], f"{average_margin:.2f}%", style="success")
#         create_statistic_card(translations["total_profit"], format_all_currencies(total_profit), style="warning")

#     with col2:
#         create_statistic_card(translations["total_sales"], format_all_currencies(total_sales), style="info")
#         create_statistic_card(translations["total_items_sold"], f"{total_items_sold}", style="danger")
