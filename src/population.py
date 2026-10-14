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
            value = int(row["OBS_VALUE"].replace('.', ''))

            # ignore specific subsets
            if row["Sex"] != "Total":
                continue
            if row["Age"] != "Total":
                continue

            for_year = by_year.get(year, {})
            for_year[country] = value
            by_year[year] = for_year

            for_country = by_country.get(country, {})
            for_country[year] = value
            by_country[country] = for_country

    return PopulationData(by_year, by_country)


def verify_completeness(population):
    missing = 0

    for country in population.by_country:
        for year in range(1961, 2026):
            if year not in population.by_country[country]:
                print(f"{country} has no data for {year}")
                missing += 1

    print(f"Found {missing} missing values")

def all_countries(population):
    print("All included countries:")
    countries = [country for country in population.by_country]
    countries.sort()
    for country in countries:
        print(f"  {country}")

def test_examples(population):
    print(f"In 1988, UK had {population.by_year[1988]['United Kingdom']} people")
    print(f"In 2005, Netherlands had {population.by_year[2005]['Netherlands']} people")
    print(f"In 2025, Mexico had {population.by_country['Mexico'][2025]} people")
    print(f"In 1963, Korea had {population.by_country['Korea'][1963]} people")

def growths_by_decade(population):
    for decade in range(1970, 2025, 10):
        growth_by_country = {}
        for country in population.by_country:
            start = population.by_country[country][decade-9]
            end = population.by_country[country][decade]
            growth = (end - start) / start
            growth_by_country[country] = growth

        highest = (0.0, "None")
        lowest = (100.0, "None")
        for (country, growth) in growth_by_country.items():
            if growth > highest[0]:
                highest = (growth, country)
            if growth < lowest[0]:
                lowest = (growth, country)

        print(f"{decade-9} - {decade}")
        print(f"  Lowest: {lowest[1]} with {lowest[0]*100:.1f}%")
        print(f"  Highest: {highest[1]} with {highest[0]*100:.1f}%")

def rank_by_growth(population):
    growth_by_country = {}
    countries = []
    for country in population.by_country:
        start = population.by_country[country][1961]
        end = population.by_country[country][2025]
        growth = (end - start) / start
        growth_by_country[country] = growth

        # using insertion sort here cuz y !
        for i in range(len(countries)):
            c = countries[i]
            if growth > growth_by_country[c]:
                countries.insert(i, country)
                break
        else:
            countries.append(country)

    print("1961 - 2025")
    for country in countries:
        print(f"  {country} ~ {growth_by_country[country]*100:.1f}%")


if __name__ == '__main__':
    population = read()

    verify_completeness(population)
    test_examples(population)
    # all_countries(population)
    growths_by_decade(population)
    rank_by_growth(population)
