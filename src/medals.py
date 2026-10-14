class Medal:
  def __init__(self, rank:str, year:int, country:str, games:str, sport:str, event_gender:str, event_name:str):
    self.rank = rank
    self.year = year
    self.country = country
    self.games = games
    self.sport = sport
    self.event_gender = event_gender
    self.event_name = event_name

class MedalData:
    def __init__(self, by_country: dict[str, list[Medal]], by_year: dict[int, list[Medal]]):
        self.by_country = by_country
        self.by_year = by_year

def read():
    import csv

    by_year = {}
    by_country = {}

    with open('../data/olympic_medalists.csv', 'r', newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            year = int(row['year'])
            rank = row['medal']
            country = row['country_code']
            games = row['games']
            sport = row['sport']
            event_gender = row['event_gender']
            event_name = row['event_name']

            if None in [year, rank, country, games, sport, event_gender, event_name]:
                print("Skipping!")
                continue

            medal = Medal(rank, year, country, games, sport, event_gender, event_name)

            for_year = by_year.get(year, [])
            for_year.append(medal)
            by_year[year] = for_year

            for_country = by_country.get(country, [])
            for_country.append(medal)
            by_country[country] = for_country

    return MedalData(by_country, by_year)

if __name__ == '__main__':
    data = read()

    import random
    rand_year = random.choice([year for year in range(1896, 2026, 4)])
    print(f"Olympic Medalists in {rand_year}")
    for medal in data.by_year[rand_year]:
        print(f"  {medal.country}: {medal.rank} in {medal.sport} {medal.event_gender} {medal.event_name}")

    rand_country = random.choice([country for country in data.by_country])
    print(f"Olympic Medalists in {rand_country}")
    for medal in data.by_country[rand_country]:
        print(f"  {medal.country}: {medal.rank} in {medal.sport} {medal.event_gender} {medal.event_name}")
