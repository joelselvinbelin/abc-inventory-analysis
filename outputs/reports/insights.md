### Data quality: SKU–Product name mismatch

Detected 32 SKUs that map to multiple Product Name values in the raw orders table.
- Combined revenue for these SKUs: 97,465.67 (4.24% of total revenue).
- Number of A-class SKUs affected: 10.

Action taken:
- For reporting we canonicalized product_name by using the most frequent (mode) Product Name per SKU.
- Original raw names are left intact in data/raw for audit and manual review.
- Recommendation: manually review the affected A-class SKUs and any SKUs contributing materially to revenue, and correct master data if they represent different physical products.
