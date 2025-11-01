<a name="readme-top"></a>
# 👨‍💻 Built with

<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />

<!-- ABOUT THE PROJECT -->
# ℹ️ About The Project

This code tracks and analyzes the performance of various Pekao SA investment funds in Poland.

- [Pekao Akcji - Aktywna Selekcja](https://pekaotfi.pl/produkty/fundusze-inwestycyjne/pekao-akcji-aktywna-selekcja?currency=PLN)
- [Pekao Zrównoważony](https://pekaotfi.pl/produkty/fundusze-inwestycyjne/pekao-zrownowazony?currency=PLN)
- [Pekao Strategii Globalnej - Stabilnego Wzrostu](https://pekaotfi.pl/produkty/fundusze-inwestycyjne/pekao-strategii-globalnej-stabilnego-wzrostu?currency=PLN)
- [Pekao Konserwatywny](https://pekaotfi.pl/produkty/fundusze-inwestycyjne/pekao-konserwatywny?currency=PLN)
- [Pekao Spokojna Inwestycja](https://pekaotfi.pl/produkty/fundusze-inwestycyjne/pekao-spokojna-inwestycja?currency=PLN)
- [Pekao Obligacji Plus](https://pekaotfi.pl/produkty/fundusze-inwestycyjne/pekao-obligacji-plus?currency=PLN)

It downloads historical price data (from August 26, 2025 to today) via CSV from the Pekao TFI website and calculates key metrics for each fund:

- Starting and current prices (kurs_start, kurs_teraz)
- Min/max prices with dates (kurs_min, kurs_max and their dates)
- 5-day moving average (last_week_avg)
- Performance changes over the entire period, 1 week, and 1 month (change_alltime, change_1_week, change_1_month)

The results are compiled into a pandas DataFrame that provides a comprehensive overview of each fund's performance trends.

<img src="https://raw.githubusercontent.com/PKuziola/personal-scripts/refs/heads/main/check_pekao_sa_funds/img/img_1.png"/>

# ⚙️ Run locally

```
pip install pandas requests
python3 check_pekao_sa_funds/main.py
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