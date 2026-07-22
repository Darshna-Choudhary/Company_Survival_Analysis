# 📊 Indian Company Survival Analysis Dashboard

> An interactive data analytics dashboard that explores the survival patterns of Indian companies using real-world Ministry of Corporate Affairs (MCA) registration data.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Project Overview

Every year, thousands of companies are registered, but not all of them survive.

This project analyzes **125,000+ registered companies** from the **Ministry of Corporate Affairs (MCA)** to uncover the factors associated with long-term company survival.

Instead of simply visualizing data, the dashboard answers business questions such as:

- Which industries have the highest survival rates?
- Does paid-up capital influence company survival?
- Which registration years produced the most active companies?
- What characteristics distinguish active and inactive companies?

The result is an interactive Streamlit dashboard that enables users to explore these patterns through dynamic visualizations.

---

## 🎯 Project Objectives

- Analyze company survival trends across industries.
- Compare active and inactive companies.
- Study the relationship between capital and company survival.
- Explore company registration trends over time.
- Identify patterns that could support future survival prediction.

---

## 📂 Dataset

**Source**

- Ministry of Corporate Affairs (MCA), Government of India

The dataset contains information including:

- Company Name
- Registration Date
- Company Status
- Authorized Capital
- Paid-up Capital
- Industry Classification
- Company Category
- ROC Code
- State
- Listing Status

**Dataset Size**

- **125,000+ Companies**

---

# 📊 Dashboard Sections

## 🏠 Executive Summary

A quick overview of the dataset including:

- Total Companies
- Active Companies
- Inactive Companies
- Average Paid-up Capital
- Survival Percentage

---

## 💰 Capital Analysis

Explore how capital relates to company survival.

Includes:

- Paid-up Capital Distribution
- Authorized Capital Analysis
- Active vs Inactive Capital Comparison
- Capital Metrics

---

## 🏭 Industry Trends

Analyze how different industries have evolved over time.

Visualizations include:

- Company Registration Trend
- Industry-wise Registrations
- Registration Heatmap
- Top Growing Industries

---

## 📈 Survival Analysis

Understand long-term company survival.

Includes:

- Active vs Inactive Distribution
- Industry Survival Rates
- Survival by Registration Year
- Company Status Insights

---

# ✨ Features

✅ Interactive filters

✅ Responsive Streamlit dashboard

✅ Dynamic KPIs

✅ Interactive Plotly visualizations

✅ Industry-wise analysis

✅ Capital analysis

✅ Survival trend exploration

✅ Registration trend analysis

---

# 🛠 Tech Stack

| Tool | Purpose |
|-------|----------|
| Python | Programming |
| Pandas | Data Cleaning & Analysis |
| NumPy | Numerical Operations |
| Plotly | Interactive Charts |
| Streamlit | Dashboard Development |

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Darshna-Choudhary/Company_Survival_Analysis.git
```

Move into the project

```bash
cd Company_Survival_Analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the dashboard

```bash
streamlit run app.py
```

---

# 📊 Key Insights

Some interesting findings from the analysis include:

- Certain industries consistently exhibit higher survival rates.
- Companies with larger paid-up capital generally demonstrate greater longevity.
- Registration activity has varied significantly across decades.
- A relatively small number of industries account for the majority of registered companies.
- Survival patterns differ considerably across industrial classifications.

---

# 🔮 Future Work

The next phase of this project focuses on **building a predictive company survival system**.

The objective is to estimate whether a newly registered company is likely to remain active based on its characteristics such as:

- Industry
- Paid-up Capital
- Authorized Capital
- Registration Year
- Company Category
- Company Class

This will extend the project from descriptive analytics to predictive decision support.

---

# 📁 Project Structure

```
Company_Survival_Analysis
│
├── data/
├── images/
├── app.py
├── requirements.txt
├── README.md
└── notebooks/
```

---

# 🌟 Live Dashboard

👉 **Try it here**

https://companysurvivalanalysis-ahdfxwepf9eqskagiaqjsx.streamlit.app/

---

# 👩‍💻 Author

**Darshna Choudhary**

---

# ⭐ If you found this project useful

Consider giving the repository a **Star ⭐**

It helps others discover the project and motivates further development.