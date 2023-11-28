import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd

def line_chart(data, x, y, title=None, xlabel=None, ylabel=None):
    """
    Renders a line chart in the Streamlit app.

    Parameters:
    - data: DataFrame with the data for the chart.
    - x: The column name to be used for the x-axis.
    - y: The column name to be used for the y-axis.
    - title: Title of the chart (optional).
    - xlabel: Label for the x-axis (optional).
    - ylabel: Label for the y-axis (optional).
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    st.pyplot(plt)

def bar_chart(data, x, y, title=None, xlabel=None, ylabel=None):
    """
    Renders a bar chart in the Streamlit app.

    Parameters:
    - data: DataFrame with the data for the chart.
    - x: The column name to be used for the x-axis.
    - y: The column name to be used for the y-axis.
    - title: Title of the chart (optional).
    - xlabel: Label for the x-axis (optional).
    - ylabel: Label for the y-axis (optional).
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    st.pyplot(plt)

def scatter_plot(data, x, y, hue=None, title=None, xlabel=None, ylabel=None):
    """
    Renders a scatter plot in the Streamlit app.

    Parameters:
    - data: DataFrame with the data for the chart.
    - x: The column name to be used for the x-axis.
    - y: The column name to be used for the y-axis.
    - hue: Variable in `data` that determines the color of plot elements.
    - title: Title of the chart (optional).
    - xlabel: Label for the x-axis (optional).
    - ylabel: Label for the y-axis (optional).
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=x, y=y, hue=hue)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    st.pyplot(plt)

def histogram(data, column, bins=20, title=None, xlabel=None):
    """
    Renders a histogram in the Streamlit app.

    Parameters:
    - data: DataFrame with the data for the chart.
    - column: The column name to be used for the histogram.
    - bins: Number of bins for the histogram.
    - title: Title of the histogram (optional).
    - xlabel: Label for the x-axis (optional).
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.tight_layout()
    st.pyplot(plt)

def convert_df_to_csv(dataframe):
    """
    Converts a DataFrame to a CSV string.

    Parameters:
    - dataframe: The DataFrame to convert.

    Returns:
    - A CSV string.
    """
    return dataframe.to_csv(index=False).encode('utf-8')

# Example usage of the functions in an app
def example_usage():
    # Example DataFrame
    df = pd.DataFrame({
        'Date': pd.date_range(start='2021-01-01', periods=100, freq='D'),
        'Sales': pd.np.random.randint(100, 500, size=100),
        'Profit': pd.np.random.randint(10, 50, size=100)
    })

    # Using the functions to create charts
    line_chart(df, 'Date', 'Sales', title='Sales Over Time', xlabel='Date', ylabel='Sales')
    bar_chart(df, 'Date', 'Profit', title='Profit by Date', xlabel='Date', ylabel='Profit')
    scatter_plot(df, 'Sales', 'Profit', title='Sales vs. Profit', xlabel='Sales', ylabel='Profit')
    histogram(df, 'Sales', bins=10, title='Sales Distribution', xlabel='Sales')

# Uncomment the line below to see the example usage in your app.
# example_usage()
