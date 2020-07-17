import pandas as pd
import collections

womenSummer = pd.read_csv("data_bases/women_winner_summer.csv", encoding='latin-1')

for column in womenSummer:
    if column == 'Location':
        countriesList = (list(womenSummer[column]))

countriesList = (set(countriesList))

countriesListDictionary = dict((x, 0) for x in countriesList)


for index, row in womenSummer.iterrows():
        countriesListDictionary[row['Location']] += 1

with open('countMedalsPerCountry.csv', 'w') as f:
    f.write("%s,%s\n" % ('Country', 'Count'))
    for key in countriesListDictionary.keys():
        f.write("%s,%s\n"%(key,countriesListDictionary[key]))