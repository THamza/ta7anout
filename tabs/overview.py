import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from components.cards import create_card, create_statistic_card
import locale


try:
    locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
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
    
    return f"{formatted_dirham}<br>"



def show(data, translations):
    """
    Displays the overview tab in the Streamlit app.
    """
    # ... existing checks and data conversion ...

    # Top Section - KPIs
    generate_kpi_cards(data, translations)

    # Top products
    generate_top_products_cards(data, translations)

    show_profitability_analysis(data, translations)

    # Middle Section - Detailed Analysis
    generate_detailed_analysis(data, translations)

    # Bottom Section - Sales Over Time Chart
    generate_sales_over_time_chart(data, translations)

def plot_profitability_chart(data, selected_skus):
    """
    Plots a bar chart showing the profitability of the selected top products.
    """
    # Filter data to include only the selected products
    filtered_data = data[data['SKU'].isin(selected_skus)]

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    barplot = sns.barplot(
        x='SKU', 
        y='Profit', 
        data=filtered_data,
        order=selected_skus  # This ensures the bars follow the selected order
    )

    # Add labels and title
    plt.title('Profitability of Top Products')
    plt.xlabel('Product SKU')
    plt.ylabel('Total Profit')
    
    # Rotate x-axis labels
    plt.xticks(rotation=45)  # Rotate labels to make them readable

    # Show the plot
    st.pyplot(barplot.figure)

def show_profitability_analysis(data, translations):
    """
    Shows an interactive profitability analysis section.
    """
    st.markdown("## " + translations["profitability_analysis"])

    # Get all unique SKUs and the top 10 profitable SKUs
    all_skus = data['SKU'].unique().tolist()
    top_skus = data.groupby('SKU')['Profit'].sum().sort_values(ascending=False).head(10).index.tolist()

    # Multiselect dropdown that includes all products but defaults to the top 10
    selected_skus = st.multiselect(
        label=translations["select_products_to_view"], 
        options=all_skus, 
        default=top_skus  # Set the top 10 SKUs as the default selection
    )

    # If products are selected, plot the chart
    if selected_skus:
        plot_profitability_chart(data, selected_skus)
    else:
        st.warning(translations["no_product_selected_warning"])

# Assuming you have a function to convert the raw metrics into formatted strings
def format_metric(value, metric_type):
    try:
        # Convert value to float
        numeric_value = float(value)
        
        if metric_type == "currency":
            formatted = f"{numeric_value:.2f}"
        elif metric_type == "quantity":
            formatted = f"{numeric_value:.0f}"
        else:
            formatted = f"{numeric_value}"
        
        # Add thousand separators
        parts = formatted.split(".")
        parts[0] = "{:,}".format(int(float(parts[0]))).replace(",", " ")
        formatted = ".".join(parts)
        
        if metric_type == "currency":
            return formatted + " Dhs"
        return formatted
    except ValueError:
        # If conversion to float fails, return the original value as a string
        return str(value)

