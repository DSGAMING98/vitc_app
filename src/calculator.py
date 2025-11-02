"""
calculator.py
Core math/chemistry functions for Vitamin C decay.
Uses first-order degradation: C_final = C_initial * e^(-k * t)
"""

from math import exp


def vitc_remaining(initial_mg_per_100g: float, k_per_min: float, minutes: float) -> float:
    """
    Estimate remaining Vitamin C after heating/storing for a given time.

    Parameters
    ----------
    initial_mg_per_100g : float
        Starting Vitamin C content for the food (mg per 100 g serving).
    k_per_min : float
        Degradation rate constant for the chosen method (per minute).
        Higher k = faster nutrient loss.
    minutes : float
        Duration of exposure (cooking time in minutes).

    Returns
    -------
    float
        Estimated remaining Vitamin C in mg per 100 g.
    """
    if initial_mg_per_100g <= 0:
        return 0.0
    if k_per_min <= 0 or minutes <= 0:
        # No cooking or no degradation
        return float(initial_mg_per_100g)

    return float(initial_mg_per_100g * exp(-k_per_min * minutes))


def vitc_loss_pct(initial_mg_per_100g: float, final_mg_per_100g: float) -> float:
    """
    Calculate the % loss of Vitamin C.

    Parameters
    ----------
    initial_mg_per_100g : float
        Starting Vitamin C (mg per 100 g).
    final_mg_per_100g : float
        Ending Vitamin C (mg per 100 g).

    Returns
    -------
    float
        Percentage lost (0–100 range). Returns 0.0 if initial is 0.
    """
    if initial_mg_per_100g <= 0:
        return 0.0

    lost = initial_mg_per_100g - final_mg_per_100g
    pct = (lost / initial_mg_per_100g) * 100.0
    return float(max(pct, 0.0))
