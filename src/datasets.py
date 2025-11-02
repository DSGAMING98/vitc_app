"""
datasets.py
Food Vitamin C reference values.

This file gives default Vitamin C content (mg per 100 g) for common foods.
These are example values used to pre-fill the app so users don't always
have to manually look up numbers.

You can extend/replace this table with lab data or nutrition table data.
"""

import pandas as pd


def load_sample_foods() -> pd.DataFrame:
    """
    Return a small DataFrame of foods and their baseline Vitamin C content.

    Returns
    -------
    pandas.DataFrame with columns:
        - food: str
        - vitc_mg_per_100g: float
    """

    # Approximate typical Vitamin C content per 100 g edible portion.
    # These are illustrative placeholders for demo.
    rows = [
        {"food": "Orange",            "vitc_mg_per_100g": 53.2},
        {"food": "Guava",             "vitc_mg_per_100g": 228.3},
        {"food": "Broccoli",          "vitc_mg_per_100g": 89.2},
        {"food": "Strawberry",        "vitc_mg_per_100g": 58.8},
        {"food": "Capsicum (Red)",    "vitc_mg_per_100g": 128.0},
        {"food": "Tomato",            "vitc_mg_per_100g": 13.7},
        {"food": "Spinach (raw)",     "vitc_mg_per_100g": 28.1},
        {"food": "Mango (ripe)",      "vitc_mg_per_100g": 36.4},
        {"food": "Lemon",             "vitc_mg_per_100g": 53.0},
        {"food": "Amla (Indian gooseberry)", "vitc_mg_per_100g": 252.0},
    ]

    df = pd.DataFrame(rows)


    df = df.sort_values(by="food").reset_index(drop=True)
    return df
