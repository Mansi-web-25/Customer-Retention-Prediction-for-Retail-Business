import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    df.dropna(inplace=True)
    df['total_spent'] = df['purchase_frequency'] * df['avg_order_value']
    return df
