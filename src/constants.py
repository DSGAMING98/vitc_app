"""
constants.py
Holds all fixed values the app uses.
These can be tuned later without touching the main logic.
"""

# Experimental/assumed Vitamin C degradation rate constants (k) per minute.
# Higher k = faster loss.
# These are illustrative defaults for the model and can be refined with literature / lab data.
METHOD_K_PER_MIN = {
    "Raw / Uncooked": 0.000,    # basically no thermal or leaching loss
    "Steaming":        0.015,   # gentle heat, less contact with water
    "Stir-fry":        0.025,   # higher surface heat, but short time
    "Boiling":         0.040,   # highest loss: heat + leaching into water
}

# Recommended safe slider range for cooking time in minutes
MIN_TIME_MIN = 0
MAX_TIME_MIN = 120

# Default portion reference (nutrition labels usually quote mg per 100 g)
DEFAULT_SERVING_GRAMS = 100

APP_TITLE = "Vitamin C Loss Calculator"
APP_TAGLINE = "Estimate nutrient damage during cooking so you can keep what's good."

FOOTNOTE = (
    "Vitamin C is water-soluble and heat-sensitive. Faster cooking with less water "
    "usually preserves more. This tool supports nutrition-aware cooking choices. "
    "Real world application: food preservation & nutrition. "
    "Source topic: Vitamin C loss calculator. "
)

