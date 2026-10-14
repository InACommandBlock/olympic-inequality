class MedalData:
    def __init__(self, by_country, by_year):
        self.by_country = by_country
        self.by_year = by_year

class Medal:
  def __init__(self, rank, year, country, games, sport, event_gender, event_name):
    self.rank = rank
    self.year = year
    self.country = country
    self.games = games
    self.sport = sport
    self.event_gender = event_gender
    self.event_name = event_name

def read():
    import csv

    by_year = {}
    by_country = {}

    with open('../data/olympic_medalists.csv', 'r', newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            year = row['year']
            rank = row['medal']
            country = row['country']
            games = row['games']
            sport = row['sport']
            event_gender = row['event_gender']
            event_name = row['event_name']

            if None in [year, rank, country, games, sport, event_gender, event_name]:
                print("Skipping!")
                continue

            medal = Medal(rank, year, country, games, sport, event_gender, event_name)

            for_year = by_year.get(year, {})
            for_year[country] = medal
            by_year[year] = for_year

            for_country = by_country.get(country, {})
            for_country[year] = medal
            by_country[country] = for_country

    return MedalData(by_country, by_year)

if __name__ == '__main__':
    data = read()
    # ... test here
