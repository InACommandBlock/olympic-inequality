class GdpData:
    def __init__(self, by_country, by_year):
        self.by_country = by_country
        self.by_year = by_year

class GdpCell:
    def __init__(self, country_key, country, year, value):
        self.country_key = country_key
        self.country = country
        self.year = year
        self.value = value


def read():
    import xml.etree.ElementTree as ET

    gdp_list = []
    by_year = {}
    by_country = {}

    with open('../data/gdp_per_capita.xml', "r", newline="", encoding="utf-8") as file:
        tree = ET.parse(file)
        root = tree.getroot()
        data = root.find('data')
        if data is None:
            raise Exception("xml does not contain the expected structure")
        records = data.findall('record')
        for record in records:
            country_key = None
            country = None
            year = None
            value = None

            for field in record.findall('field'):
                name = field.get('name')
                key = field.get('key','')
                value = field.text.strip() if field.text else None
                match name:
                    case 'Country or Area':
                        country_key = key
                        country = value
                    case 'Year':
                        year = int(value) if value else None
                    case 'Value':
                        value = float(value) if value else None

            if None in [country, year, value]:
                # print(f"Skipping incomplete record: {country}-{year}-{value}")
                continue

            # add to the collectors
            obj = GdpCell(country_key,country,year,value)
            gdp_list.append(obj)

            for_year = by_year.get(year, {})
            for_year[country] = value
            by_year[year] = for_year

            for_country = by_country.get(country, {})
            for_country[year] = value
            by_country[country] = for_country

    return GdpData(by_country, by_year)


if __name__ == '__main__':
    table = read()
