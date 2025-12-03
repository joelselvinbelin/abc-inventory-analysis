from pathlib import Path
import pandas as pd
from utils import load_data, clean_data, aggregate_sku, abc_classification, add_profit, plot_pareto, save_master

def main():
    # -------- Paths --------
    raw_path = Path('../data/raw/Sample - Superstore.csv')
    processed_dir = Path('../data/processed')
    figures_dir = Path('../outputs/figures')
    reports_dir = Path('../outputs/reports')

    processed_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    print('Loading raw data...')
    df_raw = load_data(raw_path)

    print('Cleaning data...')
    df_clean = clean_data(df_raw)

    print('Aggregating SKU-level metrics...')
    sku_df = aggregate_sku(df_clean)

    print('Running ABC classification (Revenue)...')
    abc_rev = abc_classification(sku_df, value_col='total_value')

    print('Running ABC classification (Profit)...')
    abc_profit = add_profit(abc_rev)

    # Save combined output
    master_outfile = processed_dir / 'sku_master_abc.csv'
    save_master(abc_profit, master_outfile)

    print(f'Saved master SKU ABC dataset → {master_outfile}')

    # -------- Charts --------
    print('Creating revenue Pareto chart...')
    plot_pareto(abc_profit, 'total_value', figures_dir / 'revenue_pareto.png')

    print('Creating profit Pareto chart...')
    plot_pareto(abc_profit, 'profit_sum', figures_dir / 'profit_pareto.png')

    print('All charts saved.')

    # -------- Summary text report --------
    report_path = reports_dir / 'summary.txt'
    with report_path.open('w') as f:
        f.write('ABC Inventory Classification Summary\n')
        f.write('-------------------------------------\n\n')
        f.write('Revenue ABC distribution:\n')
        f.write(str(abc_profit['ABC_class'].value_counts()) + '\n\n')
        f.write('Profit ABC distribution:\n')
        f.write(str(abc_profit['ABC_profit'].value_counts()) + '\n')

    print(f'Report saved → {report_path}')

if __name__ == '__main__':
    main()
