import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data


def show_page():
    df = load_data()
    st.title("🏭 Industry Trends")
    st.caption(
        "Explore registration trends, industry growth, survival rates and industry evolution over time."
    )
    st.divider()
    registration = df[
        df["Registration_Year"].between(1980, 2025)]
    registration = (
        registration
        .groupby("Registration_Year")
        .size()
        .reset_index(name="Registrations")
    )

    fig = px.line(
        registration,
        x="Registration_Year",
        y="Registrations",
        markers=True
    )
    fig.update_layout(
        title="Company Registration Trend",
        xaxis_title="Registration Year",
        yaxis_title="Companies Registered",
        hovermode="x unified",
        height=500
    )
    fig.update_xaxes(range=[1980, 2025])

    fig.update_traces(
        line=dict(width=4),
        marker=dict(size=7)
    )

    st.plotly_chart(fig, use_container_width=True)
    left,right = st.columns(2)
    growth = (
        df[df["Registration_Year"].between(2015,2025)]
        .pivot_table(
            index="CompanyIndustrialClassification",
            columns="Registration_Year",
            aggfunc="size",
            fill_value=0
        )
    )

    growth["Growth"] = growth.get(2025,0) - growth.get(2015,0)
    growth = (
        growth
        .sort_values("Growth",ascending=False)
        .head(10)
        .reset_index()
    )

    with left:
        fig = px.bar(
            growth,
            x="Growth",
            y="CompanyIndustrialClassification",
            orientation="h",
            color="Growth",
            color_continuous_scale="Greens"
        )

        fig.update_layout(
            title="Top Growing Industries (2015 → 2025)",
            xaxis_title="Growth",
            yaxis_title="Industry",
            height=450,
            coloraxis_showscale=False
        )

        st.plotly_chart(fig,use_container_width=True)
    survival = (
            df.groupby("CompanyIndustrialClassification")["CompanyStatus"]
            .apply(lambda x:(x=="Active").mean()*100)
            .reset_index(name="Active %")
        )

    survival["Companies"] = df.groupby("CompanyIndustrialClassification").size().values
    survival = (
            survival[survival["Companies"]>=30]
            .sort_values("Active %",ascending=False)
            .head(10)
        )

    with right:
        fig = px.bar(
            survival,
            x="Active %",
            y="CompanyIndustrialClassification",
            orientation="h",
            color="Active %",
            color_continuous_scale="Blues"
        )

        fig.update_layout(
            title="Industry Survival Rate",
            xaxis_title="Active Companies (%)",
            yaxis_title="Industry",
            height=450,
            coloraxis_showscale=False
        )

        st.plotly_chart(fig,use_container_width=True)
    
    heat = (
    df[df["Registration_Year"].between(1970, 2025)]
    .pivot_table(
        index="CompanyIndustrialClassification",
        columns="Registration_Year",
        aggfunc="size",
        fill_value=0
    ))
    heat = heat.loc[
        heat.sum(axis=1)
        .sort_values(ascending=False)
        .head(10)
        .index]
    fig = px.imshow(
    heat,
    aspect="auto",
    color_continuous_scale="Blues",
    labels={
        "x": "Registration Year",
        "y": "Industry",
        "color": "Registrations"
    })
    fig.update_layout(
    title={
        "text": "Industry × Registration Year",
        "x": 0.02,
        "font": dict(size=24)
    },
    height=500,          # increase height
    width=1300,          # optional (Streamlit container may override)
    margin=dict(l=220, r=40, t=70, b=70),
    font=dict(size=16),  # overall font
    coloraxis_colorbar=dict(
        title="Registrations",
        title_font=dict(size=18),
        tickfont=dict(size=14),
        len=0.8
    ))
    fig.update_xaxes(
    title_font=dict(size=18),
    tickfont=dict(size=14))
    
    fig.update_yaxes(
    title_font=dict(size=18),
    tickfont=dict(size=14),
    automargin=True)
    st.plotly_chart(fig, use_container_width=True)
    
    peak_year = registration.loc[
        registration["Registrations"].idxmax(),
        "Registration_Year"
    ]

    top_growth = growth.iloc[0]["CompanyIndustrialClassification"]
    best_survival = survival.iloc[0]["CompanyIndustrialClassification"]
    best_rate = survival.iloc[0]["Active %"]

    st.info(f"""
    ### 📌 Key Insights
    • Company registrations peaked in **{peak_year}**.

    • The fastest-growing industry between **2015 and 2025** is **{top_growth}**.
    
    • **{best_survival}** has the highest survival rate (**{best_rate:.1f}%**) among industries with at least 30 companies.
    
    • The heatmap highlights how different industries have expanded or contracted over time.
    """)