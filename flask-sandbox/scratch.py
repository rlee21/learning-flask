import requests
from bs4 import BeautifulSoup

# url = 'http://www.rotoworld.com/headlines/nfl/0/Football-headlines'
url = 'http://www.rotoworld.com/playernews/nfl/football-player-news'
r = requests.get(url)
# print("status code is {}".format(r.status_code))
# print("header is \n {}".format(r.headers))
# print(r.json())
soup = BeautifulSoup(r.content, "html.parser")
# print(soup)
headlines_raw = soup.find_all('div', {'class': ['report', 'impact']})
# headlines_raw = soup.find_all('div', {'class': 'news'})[1]
# print(type(headlines_raw))
headlines = headlines_raw[1:]
# print(headlines[1:3])
for headline in headlines:
    # data = headline.find('p').text
    # print(data)
    print(headline.text)
# print(ff_news.find('a')['href'])
# for headline in headlines:
    # if '/headlines/nfl/' in headline:
    #     print(headline)
    # print(headline)
# headlines2 = headlines.find_all('h2', 'FANTASY FOOTBALL HEADLINES')
# print(headlines2)
# for headline in headlines.find_all("a"):
#     print(headline)
# print(soup.prettify())
# print(soup.text())