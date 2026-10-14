
import csv
from pathlib import Path


class medal:   
  def __new__(self, number , type , year, country):
    self.nr: int =  number 
    self._type : str = type
    self.year : str = year 
    self.country : str = country 
    
    
  def number (self, number):
    
    filename: str = "olympic-inequality/data/olympic_medalists.csv"   
    with open(filename) as csv_file:
      reader = csv.reader(csv_file, delimiter=';')
      for zeile in reader:
        print(zeile['medal'])
    return self.number
  
  def type (self, type):
      
    filename: str = "olympic-inequality/data/olympic_medalists.csv"   
    with open(filename) as csv_file: 
      reader = csv.reader(csv_file, delimiter=';')
      for zeile in reader:
        print(zeile['medal'])     
      return self.type
  
  def type (self, year):  
    filename: str = "olympic-inequality/data/olympic_medalists.csv"   
    with open(filename) as csv_file:
          
      reader = csv.reader(csv_file, delimiter=';')
      for zeile in reader:
        print(zeile['medal'])
    return self.year
  def type (self, country):  
    filename: str = "olympic-inequality/data/olympic_medalists.csv"   
    with open(filename) as csv_file:
      
      reader = csv.reader(csv_file, delimiter=';')
      for zeile in reader:
        print(zeile['medal'])
    return self.country
