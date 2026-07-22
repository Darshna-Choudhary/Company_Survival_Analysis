import streamlit as st
from streamlit_option_menu import option_menu

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Indian Company Survival Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background:#111827;
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* Metric cards */

.metric-card{

    background:white;

    padding:20px;

    border-radius:15px;

    border:1px solid #e5e7eb;

    box-shadow:0px 2px 10px rgba(0,0,0,0.08);

    transition:0.3s;
}

.metric-card:hover{

    transform:translateY(-4px);

    box-shadow:0px 6px 20px rgba(0,0,0,.12);
}

/* Headings */

.big-title{

    font-size:38px;

    font-weight:700;

    color:#111827;
}

.sub-title{

    font-size:18px;

    color:#6b7280;

    margin-top:-10px;
}

/* HR */

hr{

    margin-top:8px;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.markdown(
    '<p class="big-title">📊 Indian Company Survival Analysis Dashboard</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Exploring company survival patterns across industries, capital structure and registration trends.</p>',
    unsafe_allow_html=True
)
page = st.radio(
    "Navigation",
    ["Executive Summary",
     "Capital Analysis",
     "Industry Trends",
     "Survival Analysis"]
)
st.divider()

# -------------------------------------------------
# PAGE ROUTING
# -------------------------------------------------

if page == "Executive Summary":

    from pages.executive_summary import show_page
    show_page()

elif page == "Survival Analysis":

    from pages.survival_analysis import show_page
    show_page()

elif page == "Capital Analysis":

    from pages.capital_analysis import show_page
    show_page()

elif page == "Industry Trends":

    from pages.industry_trends import show_page
    show_page()