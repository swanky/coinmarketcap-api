import pandas as pd
import csv
from datetime import datetime, date, time
from rx import Observable


def get_price():
    api_url = 'https://api.coinmarketcap.com/v1/ticker/?limit=20'
    df = pd.read_json(api_url)
    df['timestamp'] = df.last_updated.map(lambda x: datetime.fromtimestamp(int(x)).strftime("%Y-%m-%d %H:%M:%S"))
    return df


save_df = get_price()


def write_csv():
    global save_df
    save_df = save_df.append(get_price(), ignore_index=True)
    save_df = save_df.drop_duplicates()
    save_df.to_csv('test.csv', index=False, mode='w+')


Observable.interval(60000).subscribe(lambda s: write_csv())

input("Press any key to quit\n")
