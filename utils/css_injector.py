import streamlit as st
import os

def add_custom_css(file_path='static/styles.css'):
    """
    Reads a CSS file and injects it into the Streamlit app.

    Parameters:
    - file_path: The path to the CSS file.
    """
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Example usage
# Call this function in your main app.py to apply the custom styles
# add_custom_css()
