import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="HAB Lake 101", layout="wide")

# -----------------------------
# CSS – PREMIUM DASHBOARD LOOK
# -----------------------------
st.markdown(
    """
    <style>
    /* ---------- App Background ---------- */
    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
    }

    .block-container {
        padding-top: 1.4rem;
        padding-bottom: 2.5rem;
    }

    /* ---------- Title ---------- */
    .hab-title {
        text-align: center;
        font-size: 3.2rem;
        font-weight: 900;
        background: linear-gradient(90deg, #0f172a, #1e3a8a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
    }

    .hab-subtitle {
        text-align: center;
        color: #475569;
        font-size: 1.05rem;
        margin-bottom: 1.8rem;
    }

    /* ---------- Tabs ---------- */
    div[data-baseweb="tab-list"] {
        display: flex !important;
        justify-content: space-between !important;
        width: 100% !important;
        border-bottom: 2px solid #e5e7eb !important;
        padding-bottom: 8px !important;
        margin-bottom: 26px !important;
    }

    button[data-baseweb="tab"] {
        flex: 1;
        margin: 0 10px !important;
        padding: 12px 0 !important;
        border-radius: 14px !important;
        background: #f1f5f9 !important;
        border: 1px solid #e2e8f0 !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        color: #334155 !important;
        transition: all 0.2s ease-in-out;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #0f172a, #1e40af) !important;
        color: #ffffff !important;
        border: none !important;
        box-shadow: 0 12px 30px rgba(30, 64, 175, 0.35) !important;
    }

    button[data-baseweb="tab"]:hover {
        background: #e0e7ff !important;
        border-color: #c7d2fe !important;
    }

    /* ---------- Section Titles ---------- */
    .hab-section-title {
        font-size: 1.65rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 0.75rem;
    }

    /* ---------- Card Containers ---------- */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(180deg, #ffffff, #f8fafc) !important;
        border-radius: 18px !important;
        border-top: 5px solid #1e40af !important;
        border-left: 1px solid #e5e7eb !important;
        border-right: 1px solid #e5e7eb !important;
        border-bottom: 1px solid #e5e7eb !important;
        box-shadow: 0 14px 35px rgba(15, 23, 42, 0.12) !important;
        padding: 14px 14px 10px 14px !important;
    }

    /* Reduce empty spacing */
    div[data-testid="stVerticalBlockBorderWrapper"] .element-container {
        margin-top: 0.2rem !important;
        margin-bottom: 0.2rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Title
# -----------------------------
st.markdown("<div class='hab-title'>HAB Lake 101</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='hab-subtitle'>Lake-101 Water Quality Dashboard (Prototype UI)</div>",
    unsafe_allow_html=True
)

# -----------------------------
# Graph Generator
# -----------------------------
def random_graph(title: str, seed: int):
    rng = np.random.default_rng(seed)
    x = np.arange(1, 31)
    y = np.cumsum(rng.normal(0, 1, size=len(x))) + rng.uniform(10, 30)

    fig, ax = plt.subplots(figsize=(7.6, 3.9))
    ax.plot(x, y, marker="o", linewidth=2.2, color="#1e40af")
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.set_xlabel("Day")
    ax.set_ylabel("Value")
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    return fig

# -----------------------------
# Tab Content Builder
# -----------------------------
def build_tab(metric_name: str, base_seed: int):
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown("<div class='hab-section-title'>Daily & Monthly</div>", unsafe_allow_html=True)
        with st.container(border=True):
            st.pyplot(random_graph(f"{metric_name}: Daily/Monthly", base_seed + 1), clear_figure=True)

    with col2:
        st.markdown("<div class='hab-section-title'>Models</div>", unsafe_allow_html=True)
        with st.container(border=True):
            st.pyplot(random_graph(f"{metric_name}: Models", base_seed + 2), clear_figure=True)

    with col3:
        st.markdown("<div class='hab-section-title'>Predicted</div>", unsafe_allow_html=True)
        with st.container(border=True):
            st.pyplot(random_graph(f"{metric_name}: Predicted", base_seed + 3), clear_figure=True)

# -----------------------------
# Tabs
# -----------------------------
tabs = st.tabs(["Chla", "DO", "PH", "Turbidity"])

with tabs[0]:
    build_tab("Chla", 100)

with tabs[1]:
    build_tab("DO", 200)

with tabs[2]:
    build_tab("PH", 300)

with tabs[3]:
    build_tab("Turbidity", 400)