ABC Inventory Classification (Revenue & Profit Based)

This project performs a complete SKU-level ABC inventory analysis using both
revenue and profit as classification drivers. It combines data cleaning,
aggregation, Pareto analysis, and clear business recommendations — all using Python.

📌 Key Features

✔ SKU-level revenue aggregation

✔ SKU-level profit aggregation

✔ Revenue-based ABC classification

✔ Profit-based ABC classification

✔ Pareto charts (Revenue & Profit)

✔ Category-stacked ABC breakdown

✔ SKU ranking visualizations

✔ Data quality checks (SKU–Product mapping issues)

✔ Clear business recommendations

✔ Modular Python pipeline (main.py, utils.py)

✔ Jupyter notebook for full analysis

✔ 12 visualizations saved in outputs/figures/

🧠 Why This Project Matters

ABC analysis is a foundational supply-chain technique that helps businesses:

Identify the high-value SKUs that drive the majority of revenue

Understand profit concentration across SKU portfolios

Prioritize replenishment of A-class SKUs

Optimize safety stock

Reduce working capital tied to long-tail (C-class) items

This project offers both revenue and profit perspectives, similar to what real
inventory analysts do inside retail, e-commerce, CPG, or warehousing teams.

📂 Project Structure
abc-inventory-analysis/
│
├── notebooks/
│   └── 01-abc-analysis.ipynb               ← Final polished notebook
│
├── src/
│   ├── main.py                             ← Reproducible pipeline
│   └── utils.py
│
├── data/
│   ├── raw/
│   │   └── Sample - Superstore.csv         ← Original dataset
│   ├── processed/
│   │   ├── sku_master_abc.csv              ← FINAL master dataset
│   │   ├── sku_abc_by_profit.csv
│   │   └── sku_abc_with_labels.csv
│   └── archived/
│       └── (intermediate CSVs)
│
├── outputs/
│   ├── figures/
│   │   └── (12 visualizations in PNG)
│   └── reports/
│       ├── final_report.md
│       └── insights.md
│
└── README.md

📊 Example Visuals

Below are some of the key charts included in this project:

Revenue Pareto Chart

Profit Pareto Chart

Category-wise ABC split

Top 15 revenue-generating SKUs

Top 15 profit-generating SKUs

ABC distribution bar charts

Value share pie charts

Unit price distribution by ABC class

All figures are available in outputs/figures/.

🧪 How To Run

Install required packages:

pip install -r requirements.txt


Run the reproducible pipeline:

python src/main.py


Or open the full analysis notebook:

notebooks/01-abc-analysis.ipynb

🧩 Business Insights (Summary)

A-Class SKUs

~15% of SKUs but ~70% of revenue and profit

Require daily review and tight replenishment

High stockout risk impact

B-Class SKUs

Moderate contributors

Weekly review cycle

Good candidates for promotions

C-Class SKUs

Low-value, long-tail items

Lower safety stock

Candidates for SKU rationalization

🚀 Conclusion

This project demonstrates a complete supply-chain analytics workflow with clean code, structured modular design, curated visualizations, and actionable recommendations.
It reflects industry practices used by operations, merchandising, or supply-chain planning teams.

👤 Author

Joel