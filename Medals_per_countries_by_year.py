import pandas as pd
import collections

def olympicGamesDBRange(start, end, step):
    while start <= end:
        yield start
        start += step

womenSummer = pd.read_csv("data_bases/women_winner_summer.csv", encoding='latin-1')
medalsPerCountries = pd.read_csv("data_bases/countMedalsPerCountry.csv")

for column in medalsPerCountries:
    if column == 'Country':
        countriesList = (list(medalsPerCountries[column]))

olympicYearsList = []

for x in olympicGamesDBRange(1900,2012,4):
    olympicYearsList.append(x)

# countriesDict = dict((country, 0) for country in countriesList)
# olympicYearsDicationary = dict((year, countriesDict) for year in olympicYearsList)
olympicYearsDicationary = dict((year, dict((country, 0) for country in countriesList)) for year in olympicYearsList)


for index, row in womenSummer.iterrows():
    olympicYearsDicationary[row['Year']][row['Location']] += 1


with open('medalsPerCountriesByYears.csv', 'w') as f:
    f.write("%s,%s,%s\n" % ('Year', 'Country', 'Count'))
    for year in olympicYearsList:
        for country in olympicYearsDicationary[year].keys():
            f.write("%s,%s,%s\n"%(year,country,olympicYearsDicationary[year][country]))