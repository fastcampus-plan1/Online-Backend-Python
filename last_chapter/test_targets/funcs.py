import pandas as pd

def process_customer_data(file_path):
    df = pd.read_csv(file_path)
    df['age'].fillna(0, inplace=True)
    df['age'] = df['age'].astype('int')
    return df


def process_join_dates(file_path):
    df = pd.read_csv(file_path)
    df['join_date'] = pd.to_datetime(df['join_date'])
    df["year"] = df["join_date"].dt.year
    df["month"] = df["join_date"].dt.month
    df["day"] = df["join_date"].dt.day
    df["hour"] = df["join_date"].dt.hour
    df["minute"] = df["join_date"].dt.minute
    return df
