# Product Sales Dashboard Application

## Overview

This Python and Streamlit-based application offers a dynamic and interactive dashboard for product sales analysis. It supports multiple languages including English, Français, العربية, and ⵜⴰⵎⴰⵣⵉⵖⵜ, enabling a wide range of users to interact with their sales data effectively. Key features include data upload, filtering, visualization, and statistical summaries.

## Features

- **Multilingual Support**: Interface available in multiple languages.
- **Data Filtering**: Users can filter sales data based on SKU.
- **Interactive Graphs**: Sales over time and margin analysis visualizations.
- **Data Upload**: Capability to upload sales data via CSV files.
- **Data Visualization**: Data can be viewed and interacted with in a tabular format.
- **Statistical Summaries**: Quick view of summary statistics of the data.
- **Custom Styling**: Enhanced user experience with custom CSS.

## Installation

1. Install Python on your system.
2. Install required libraries: `streamlit`, `pandas`, `matplotlib`, and `seaborn`.
3. Download and extract the application code.

## Usage

1. Launch the application with Streamlit: `streamlit run app.py`.
2. Use the sidebar to upload your CSV file and choose the desired language.
3. Navigate through different tabs to interact with various data visualizations and analyses.

## Expected Input File Format

### File Type

- **Format**: CSV (Comma-Separated Values)
- **Upload Method**: Drag and drop or click to upload in the Streamlit interface.

### Required Columns

Your CSV file must include these columns:

- **SKU**: Unique identifier for each product.
- **Price**: Sale price of the product.
- **Quantity**: Number of units sold.
- **Date**: Date of the sale.
- **Total**: Total sales amount (calculated as Price \* Quantity).
- **Margin**: Profit margin per product.

### Formatting Tips

- First row should contain column headers.
- Ensure data consistency in each column.
- Avoid special characters or extra spaces in headers.
- Dates should be in a consistent format.

### Sample CSV Format

SKU,Price,Quantity,Date,Total,Margin
1001,20,5,2023-01-01,100,10
1002,15,8,2023-01-02,120,12

## Customization

- **Language Selection**: Modify the `translations` dictionary to add or edit interface translations.
- **Graph Styles**: Adjust the `render_graphs` function to alter graph styles.

## Troubleshooting

- **Data Upload Issues**: Check CSV format, especially the 'SKU' column.
- **Graph Rendering Problems**: Ensure required columns like 'Date', 'Total', and 'Margin' are present.

## Support

For issues or feature requests, please open an issue on the project's GitHub page.

## Contributing

Contributions are welcome. Adhere to coding standards and submit a pull request for review.

---

Keep your Python packages updated for compatibility. Enjoy your data analysis journey!
