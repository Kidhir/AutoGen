import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna(axis=1, how='all')  # Drop columns that are completely empty
    df = df.fillna(df.mean(numeric_only=True))  # Fill missing numeric values with column mean
    return df
