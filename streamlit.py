import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="HAB Lake 101", layout="wide")

# -----------------------------
# CSS (Tabs equal + Card styling for bordered containers)
# -----------------------------
st.markdown(
    """
    <style>
    /* Overall */
    .stApp { background: #ffffff; }
    .block-container { padding-top: 1.2rem; padding-bottom: 2.5rem; }

    /* Title */
    .hab-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        letter-spacing: 0.5px;
        margin: 0.2rem 0 0.2rem 0;
    }
    .hab-subtitle {
        text-align: center;
        color: #6b7280;
        margin-top: 0.3rem;
        margin-bottom: 1.6rem;
        font-size: 1rem;
    }

    /* Tabs: full width, equal space */
    div[data-baseweb="tab-list"] {
        display: flex !important;
        justify-content: space-between !important;
        width: 100% !important;
        border-bottom: 1px solid #e5e7eb !important;
        padding-bottom: 6px !important;
        margin-bottom: 20px !important;
    }
    button[data-baseweb="tab"] {
        flex: 1 1 0 !important;
        text-align: center !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        color: #374151 !important;
        padding: 12px 0 !important;
        margin: 0 10px !important;
        border-radius: 12px !important;
        background: #f9fafb !important;
        border: 1px solid #e5e7eb !important;
        transition: all 0.15s ease-in-out;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        background: #111827 !important;
        color: #ffffff !important;
        border: 1px solid #111827 !important;
        box-shadow: 0 10px 25px rgba(17, 24, 39, 0.15) !important;
    }
    button[data-baseweb="tab"]:hover {
        background: #eef2ff !important;
        border-color: #c7d2fe !important;
    }

    /* Section headings */
    .hab-section-title {
        font-size: 1.6rem;
        font-weight: 800;
        margin: 0.25rem 0 0.75rem 0;
        color: #111827;
    }

    /* IMPORTANT: Style ONLY bordered containers (this wrapper appears when border=True) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: #ffffff !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 16px !important;
        box-shadow: 0 12px 30px rgba(0,0,0,0.08) !important;
        padding: 12px 12px 6px 12px !important;
    }

    /* Reduce extra blank space above pyplot inside bordered container */
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
st.markdown("<div class='hab-subtitle'>Lake-101 Water Quality Dashboard (Prototype UI)</div>", unsafe_allow_html=True)

# -----------------------------
# Random Graph Generator (demo)
# -----------------------------
def random_graph(title: str, seed: int):
    rng = np.random.default_rng(seed)
    x = np.arange(1, 31)
    y = np.cumsum(rng.normal(0, 1, size=len(x))) + rng.uniform(10, 30)

    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    ax.plot(x, y, marker="o", linewidth=1.6)
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.set_xlabel("Day")
    ax.set_ylabel("Value")
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    return fig

# -----------------------------
# Tab content builder
# -----------------------------
def build_tab(metric_name: str, base_seed: int):
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown("<div class='hab-section-title'>Daily & Monthly</div>", unsafe_allow_html=True)
        with st.container(border=True):  # graph INSIDE this box
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