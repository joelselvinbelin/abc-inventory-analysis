
# Final Report — ABC Inventory Classification (Revenue + Profit)

## Executive Summary  
This project was an incredibly fun deep-dive into **retail analytics**, and I genuinely enjoyed breaking down the data to see how revenue and profit concentrate among a small set of SKUs.  

Using Python, Pandas, and Matplotlib, I performed both **Revenue-Based ABC** and **Profit-Based ABC** analyses to understand which SKUs drive value — not only in sales volume, but actual profitability.  

The results clearly show a classic **Pareto distribution**: a small number of SKUs dominate revenue and profit, making them the top candidates for tighter inventory control and strategic focus.

---

## Revenue-Based ABC Classification  
Total SKUs analyzed: **1862**

### Class Distribution (Revenue)
- **A-class:** 280 SKUs — contribute **69.95%** of all revenue  
- **B-class:** 373 SKUs — contribute **20.03%**  
- **C-class:** 1209 SKUs — contribute **10.02%**

This means about **15% of SKUs generate ~70% of revenue**, a beautifully clean Pareto curve (saved as: `pareto_revenue.png`).  

Other helpful charts saved:
- `abc_counts_revenue.png` (SKU count by class)  
- `abc_value_share_revenue_pie.png` (value distribution pie chart)  
- `top_15_skus_revenue.png` (top performers)  

---

## Profit-Based ABC Classification  
Profit often tells a *different story* than revenue — and that was exactly the case here.

### Class Distribution (Profit)
- **A-profit items:** 69.97% of total profit  
- **B-profit items:** 19.94%  
- **C-profit items:** 10.09%  

Some SKUs that are “A” in revenue fall into “B” or “C” in profit, meaning:
- they sell a lot but earn little  
- or discounts shrink margins  
- or costs are too high relative to price  

Visuals saved:  
- `pareto_profit.png`  
- `top_15_skus_profit.png`

---

## Data Quality: SKU–Product Name Mismatch  
I found **32 SKUs** with inconsistent product names (e.g., one SKU having 2–3 different descriptions).  
These SKUs represent **4.24%** of revenue.

This is realistic — companies often have messy master data.  

Action taken:
- Canonicalized names using the most frequent description  
- Created a manual review file: `sku_manual_mapping_template.csv`  
- Documented the issue in this report  

---

## Insights & Interpretation

### 🔥 Insight 1 — The business runs on a small set of SKUs  
A-items (top revenue drivers) need:
- tight safety stock  
- accurate forecasting  
- reliable suppliers  
- priority replenishment  

### 💸 Insight 2 — Revenue winners ≠ Profit winners  
Several SKUs were high-revenue but low-profit.  
These should be reviewed for:
- heavy discounting  
- high acquisition cost  
- promotional leakage  
- potential price increase  

### 🧊 Insight 3 — C-items may not deserve complex tracking  
C-class SKUs contribute little to overall value. They are good candidates for:
- bulk ordering  
- longer replenishment cycles  
- vendor-managed inventory  
- even SKU rationalization  

### ⚠ Insight 4 — Data quality matters  
Duplicate naming or inconsistent SKU mapping impacts:
- forecasting  
- ABC accuracy  
- category-level decisions  
- dashboards  

The data quality check was a valuable part of this project.

---

## Recommended Business Actions

1. **Review the top A-profit SKUs** for opportunities:
   - pricing power  
   - supplier negotiations  
   - demand shaping  

2. **Audit A-revenue but C-profit SKUs**  
   These are “fake heroes”.

3. **Simplify handling of C-items**  
   Apply low-touch inventory strategies.

4. **Clean master data** for the 64 inconsistent SKUs  
   Use `sku_manual_mapping_template.csv`.

---

## What I Learned  
This project helped me understand:
- the practical use of ABC classification  
- differences between revenue and profit prioritization  
- working with messy real-world data  
- building a full analytics workflow end-to-end  
- producing visual insights that actually help operations teams  

Honestly, diving into this kind of analysis confirmed that **data analytics is genuinely exciting** and something I want to keep improving at.

---

## Files Saved in This Project
- **Master dataset:** `sku_master_summary.csv`  
- **Revenue ABC charts:** `pareto_revenue.png`, `abc_value_share_revenue_pie.png`, etc.  
- **Profit ABC charts:** `pareto_profit.png`  
- **Anomaly template:** `sku_manual_mapping_template.csv`  
- **This report:** `final_report.md`

---

Report generated automatically via Python.
