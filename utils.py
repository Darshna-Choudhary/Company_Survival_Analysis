import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_company_data.csv")
    return df

def format_currency(value):
    if value >= 1e7:
        return f"₹{value/1e7:.1f} Cr"
    elif value >= 1e6:
        return f"₹{value/1e6:.1f} M"
    elif value >= 1e3:
        return f"₹{value/1e3:.1f} K"
    else:
        return f"₹{value:,.0f}"