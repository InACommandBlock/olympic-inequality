# Olympic Medalists -- A Contest Between Humans or Countries?


## Test & Run

If the CSV/XML files are still zip-compressed, please extract them directly below `data/`.
While the parsers use built-in modules, we use `matplotlib` and `numpy` for the generation of results. You can enter the virtual environment and run the code:
```ps
cd /src
./Scripts/Activate
py results.py
```

## The Guidelines

* Use [emojis](https://gitmoji.dev) for commits.
* Code is to be written in Python.
* Use comments!
* Data is stored compressed; please extract the files directly below `./data/`


## The Sources

| Data              | Source        | Format     | Years       | Notes                          |
| ----------------- | ------------- | ---------- | ----------- | ------------------------------ |
| Olympic Medals    | Kaggle.com    |  CSV       | 1896 - 2022 | Alice                          |
| GDP per Capita    | World Bank    |  XML       | 1960 - 2025 | Dennis                         |
| Population        | OECD          |  CSV       | 1961 - 2025 | Dominic                        |


[WorldBank.org](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD)

[Kaggle.com](https://www.kaggle.com/datasets/cahyaalkahfi/olympic-medalist-dataset-18962024)

[OECD.org](https://data-explorer.oecd.org/vis?lc=en&df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_POPULATION%40DF_POP_HIST&df%5Bag%5D=OECD.ELS.SAE&df%5Bvs%5D=1.0&dq=AUS..PS._T..&pd=2014,2024&to%5BTIME_PERIOD%5D=false)


## The Plan

1. Check the data.
2. Parse the data with Python.
3. Pretty graphs.
