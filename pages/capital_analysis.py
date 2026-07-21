import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data

from scipy.stats import chi2_contingency

def show_page():
    df = load_data()
    df["is_active"] = (df["CompanyStatus"] == "Active").astype(int)

    st.title("💰 Capital Analysis")
    st.caption(
    "Analyze whether paid-up capital influences the survival of Indian companies."
    )
    st.divider()

    fig = px.box(
    df,
    x="CompanyStatus",
    y="PaidupCapital",
    color="CompanyStatus",
    log_y=True,
    points=False
    )
    fig.update_layout(
    title="Paid-up Capital vs Company Status",
    xaxis_title="Company Status",
    yaxis_title="Paid-up Capital (Log Scale)",
    height=500
    )
    st.plotly_chart(fig, use_container_width=True)

    bins = [0,1e5,1e6,1e7,1e8,df["PaidupCapital"].max()]
    labels = ["<1 Lakh", "1L - 10L", "10L - 1Cr", "1Cr - 10Cr", ">10Cr"]
    df["capital_bucket"] = pd.cut(
    df["PaidupCapital"],
    bins=bins,
    labels=labels,
    include_lowest=True
    )
    bucket = (
    df.groupby("capital_bucket")["CompanyStatus"]
    .apply(lambda x: (x=="Active").mean()*100)
    .reset_index(name="Active %")
    )
    left,right = st.columns(2)

    with left:
        fig = px.bar(
            bucket,
            x="capital_bucket",
            y="Active %",
            color="Active %",
            color_continuous_scale="Blues"
        )
        fig.update_layout(
        title="Capital Buckets vs Active Companies",
        xaxis_title="Paid-up Capital",
        yaxis_title="Active %",
        coloraxis_showscale=False,
        height=430
        )
    st.plotly_chart(fig,use_container_width=True)

    with right:
        fig = px.violin(
            df,
            x="CompanyStatus",
            y="PaidupCapital",
            color="CompanyStatus",
            box=True,
            log_y=True
        )
        fig.update_layout(
        title="Capital Distribution by Status",
        yaxis_title="Paid-up Capital (Log Scale)",
        height=430)

    st.plotly_chart(fig,use_container_width=True)

    st.info(f"""
    ### 📌 Key Findings
    • Companies with higher paid-up capital generally show a higher survival rate.
    • Survival increases noticeably after the **1 Crore** capital mark.
    """)