def create_multi_metric_card(rank, sku, metrics, translations):
    # Define symbols for each rank
    rank_symbols = {
        1: "🥇",
        2: "🥈",
        3: "🥉"
    }
    rank_symbol = rank_symbols.get(rank, "")

    with st.container():
        # Use a card-like layout with shadows for a subtle 3D effect
        st.markdown(f"""
            <style>
            .metric-container {{
                border-radius: 10px;
                background-color: #f8f9fa;
                box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
                transition: 0.3s;
                padding: 15px;
                margin-bottom: 10px;
            }}
            .metric-container:hover {{
                box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
            }}
            .metric-title {{
                font-size: 1.25rem;
                font-weight: 500;
                margin: 0;
                padding: 0;
                color: #333;
            }}
            .metric-value {{
                font-size: 2rem;
                font-weight: bold;
                margin: 0;
                padding: 0;
                color: #1a73e8;  /* Change color to suit your branding */
            }}
            .metric-label {{
                font-size: 1rem;
                color: #6c757d;
            }}
            </style>
            <div class="metric-container">
                <p class="metric-title"><span class="rank-symbol">{rank_symbol}</span>{sku}</p>
                <div class="row">
                    <div class="col">
                        <p class="metric-value">{format_metric(metrics['Quantity'], 'quantity')}</p>
                        <p class="metric-label">{translations["total_items_sold"]}</p>
                    </div>
                    <div class="col">
                        <p class="metric-value">{format_metric(metrics['Total'], 'currency')}</p>
                        <p class="metric-label">{translations["total_sales"]}</p>
                    </div>
                    <div class="col">
                        <p class="metric-value">{format_metric(metrics['Profit'], 'currency')}</p>
                        <p class="metric-label">{translations["total_profit"]}</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

 
def generate_top_products_cards(data, translations):
    st.markdown("## " + translations["top_products"])
    
    # Add a dropdown menu for sorting criteria
    sort_criteria = st.selectbox(
        translations["sort_by"],
        [translations["total_items_sold"], translations["total_profit"], translations["total_sales"]],
        key="top_products_sort"
    )
    
    # Map the selected option to the corresponding column name
    sort_column = {
        translations["total_items_sold"]: "Quantity",
        translations["total_profit"]: "Profit",
        translations["total_sales"]: "Total"
    }[sort_criteria]
    
    # Calculate top 3 products based on the selected criteria
    top_products_data = data.groupby('SKU').agg({
        'Quantity': lambda x: pd.to_numeric(x, errors='coerce').sum(),
        'Total': lambda x: pd.to_numeric(x, errors='coerce').sum(),
        'Profit': lambda x: pd.to_numeric(x, errors='coerce').sum(),
    }).sort_values(by=sort_column, ascending=False).head(3)

    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]
    
    for i, (sku, metrics) in enumerate(top_products_data.iterrows(), start=1):
        with columns[i-1]:
            create_multi_metric_card(i, sku, metrics, translations)

def generate_kpi_cards(data, translations):
    """
    Generate KPI cards for displaying key metrics.
    """ 

    st.markdown("## " + translations["overview_tab"])

    # Calculate KPI values
    average_price = data['Price'].mean()
    average_margin = data['Margin'].mean()
    total_sales = data['Total'].sum()
    total_profit = data['Profit'].sum()
    total_items_sold = pd.to_numeric(data['Quantity'], errors='coerce').fillna(0).astype(int).sum()

   
    # Create columns for each card
    col1, col2, col3 = st.columns(3)

    with col1:
        create_statistic_card(
            translations["total_profit"], 
            f"{total_profit:,.2f}".replace(',', ' ') + " Dhs", 
            style="warning"
        )

    with col2:
        create_statistic_card(
            translations["total_sales"], 
            f"{total_sales:,.2f}".replace(',', ' ') + " Dhs", 
            style="info"
        )

    with col3:
        create_statistic_card(
            translations["total_items_sold"], 
            f"{total_items_sold:,}".replace(',', ' '), 
            style="danger"
        )



def generate_detailed_analysis(data, translations):
    generate_unit_price_distribution_chart(data, translations)
    generate_profit_margin_chart(data, translations)

def generate_unit_price_distribution_chart(data, translations):
    st.markdown("### " + translations["unit_price_distribution"])
    fig, ax = plt.subplots()
    sns.histplot(data['Price'], bins=20, kde=True, ax=ax)
    ax.set_title(translations["unit_price_distribution"])
    st.pyplot(fig)

def generate_profit_margin_chart(data, translations):
    st.markdown("### " + translations["profit_margin_by_sku"])
    fig, ax = plt.subplots()
    sns.barplot(x='SKU', y='Margin', data=data, ax=ax)
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
    barplot = sns.barplot(x='SKU', y='Total', data=data, ax=ax1, color='blue', label='Total Sales')

    # Create the secondary y-axis for the total quantity sold
    ax2 = ax1.twinx()
    lineplot_quantity = sns.lineplot(x='SKU', y='Quantity', data=data, ax=ax2, color='green', marker='o', label='Total Quantity Sold')
    lineplot_profit = sns.lineplot(x='SKU', y='Profit', data=data, ax=ax2, color='red', marker='x', label='Total Profit Made')

    # Annotate bars with unitary price
    for index, row in data.iterrows():
        unit_price = row['Price']  # Assuming 'Price' is the unitary price column in your dataset
        ax1.text(
            x=index, 
            y=row['Total'], 
            s=f"{unit_price:.2f}",  # Format to 2 decimal places
            color='black',
            ha="center",
            va='bottom'  # To position the text at the top of the bar
        )

    # Set axis labels and legend
    ax1.set_xlabel('SKU')
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
#     data['Margin'] = data['Margin'].apply(convert_percentage_to_float)

#     average_price = data['Price'].mean()
#     average_margin = data['Margin'].mean()
#     total_sales = data['Total'].sum()

#     # Calculating total profit
#     total_profit = data['Profit'].sum()
#     total_items_sold = data['Quantity'].sum()

#     col1, col2 = st.columns(2)

#     with col1:
#         create_statistic_card(translations["average_price"], format_all_currencies(average_price), style="primary")
#         create_statistic_card(translations["average_margin"], f"{average_margin:.2f}%", style="success")
#         create_statistic_card(translations["total_profit"], format_all_currencies(total_profit), style="warning")

#     with col2:
#         create_statistic_card(translations["total_sales"], format_all_currencies(total_sales), style="info")
#         create_statistic_card(translations["total_items_sold"], f"{total_items_sold}", style="danger")
