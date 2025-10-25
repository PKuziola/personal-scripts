<a name="readme-top"></a>
# 👨‍💻 Built with

<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />

<!-- ABOUT THE PROJECT -->
# ℹ️ About The Project

This code tracks and analyzes the performance of four Goldman Sachs investment funds in Poland.

- [Goldman Sachs Krótkoterminowy Obligacji](https://www.gstfi.pl/fundusze-inwestycyjne/fundusze-krotkoterminowe-dluzne/goldman-sachs-krotkoterminowy-obligacji)
- [Goldman Sachs Akcji](https://www.gstfi.pl/fundusze-inwestycyjne/fundusze-akcji/goldman-sachs-akcji)
- [Goldman Sachs Zrównoważony](https://www.gstfi.pl/fundusze-inwestycyjne/fundusze-mieszane/goldman-sachs-zrownowazony)
- [Goldman Sachs Średnich i Małych Spółek](https://www.gstfi.pl/fundusze-inwestycyjne/fundusze-akcji/goldman-sachs-srednich-i-malych-spolek)

It downloads historical price data (from August 26, 2025 to today) via CSV from the Goldman Sachs TFI website and calculates key metrics for each fund:

- Starting and current prices (kurs_start, kurs_teraz)
- Min/max prices with dates (kurs_min, kurs_max and their dates)
- 5-day moving average (last_week_avg)
- Performance changes over the entire period, 1 week, and 1 month (change_alltime, change_1_week, change_1_month)

The results are compiled into a pandas DataFrame that provides a comprehensive overview of each fund's performance trends.

<img src="https://raw.githubusercontent.com/PKuziola/personal-scripts/refs/heads/main/check_goldman_sachs_funds/img/img_1.png"/>

# ⚙️ Run locally

```
pip install pandas requests
python3 check_goldman_sachs_funds/main.py
```

# 🌲 Project tree
```bash
.
├───img
│   └── img_1.png
├── license.txt
├── main.py
└── README.md

```

<!-- LICENSE -->
# 📄 License

Distributed under the MIT License. See `LICENSE.txt` for more information.