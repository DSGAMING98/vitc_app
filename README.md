# Vitamin C Loss Calculator

A Streamlit web app that estimates how much Vitamin C is lost during cooking and storage. The goal is nutrition-aware cooking: keep the nutrients instead of boiling them away.  
Real-world application: Food preservation and nutrition. :contentReference[oaicite:0]{index=0}
This app is made by a small group who study in Jain University for chemistry project overshowing how we could do these things
---

## 1. What this app does
- Takes a food item (e.g. orange, broccoli, capsicum).
- Uses an initial Vitamin C value in mg per 100 g.
- Lets the user pick a cooking method (raw, steam, stir-fry, boil).
- Uses an estimated degradation rate ("k value") for that method.
- Uses first-order decay to estimate:
  - Vitamin C remaining (mg/100 g)
  - Percentage lost (%)
  - A plot of Vitamin C vs time.

This helps compare cooking styles for better nutrient retention.

---

## 2. Why Vitamin C
- Vitamin C (ascorbic acid) is heat-sensitive and water-soluble.
- Boiling causes leaching into water.
- Steaming generally preserves more Vitamin C than boiling.
- Tracking this is relevant to meal planning, nutrition, and food science.

---

## 3. How the math works
We model Vitamin C loss as first-order decay:

Final_VitC = Initial_VitC × e^(−k × t)

Where:  
- Initial_VitC = Vitamin C before cooking (mg per 100 g)  
- k = degradation rate constant per minute (depends on method)  
- t = time in minutes  
- Final_VitC = estimated Vitamin C after cooking

Vitamin C loss %:
Loss% = ((Initial − Final) / Initial) × 100

---

## 4. Project structure
```text
vitc_app/
├─ app.py
├─ requirements.txt
├─ README.md
├─ .streamlit/
│  └─ config.toml
├─ src/
│  ├─ __init__.py
│  ├─ constants.py
│  ├─ calculator.py
│  ├─ datasets.py
│  └─ visuals.py
├─ data/
│  └─ sample_foods.csv
├─ assets/
│  └─ logo.png          (optional)
└─ tests/
   └─ test_calculator.py (optional)
