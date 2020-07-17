import unicodedata

from theguardianApiPython.theguardian import theguardian_content, theguardian_section
import pandas as pd


headers = {
    #"q": "\"Victoria Manalo Draves\"",
    "order-by": "relevance",
    "section": "sport",
    "page-size": 50
}
def strip_accents(text):
    return ''.join(char for char in
                   unicodedata.normalize('NFKD', text)
                   if unicodedata.category(char) != 'Mn')

def parse_name(name):
    array = name.split(',')
    array[0] = array[0].lower()
    a = list(reversed(array))
    return ' '.join(a)

def calculate_articles_graph(sport):
    all_athletes = pd.read_csv("data_bases/all_athletes.csv")

    name_and_sport = []
    for index, row in all_athletes.iterrows():
        if row['Sport'] == sport and row['NOC'] == 'USA':
            name_and_sport.append(str(row['Name']) + '|' + row['Sport'] + '|' + row['Sex'])

    name_and_sport = set(name_and_sport) #unic name sport ans sex
    articles = []
    for row in name_and_sport:
        name = row.split('|')[0].replace('.','')
        headers["q"] = name
        content = theguardian_content.Content(api='test', **headers)
        res = content.get_content_response()
        result = content.get_results(res)

        for item in result:
            newRow = {}
            newRow['Name'] = name.replace(',','')
            newRow['Sport'] = row.split('|')[1]
            newRow['Sex'] = row.split('|')[2]
            newRow['Url'] = item['webUrl']
            newRow['Title'] = item['webTitle'].replace(',','')
            newRow['Publish'] = item['webPublicationDate']
            newRow['Year'] = item['webPublicationDate'].split('-')[0]
            articles.append(newRow)


    with open('data_bases/Articles_'+ sport + '.csv','w+') as file:
        file.write("%s,%s,%s,%s,%s,%s,%s\n" % ('Name', 'Sport','Sex','Url','Title','Publication Date','Publication Year'))
        for res in articles:
            file.write("%s,%s,%s,%s,%s,%s,%s\n" % (res['Name'], res['Sport'],res['Sex'], res['Url'], strip_accents(res['Title']).replace('\u2010',' '), res['Publish'],res['Year']))




    years = [row['Year'] for row in articles]
    years = set(years)

    amountFMPerYear = []
    for year in years:
        articles_F = 0
        articles_M = 0
        amountF = []
        amountM = []

        for article in articles:
            if article['Year'] == year:
                if article['Sex'] == 'F':
                    articles_F +=1
                    amountF.append(article['Name'])
                else:
                    articles_M += 1
                    amountM.append(article['Name'])

        amountM = set(amountM)
        amountF = set(amountF)

        ratioF = articles_F / len(amountF) if not len(amountF) == 0 else 0
        ratioM = articles_M / len(amountM) if not len(amountM) == 0 else 0

        amountFMPerYear.append({'Year': year, 'RatioF': ratioF, 'RatioM':ratioM})

    with open('data_bases/Graph_ratio_F_vs_M_per_year'+ sport + '.csv','w+') as file:
        file.write("%s,%s,%s\n" % ('Year','RatioF','RatioM'))
        for row in amountFMPerYear:
            file.write("%s,%s,%s\n" % (row['Year'], row['RatioF'],row['RatioM']))



#calculate_articles_graph('Tennis')
print('Boxing')
calculate_articles_graph('Boxing')