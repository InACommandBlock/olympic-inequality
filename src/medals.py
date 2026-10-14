

import urllib.request

url = ' https://www.kaggle.com/api/v1/datasets/download/cahyaalkahfi/olympic-medalist-dataset-18962024'
ziel_pfad = './datasets/medals.csv'

urllib.request.urlretrieve(url, ziel_pfad)
print('Download abgeschlossen!')
