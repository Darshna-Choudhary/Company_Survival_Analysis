import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, format_currency


def show_page():
    df = load_data()

    active_df = df[df["CompanyStatus"]=="Active"]

    st.title("📈 Survival Analysis")

    st.caption(
        "Identify which companies are more likely to survive based on industry, category, company class and age."
    )

    st.divider()

    industry = (
        df.groupby("CompanyIndustrialClassification")["CompanyStatus"]
        .apply(lambda x:(x=="Active").mean()*100)
        .reset_index(name="Active %")
        .sort_values("Active %",ascending=False)
        .head(15)
    )

    fig = px.bar(
        industry,
        x="Active %",
        y="CompanyIndustrialClassification",
        orientation="h",
        color="Active %",
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        title="Industry Survival Rate",
        yaxis_title="Industry",
        xaxis_title="Active Companies (%)",
        height=550,
        coloraxis_showscale=False
    )

    st.plotly_chart(fig,use_container_width=True)

    left,right = st.columns(2)

    with left:
        category = (
            df.groupby("CompanyCategory")["CompanyStatus"]
            .apply(lambda x:(x=="Active").mean()*100)
            .reset_index(name="Active %")
            .sort_values("Active %",ascending=False)
        )

        fig = px.bar(
            category,
            x="CompanyCategory",
            y="Active %",
            color="Active %",
            color_continuous_scale="Greens"
        )

        fig.update_layout(
            title="Company Category Survival",
            xaxis_title="",
            coloraxis_showscale=False,
            height=420
        )

        st.plotly_chart(fig,use_container_width=True)

    with right:
        company_class = (
            df.groupby("CompanyClass")["CompanyStatus"]
            .apply(lambda x:(x=="Active").mean()*100)
            .reset_index(name="Active %")
            .sort_values("Active %",ascending=False)
        )

        fig = px.bar(
            company_class,
            x="CompanyClass",
            y="Active %",
            color="Active %",
            color_continuous_scale="Oranges"
        )

        fig.update_layout(
            title="Company Class Survival",
            xaxis_title="",
            coloraxis_showscale=False,
            height=420
        )

        st.plotly_chart(fig,use_container_width=True)

    registration = df[
        df["Company_Age"].between(0, 100)]
    fig = px.box(
        registration,
        x="CompanyStatus",
        y="Company_Age",
        color="CompanyStatus",
        color_discrete_map={
            "Active":"#16a34a",
            "Strike Off":"#dc2626",
            "Dissolved":"#6b7280",
            "Liquidation":"#9333ea"
        }
    )

    fig.update_layout(
        title="Company Age Distribution",
        xaxis_title="Status",
        yaxis_title="Company Age",
        height=500
    )

    st.plotly_chart(fig,use_container_width=True)

    st.subheader("Characteristics of Active Companies")
    c1,c2,c3,c4 = st.columns(4)
    c1.metric(
        "Average Age",
        f"{active_df['Company_Age'].mean():.1f} Years"
    )

    c2.metric(
        "Average Paid-up Capital",
        format_currency(active_df['PaidupCapital'].mean())
    )

    c3.metric(
        "Most Common Industry",
        active_df["CompanyIndustrialClassification"].mode()[0]
    )

    c4.metric(
        "Most Common Category",
        active_df["CompanyCategory"].mode()[0]
    )

    st.info(f"""

    ### 📌 Key Findings

    • Companies in **{industry.iloc[0]['CompanyIndustrialClassification']}** have the highest survival rate (**{industry.iloc[0]['Active %']:.1f}%**).

    • **{category.iloc[0]['CompanyCategory']}** companies survive more frequently than other categories.

    • The most successful company class is **{company_class.iloc[0]['CompanyClass']}**.

    • Active companies are on average **{active_df['Company_Age'].mean():.1f} years** old.

    • The dominant surviving industry is **{active_df['CompanyIndustrialClassification'].mode()[0]}**.

    """)