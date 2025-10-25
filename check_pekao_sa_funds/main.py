import pandas as pd
import requests
from io import StringIO

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

fund_ids = {
    "Pekao Akcji - Aktywna Selekcja": 12,
    "Pekao Zrównoważony": 9,
    "Pekao Strategii Globalnej - Stabilnego Wzrostu": 29,
    "Pekao Konserwatywny": 1,
    "Pekao Spokojna Inwestycja": 14,
    "Pekao Obligacji Plus": 4,
}

final_df = pd.DataFrame(
    columns=[
        "fundusz",
        "kurs_start",
        "kurs_teraz",
        "kurs_min",
        "kurs_min_date",
        "kurs_max",
        "kurs_max_date",
        "last_week_avg",
        "change_alltime",
        "change_1_week",
        "change_1_month",
    ]
)

for i in fund_ids:

    download_url = f"https://pekaotfi.pl/pobierz/fund?funds={fund_ids[i]}&type=csv"
    response = requests.get(download_url)
    source_csv = response.text
    df = pd.read_csv(
        StringIO(source_csv), sep=None, decimal=",", skiprows=1, engine="python"
    )
    df["Data"] = pd.to_datetime(df["Data"], format="%Y-%m-%d")
    df = df[df["Data"] >= "2025-10-20"].reset_index(drop=True)

    new_row = {
        "fundusz": i,
        "kurs_start": df.iloc[0, 1],
        "kurs_teraz": df.iloc[-1, 1],
        "kurs_min": df.iloc[:, 1].min(),
        "kurs_min_date": df.iloc[df.iloc[:, 1].idxmin(), 0].strftime("%Y-%m-%d"),
        "kurs_max": df.iloc[:, 1].max(),
        "kurs_max_date": df.iloc[df.iloc[:, 1].idxmax(), 0].strftime("%Y-%m-%d"),
        "last_week_avg": round(df.iloc[:, 1].rolling(window=5).mean().iloc[-1], 2),
        "change_1_week": round((df.iloc[-1, 1] - df.iloc[-5 , 1]) / df.iloc[-5, 1] * 100, 2),
        "change_1_month": round((df.iloc[-1, 1] - df.iloc[-20 , 1]) / df.iloc[-20, 1] * 100, 2),
    }

    final_df = pd.concat([final_df, pd.DataFrame([new_row])], ignore_index=True)

print(final_df)
