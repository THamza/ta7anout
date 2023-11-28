import streamlit as st

def create_card(title, content, style="info"):
    """
    Creates a stylized card component for the Streamlit dashboard.

    Parameters:
    - title: The title of the card.
    - content: The main content to display on the card.
    - style: Style of the card (e.g., 'info', 'success', 'warning', 'danger').
    """

    card_color = {
        "info": "#117a8b",
        "success": "#28a745",
        "warning": "#ffc107",
        "danger": "#dc3545"
    }

    card_html = f"""
        <div style="
            border-left: 5px solid {card_color.get(style, '#117a8b')};
            background-color: #f4f4f4;
            padding: 15px 20px;
            border-radius: 5px;
            margin: 10px 0px;
            box-shadow: 2px 2px 2px rgba(0,0,0,0.1);">
            <h4 style="color: {card_color.get(style, '#117a8b')}; margin:0;">{title}</h4>
            <p style="margin:5px 0px;">{content}</p>
        </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

def create_statistic_card(label, value, style="primary"):
    """
    Creates a statistic card to display key metrics.

    Parameters:
    - label: Label of the statistic.
    - value: Value of the statistic.
    - style: Style of the card (e.g., 'primary', 'secondary').
    """

    bg_color = "#f8f9fa" if style == "secondary" else "#ffffff"
    text_color = "#6c757d" if style == "secondary" else "#000000"

    card_html = f"""
        <div style="
            background-color: {bg_color};
            padding: 10px 15px;
            border-radius: 5px;
            border: 1px solid #ddd;
            text-align: center;
            margin: 10px 0px;
            box-shadow: 1px 1px 3px rgba(0,0,0,0.1);">
            <h3 style="color: {text_color}; margin:0;">{value}</h3>
            <p style="color: {text_color}; margin:5px 0px;">{label}</p>
        </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

# Example usage of the card components
def example_usage():
    create_card("Notice", "This is an informational card.", style="info")
    create_card("Warning", "Please check your input.", style="warning")
    create_statistic_card("Total Sales", "$1,234", style="primary")
    create_statistic_card("Active Users", "456", style="secondary")

# Uncomment the line below to test the example usage in your app.
# example_usage()
