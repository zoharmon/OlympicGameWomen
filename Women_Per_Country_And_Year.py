# 1 Norway
# 19 USA
# 64 Moldova
# 98 Brazil
# 154 Somalia
# 76 China
# 6 Austria
# 29 Japan
# 133 India
import pandas as pd
countries = ['USA', 'Norway', 'Somalia', 'Brazil', 'Moldova', 'China', 'Austria','Japan', 'India']

all_women = pd.read_csv("data_bases/all_women_athletes.csv")

def getCountryList(country):
    womenCountry = []
    for index, row in all_women.iterrows():
        if row['Country'] == country:
            womenCountry.append(row)

    return womenCountry


def countWomenPerYear(countryList):
    id_and_game = []
    for row in countryList:
        id_and_game.append(str(row['ID']) + ' ' + row['Games'])

    # reduce duplicate participants
    id_and_game = set(id_and_game)

    olympicGames = pd.read_csv("data_bases/OlympicGames.csv")

    num_of_women_per_year = {}
    for index, row in olympicGames.iterrows():
        season = 'Summer' if row['Season'] == 'S' else 'Winter'
        num_of_women_per_year[row['Name'] + ' ' + str(row['Year']) + ' ' + season] = 0

    for item in id_and_game:
        game = item.split(' ')
        game = game[1:]
        game = ' '.join(game)
        for key in num_of_women_per_year.keys():
            if game in key:
                num_of_women_per_year[key] += 1

    return num_of_women_per_year


def exportCSV(countryName, countryList):
    'data_bases/' + countryName + '.csv'
    with open('data_bases/' + countryName + '.csv','w+') as file:
        file.write("%s,%s\n" % ('Game', 'NumOfWomen'))
        for res in countryList:
            file.write("%s,%s\n" % (res, countryList[res]))


for country in countries:
    exportCSV(country,countWomenPerYear(getCountryList(country)))