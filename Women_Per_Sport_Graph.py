import pandas as pd

all_women = pd.read_csv("data_bases/all_women_athletes.csv")
id_and_sport = []
sport = []
for index, row in all_women.iterrows():
    id_and_sport.append(str(row['ID']) + ' ' + row['Sport'])
    sport.append(row['Sport'])

#reduce duplicate id
id_and_sport = set(id_and_sport)
sport = set(sport)

sport_dict = {}
for item in sport:
    sport_dict[item] = 0

for item in id_and_sport:
    item = item.split(' ')
    item = item[1:]
    item = ' '.join(item)
    sport_dict[item] += 1


with open('data_bases/Graph_Women_Per_Sport.csv','w+') as file:
    file.write("%s,%s\n" % ('Sport', 'NumOfWomen'))
    for res in sport_dict:
        file.write("%s,%s\n" % (res, sport_dict[res]))
