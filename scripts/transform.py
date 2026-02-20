import pandas as pd

def transform_data():
    # 1. Load the raw data
    df = pd.read_csv('data/raw_sales.csv')
    print("Reading raw data...")

    # 2. BUG: Attempting to calculate tax on uncleaned data
    # This will FAIL because the 'amount' column contains the string 'ERROR'
    df['tax_amount'] = df['amount'] * 0.10 
    
    # 3. BUG: Date format is left as a string (harder for BI tools to use)
    df['total_with_tax'] = df['amount'] + df['tax_amount']

    # 4. Save to Silver Layer
    df.to_csv('data/clean_sales.csv', index=False)
    print("Transformation complete (or so we think...)")

if __name__ == "__main__":
    transform_data()