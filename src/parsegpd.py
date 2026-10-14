import xml.etree.ElementTree as ET 
from gdp import GDPData
import os

def parseGDPData():
    with open("../data/gdp.xml", "r", newline="", encoding="utf-8") as file:
        tree = ET.parse(file)
        root = tree.getroot()

        records = root.findall('record')

        gdp_list = []
    
        for record in records:

            country_key = None
            country = None
            year = None
            val = None


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
                        val = float(value) if value else None

            obj = GDPData(country_key,country,year,val)
            gdp_list.append(obj)

        return gdp_list

def read():
    return parseGDPData()


if __name__ == '__main__':
    gdp_table = read()
    if gdp_table:
        print(f"First record: {table[0].country} - Year: {table[0].year}, Value: {table[0].value}")



