import datanews
import requests
from bs4 import BeautifulSoup


URL = 'https://www.foxnews.com/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
for h2 in soup.find_all('h2', {'class':'title'}):
    print(h2.string)

# position = 0
# articles = []
# article_find= "'"+"article story" +str(position)+"'"
# for position in range(1, 5):
#     check = ("'article story-"+str(position)+"'")
#     print (check)
#     results = soup.find('article', {'class': (check)})
#     title=soup.find('h2', {'class': 'title'}).string
#     articles.append(results)
#     articles.append(title)
# print(articles)
    

# full = soup.find('div', {'class': 'content'})
# results = soup.find('article', {'class':'article story-1'})
# print (results)
# article = soup.find_all('h2', {'class':'title'}).string

# for string in article:
#     articles.append(string)

# print(soup)


# import datanews
# datanews.api_key = 'your api key'

# response1 = datanews.headlines(q='us',source='foxnews.com',language=['en'])
# fox_news = response1['hits']
# print(fox_news[0]['title'])
# print(fox_news[1]['title'])
# print(fox_news[2]['title'])
# print(fox_news[3]['title'])
# print(fox_news[4]['title'])

# response1 = datanews.headlines(q='us', source='cnn.com', language=['en'])
# cnn_news = response1['hits']
# print(cnn_news[0]['title'])
# print(cnn_news[1]['title'])
# print(cnn_news[2]['title'])
# print(cnn_news[3]['title'])
# print(cnn_news[4]['title'])

# response1 = datanews.headlines(q='us', source='msnbc.com', language=['en'])
# msnbc_news = response1['hits']
# print(msnbc_news[0]['title'])
# print(msnbc_news[1]['title'])
# print(msnbc_news[2]['title'])
# print(msnbc_news[3]['title'])
# print(msnbc_news[4]['title'])

# response1 = datanews.headlines(q='us', source='dailywire.com', language=['en'])
# dailywire_news = response1['hits']
# print(dailywire_news[0]['title'])
# print(dailywire_news[1]['title'])
# print(dailywire_news[2]['title'])
# print(dailywire_news[3]['title'])
# print(dailywire_news[4]['title'])

# response1 = datanews.headlines(q='us', source='usatoday.com', language=['en'])
# usatoday_news = response1['hits']
# print(usatoday_news[0]['title'])
# print(usatoday_news[1]['title'])
# print(usatoday_news[2]['title'])
# print(usatoday_news[3]['title'])
# print(usatoday_news[4]['title'])




