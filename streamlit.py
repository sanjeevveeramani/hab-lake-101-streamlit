import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1) Page settings (wide screen)
st.set_page_config(page_title="HAB Lake 101", layout="wide")

# 2) Title (Heading)
st.markdown(
    "<h1 style='text-align:center;'>HAB Lake 101</h1>",
    unsafe_allow_html=True
)

# 3) Function to create random graphs
def random_graph(title: str, seed: int):
    rng = np.random.default_rng(seed)
    x = np.arange(1, 31)
    y = np.cumsum(rng.normal(0, 1, size=len(x))) + rng.uniform(10, 30)

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(x, y, marker="o", linewidth=1.5)
    ax.set_title(title)
    ax.set_xlabel("Day")
    ax.set_ylabel("Value")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return fig

# 4) Tabs
tabs = st.tabs(["Chla", "DO", "PH", "Turbidity"])

# 5) Tab content builder
def build_tab(tab_name: str, base_seed: int):
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.subheader("Daily & Monthly")
        with st.container(border=True):
            st.pyplot(random_graph(f"{tab_name}: Daily/Monthly", base_seed + 1), clear_figure=True)

    with col2:
        st.subheader("Models")
        with st.container(border=True):
            st.pyplot(random_graph(f"{tab_name}: Models", base_seed + 2), clear_figure=True)

    with col3:
        st.subheader("Predicted")
        with st.container(border=True):
            st.pyplot(random_graph(f"{tab_name}: Predicted", base_seed + 3), clear_figure=True)

# 6) Build each tab
with tabs[0]:
    build_tab("Chla", 100)

with tabs[1]:
    build_tab("DO", 200)

with tabs[2]:
    build_tab("PH", 300)

with tabs[3]:
    build_tab("Turbidity", 400)