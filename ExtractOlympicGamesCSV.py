from bs4 import BeautifulSoup
import urllib.request

fp = urllib.request.urlopen("https://www.olympic.org/summer-games")
mybytes = fp.read()

htmlFile = mybytes.decode("utf8")
fp.close()
soup = BeautifulSoup(htmlFile,"html5lib")
summer_games = soup.findAll('li', attrs={'class': 'summergames'})
winter_games = soup.findAll('li', attrs={'class': 'wintergames'})


result = []

for game in summer_games:
    a = str(game)
    x = BeautifulSoup(a,"html5lib")
    for z in x.find_all('a', href=True):
        game = z['href']
        game = game[1:]
        game = game.split('-')
        year = game[-1]
        if int(year) > 2020:
            continue
        game = game[:-1]
        name = ' '.join(game)
        result.append({'Name': name, 'Year': year, 'Season': 'S'})

for game in winter_games:
    a = str(game)
    x = BeautifulSoup(a,"html5lib")
    for z in x.find_all('a', href=True):
        game = z['href']
        game = game[1:]
        game = game.split('-')
        year = game[-1]
        if int(year) > 2020:
            continue
        game = game[:-1]
        name = ' '.join(game)
        result.append({'Name': name, 'Year': year, 'Season': 'W'})


# Save result to csv file
with open('data_bases/OlympicGames.csv','w+') as file:
    file.write("%s,%s,%s\n" % ('Name', 'Year','Season'))
    for res in result:
        file.write("%s,%s,%s\n" % (res['Name'], res['Year'], res['Season']))

