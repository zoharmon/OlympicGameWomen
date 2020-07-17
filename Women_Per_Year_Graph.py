import pandas as pd

all_women = pd.read_csv("data_bases/all_women_athletes.csv")
id_and_game = []
for index, row in all_women.iterrows():
    id_and_game.append(str(row['ID']) + ' ' + row['Games'])

#reduce duplicate participants
id_and_game = set(id_and_game)

olympicGames = pd.read_csv("data_bases/OlympicGames.csv")

num_of_women_per_year = {}
for index, row in olympicGames.iterrows():
    season = 'Summer' if row['Season'] == 'S' else 'Winter'
    num_of_women_per_year[row['Name']+' '+ str(row['Year']) + ' ' + season] = 0

for item in id_and_game:
    game = item.split(' ')
    game = game[1:]
    game = ' '.join(game)
    for key in num_of_women_per_year.keys():
        if game in key:
            num_of_women_per_year[key] += 1



with open('data_bases/Graph_Women_Per_Game.csv','w+') as file:
    file.write("%s,%s\n" % ('Game', 'NumOfWomen'))
    for res in num_of_women_per_year:
        file.write("%s,%s\n" % (res, num_of_women_per_year[res]))