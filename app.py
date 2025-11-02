import streamlit as st
import pandas as pd

from src.constants import (
    METHOD_K_PER_MIN,
    MIN_TIME_MIN,
    MAX_TIME_MIN,
    APP_TITLE,
    APP_TAGLINE,
    FOOTNOTE,
)
from src.calculator import vitc_remaining, vitc_loss_pct
from src.datasets import load_sample_foods
from src.visuals import time_decay_chart, compare_initial_final_bar


# Page config
st.set_page_config(
    page_title="Vitamin C Loss Calculator",
    page_icon="🧪",
    layout="centered",
)


# Header
st.title(APP_TITLE)
st.caption(APP_TAGLINE)
st.markdown(
    "This tool estimates how much Vitamin C is lost during cooking based on time and method. "
    "Real-world focus: food preservation and nutrition. "
    "This matches the 'Vitamin C loss calculator' topic for experiential learning. "
    ":contentReference[oaicite:0]{index=0}"
)


#  Sidebar Inputs
with st.sidebar:
    st.header("Input Parameters")

    # 1. choose food
    foods_df = load_sample_foods()
    food_choice = st.selectbox(
        "Select food item (mg Vitamin C per 100 g will auto-fill):",
        options=foods_df["food"].tolist(),
        index=0,
    )

    # lookup vitamin C for that food
    base_vitc_val = float(
        foods_df.loc[foods_df["food"] == food_choice, "vitc_mg_per_100g"].iloc[0]
    )

    # allow manual override
    initial_vitc = st.number_input(
        "Initial Vitamin C (mg per 100 g)",
        min_value=0.0,
        value=base_vitc_val,
        step=0.1,
        help="If you have lab/label data, enter it here.",
    )

    # cooking method
    method_choice = st.selectbox(
        "Cooking / Processing Method",
        options=list(METHOD_K_PER_MIN.keys()),
        index=1 if "Steaming" in METHOD_K_PER_MIN else 0,
        help="Different methods destroy Vitamin C at different rates.",
    )

    # cooking time
    cook_time = st.slider(
        "Cooking / Holding Time (minutes)",
        min_value=MIN_TIME_MIN,
        max_value=MAX_TIME_MIN,
        value=10,
        step=1,
    )


# Core Calculation
k_value = METHOD_K_PER_MIN[method_choice]
final_vitc = vitc_remaining(
    initial_mg_per_100g=initial_vitc,
    k_per_min=k_value,
    minutes=cook_time,
)
loss_pct = vitc_loss_pct(
    initial_mg_per_100g=initial_vitc,
    final_mg_per_100g=final_vitc,
)


# Results Summary Metrics
st.subheader("Nutrient Retention Estimate")

left_col, right_col = st.columns(2)
with left_col:
    st.metric(
        label="Remaining Vitamin C (mg / 100 g)",
        value=f"{final_vitc:.2f}",
        help="Estimated Vitamin C left after the selected cooking method + time.",
    )

with right_col:
    st.metric(
        label="Vitamin C Lost (%)",
        value=f"{loss_pct:.2f} %",
        help="Percent destroyed or leached out.",
    )

st.write(
    f"Food: **{food_choice}**  |  Method: **{method_choice}**  |  Time: **{cook_time} min**"
)

st.divider()


#  Visual: Initial vs Final
st.subheader("Before vs After Cooking")
bar_fig = compare_initial_final_bar(initial_vitc, final_vitc)
st.pyplot(bar_fig, use_container_width=True)


#  Visual: Decay Over Time
st.subheader("Vitamin C vs Time Curve")
max_plot_time = max(cook_time, 60)
line_fig = time_decay_chart(
    initial_vitc=initial_vitc,
    k_per_min=k_value,
    max_minutes=max_plot_time,
)
st.pyplot(line_fig, use_container_width=True)

st.caption(
    "Curve shows estimated Vitamin C (mg/100 g) if cooking continued for longer. "
    "If k = 0 (raw / uncooked), the curve is flat."
)

st.divider()


# Assumptions / Science Note
with st.expander("Model assumptions and chemistry note"):
    st.markdown(
        """
**Degradation model used**
- We assume first-order degradation:  
  Final = Initial × e^(−k × t)  
  where k is a method-specific constant (per minute) and t is time in minutes.
- Larger k means faster Vitamin C destruction.

**Why methods matter**
- Boiling: high heat + water → Vitamin C leaches out and breaks down.
- Stir-fry: high heat but short time, less water contact.
- Steaming: gentler heat, minimal leaching.
- Raw / Uncooked: almost no heat-related destruction.

**Why this matters in real life**
- Vitamin C supports immunity and is easily destroyed by heat.
- Tracking Vitamin C retention helps guide cooking/processing choices to preserve nutrients, which is part of food preservation and nutrition. :contentReference[oaicite:1]{index=1}

**Limitations**
- k values are illustrative defaults, not lab-calibrated for every food.
- Surface area, pH, reheating, storage, and oxygen exposure can also change Vitamin C.
"""
    )

st.info(FOOTNOTE)
with st.expander("Model assumptions and chemistry note"):
    st.markdown(
        """
        ... (unchanged text from before)
        """
    )

st.info(FOOTNOTE)

st.divider()

st.subheader("Project Credits")

st.markdown(
    """
**Developed by:**  
- Prajwal C Pradhan — primary developer (application logic, Streamlit UI)

**Contributors (support, data, review):**  
- M Sanjana Reddy  
- Namgay D Wangchuk  
- Malavika Vinod  
- Pakalapati Monika  
- Lepmuhang Dewan  

**Group note:**  
"Experential Learning has been a blast. Creating an app was an experience. Just want to say, it's been a great learning trip.
Hope we all learnt something from this!"

**Copyright:**  
© 2025 Vitamin C Loss Calculator. All rights reserved.
"""
)
