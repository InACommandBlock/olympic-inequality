class PopulationData:
    def __init__(self, by_year, by_country):
        self.by_year = by_year
        self.by_country = by_country


def read():
    import csv

    by_year = {}
    by_country = {}

    with open("../data/population.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            country = row["Reference area"]
            year = int(row["TIME_PERIOD"])
            value = row["OBS_VALUE"]

            for_year = by_year.get(year, {})
            for_year[country] = value
            by_year[year] = for_year

            for_country = by_country.get(country, {})
            for_country[year] = value
            by_country[country] = for_country

    return PopulationData(by_year, by_country)


if __name__ == '__main__':
    population = read()
    print(f"In 1988, UK had {population.by_year[1988]['United Kingdom']}")
    print(f"In 2005, Netherlands had {population.by_year[2005]['Netherlands']}")
    print(f"In 2025, Mexico had {population.by_country['Mexico'][2025]}")
    print(f"In 1963, Korea had {population.by_country['Korea'][1963]}")

    print("All included countries:")
    countries = [country for country in population.by_country]
    countries.sort()
    for country in countries:
        print(f"  {country}")
