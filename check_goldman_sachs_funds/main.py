from datetime import date
import requests
import pandas as pd
from io import StringIO

fund_ids = {
    "Goldman Sachs Krótkoterminowy Obligacji": 15,
    "Goldman Sachs Akcji": 1,
    "Goldman Sachs Zrównoważony": 2,
    "Goldman Sachs Średnich i Małych Spółek": 10
}

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

final_df = pd.DataFrame(columns=['fundusz', 'kurs_start', 'kurs_teraz', 'kurs_min', 'kurs_min_date', 'kurs_max', 'kurs_max_date', 'last_week_avg', 'change_alltime', 'change_1_week', 'change_1_month'])

today_date = date.today().strftime("%Y-%m-%d")

for i in fund_ids:
    download_url = f"https://www.gstfi.pl/?action=quotes.getQuotesCsv&startDate=2025-08-26&endDate={today_date}&fundIds={fund_ids[i]}&unitCategoryIds=1"
    response = requests.get(download_url)
    
    source_csv = response.text
    df = pd.read_csv(StringIO(source_csv), sep=',', decimal='.')

    new_row = {
        'fundusz': i,
        'kurs_start': df.iloc[0, 1],
        'kurs_teraz': df.iloc[-1, 1],
        'kurs_min': df.iloc[:, 1].min(),
        'kurs_min_date': df.iloc[df.iloc[:, 1].idxmin(), 0],
        'kurs_max': df.iloc[:, 1].max(),
        'kurs_max_date': df.iloc[df.iloc[:, 1].idxmax(), 0],
        'last_week_avg': round(df.iloc[:, 1].rolling(window=5).mean().iloc[-1], 2),
        'change_alltime': round((df.iloc[-1, 1] - df.iloc[0, 1]) / df.iloc[0, 1] * 100, 2),
        'change_1_week': round((df.iloc[-1, 1] - df.iloc[-5 , 1]) / df.iloc[-5, 1] * 100, 2),
        'change_1_month': round((df.iloc[-1, 1] - df.iloc[-20 , 1]) / df.iloc[-20, 1] * 100, 2),
    }

    final_df = pd.concat([final_df, pd.DataFrame([new_row])], ignore_index=True)

print(final_df)