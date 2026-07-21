import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, format_currency

# ---------------------------------------------------
# PAGE
# ---------------------------------------------------    

def show_page():

    df = load_data()

    # -----------------------------
    # KPIs
    # -----------------------------

    total = len(df)
    active = df["CompanyStatus"].str.lower().eq("active").sum()
    inactive = total - active
    active_pct = active / total * 100
    inactive_pct = inactive / total * 100
    avg_age = df["Company_Age"].mean()
    avg_capital = df["PaidupCapital"].mean()

    # -----------------------------
    # KPI Cards
    # -----------------------------

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric(
        "🏢 Total Companies",
        f"{total:,}"
    )

    c2.metric(
        "✅ Active %",
        f"{active_pct:.1f}%"
    )

    c3.metric(
        "❌ Inactive %",
        f"{inactive_pct:.1f}%"
    )

    c4.metric(
        "⏳ Avg Company Age",
        f"{avg_age:.1f} Years"
    )

    c5.metric(
        "💰 Avg Paid-up Capital",
        format_currency(avg_capital)
    )

    st.markdown("---")

    # -----------------------------
    # Charts
    # -----------------------------

    col1,col2 = st.columns((1,2))

    # -------------------------------------
    # Donut Chart
    # -------------------------------------

    with col1:
        status_counts = (
            df["CompanyStatus"]
            .value_counts()
            .reset_index()
        )
        status_counts.columns=["Status","Companies"]
        fig = px.pie(
            status_counts,
            names="Status",
            values="Companies",
            hole=.65,
            color="Status",
            color_discrete_map={
                "Active":"#16a34a",
                "Strike Off":"#ef4444",
                "Amalgamated":"#f59e0b",
                "Liquidation":"#8b5cf6",
                "Dissolved":"#6b7280"
            }
        )

        fig.update_layout(
            title="Company Status Distribution",
            title_x=0.25,
            legend_title="Status",
            height=450
        )

        fig.update_traces(
            textposition="inside",
            textinfo="percent"
        )

        st.plotly_chart(fig,use_container_width=True)

    # -------------------------------------
    # Registration Trend
    # -------------------------------------

    with col2:
        registration = df[
        df["Registration_Year"].between(1980, 2030)]
        yearly = (
            registration
            .groupby("Registration_Year")
            .size()
            .reset_index(name="Companies")
        )

        fig = px.line(
            yearly,
            x="Registration_Year",
            y="Companies",
            markers=True
        )

        fig.update_layout(
            title="Company Registration Trend",
            xaxis_title="Registration Year",
            yaxis_title="Companies Registered",
            hovermode="x unified",
            height=450
        )

        fig.update_traces(
            line=dict(width=4),
            marker=dict(size=7)
        )

        st.plotly_chart(fig,use_container_width=True)
    
    st.markdown("### 📌 Key Insights")
    st.info(f"""
        • **{active_pct:.1f}%** of companies are currently active.
        
        • Average company age is **{avg_age:.1f} years**.
        
        • The dataset contains **{total:,}** registered companies.
        
        • Average paid-up capital is **{format_currency(avg_capital)}**.
        
        • Company registrations peaked around **{yearly.loc[yearly['Companies'].idxmax(),'Registration_Year']}**.
        """)