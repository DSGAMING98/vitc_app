"""
visuals.py
All plotting utilities for the Streamlit app.
"""

import matplotlib.pyplot as plt
from math import exp


def time_decay_chart(initial_vitc: float, k_per_min: float, max_minutes: int = 60):
    """
    Build a line chart of Vitamin C (mg/100g) vs time (minutes).

    Parameters
    ----------
    initial_vitc : float
        Starting Vitamin C (mg per 100 g).
    k_per_min : float
        Degradation rate constant (per minute).
    max_minutes : int
        Plot range (0 .. max_minutes).

    Returns
    -------
    matplotlib.figure.Figure
        A matplotlib Figure object ready for st.pyplot(fig)
    """
    if max_minutes < 1:
        max_minutes = 1

    xs = list(range(max_minutes + 1))
    ys = []

    for t in xs:
        if k_per_min > 0:
            remaining = initial_vitc * exp(-k_per_min * t)
        else:
            remaining = initial_vitc
        ys.append(remaining)

    fig, ax = plt.subplots()
    ax.plot(xs, ys, linewidth=2)
    ax.set_xlabel("Time (minutes)")
    ax.set_ylabel("Vitamin C (mg per 100 g)")
    ax.set_title("Vitamin C vs Time (estimated)")
    ax.grid(True, alpha=0.3)
    return fig


def compare_initial_final_bar(initial_vitc: float, final_vitc: float):
    """
    Build a 2-bar comparison: initial vs final Vitamin C.

    Parameters
    ----------
    initial_vitc : float
        Starting Vitamin C (mg per 100 g).
    final_vitc : float
        Ending Vitamin C (mg per 100 g).

    Returns
    -------
    matplotlib.figure.Figure
    """
    fig, ax = plt.subplots()
    ax.bar(["Initial", "After Cooking"], [initial_vitc, final_vitc])
    ax.set_ylabel("Vitamin C (mg per 100 g)")
    ax.set_title("Before vs After")
    for i, v in enumerate([initial_vitc, final_vitc]):
        ax.text(i, v, f"{v:.1f}", ha="center", va="bottom")
    return fig
