import pandas as pd
import os

def extract_data():
    # Mock data creation
    data = {
        'order_id': [1, 2, 3, 4],
        'amount': [100.50, 200.00, 'ERROR', 150.75], # Include an error for the "fix" exercise
        'date': ['2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03']
    }
    df = pd.DataFrame(data)
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/raw_sales.csv', index=False)
    print("✅ Extraction complete: raw_sales.csv created.")

if __name__ == "__main__":
    extract_data()