import pandas as pd

def transform_data():
    df = pd.read_csv('data/raw_sales.csv')
    
    # THE FIX: Convert to numeric and force errors to NaN, then fill with 0
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0)
    
    # Now this calculation won't crash!
    df['tax_amount'] = df['amount'] * 0.10
    df['total_with_tax'] = df['amount'] + df['tax_amount']
    
    # PRO TIP: Convert date strings to actual datetime objects
    df['date'] = pd.to_datetime(df['date'])
    
    df.to_csv('data/clean_sales.csv', index=False)
    print("✅ Transformation successful: Clean data saved to Gold layer.")

if __name__ == "__main__":
    transform_data()