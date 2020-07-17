import pandas as pd

#convert NOC to location
locations = pd.read_csv("data_bases/all_athletes_locations.csv")
countries_dict = {}
for index, row in locations.iterrows():
    countries_dict[row["NOC"]] = row["region"]

#convert NOC to location
locations = pd.read_csv("data_bases/summer_winter_locations.csv")
summer_winter_dict = {}
for index, row in locations.iterrows():
    summer_winter_dict[row["Code"]] = row["Country"]


def parse_name(name):
    array = name.split(',')
    array[0] = array[0].lower()
    a = list(reversed(array))
    return ' '.join(a)


def all_women_athletes():
    summer_olympic = pd.read_csv("data_bases/all_athletes.csv")
    result = []
    for index, row in summer_olympic.iterrows():
        if row['Sex'] == 'F':
            result.append(row)

    with open('data_bases/all_women_athletes.csv','w+') as file:
        file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % ('ID','Name','Sex','Age','Height','Weight','Team','Country','Games','Year','Season','City','Sport','Event','Medal'))
        for row in result:
            file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (
            row['ID'], row['Name'].replace(',',''),
            row['Sex'], row['Age'],
            row['Height'], row['Weight'],
            row['Team'].replace(',',''), countries_dict[row['NOC']],
            row['Games'], row['Year'], row['Season'].replace(',',''),
            row['City'].replace(',',''),
            row['Sport'].replace(',',''), row['Event'].replace(',',''), row['Medal']))


def all_women_winner_summer():
    summer_olympic = pd.read_csv("data_bases/summer_winners.csv")
    result = []
    for index, row in summer_olympic.iterrows():
        if row['Gender'] == 'Women':
            name = parse_name(row['Athlete'])
            row['Athlete'] = name
            result.append(row)

    with open('data_bases/women_winner_summer.csv','w+') as file:
        file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % ('Year','City','Sport','Discipline','Athlete','Location','Gender','Event','Medal'))
        for row in result:
            file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (
            row['Year'], row['City'].replace(',',''), row['Sport'].replace(',',''), row['Discipline'].replace(',',''), row['Athlete'].replace(',',''), countries_dict[row['Country']], row['Gender'], row['Event'].replace(',',''), row['Medal']))


def all_women_winner_winter():
    summer_olympic = pd.read_csv("data_bases/winter_winners.csv")
    result = []
    for index, row in summer_olympic.iterrows():
        if row['Gender'] == 'Women':
            name = parse_name(row['Athlete'])
            row['Athlete'] = name
            result.append(row)

    with open('data_bases/women_winner_winter.csv','w+') as file:
        file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % ('Year','City','Sport','Discipline','Athlete','Location','Gender','Event','Medal'))
        for row in result:
            file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (row['Year'], row['City'].replace(',',''), row['Sport'].replace(',',''), row['Discipline'].replace(',',''), row['Athlete'].replace(',',''), countries_dict[row['Country']], row['Gender'], row['Event'].replace(',',''), row['Medal']))


print('########  start create winner winter olympic games file ########')
all_women_winner_winter()
print('########  start create winner summer olympic games file ########')
all_women_winner_summer()
print('########  start create all women in olympic games file ########')
#all_women_athletes()
