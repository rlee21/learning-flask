import requests
from bs4 import BeautifulSoup


url_news = 'http://www.rotoworld.com/playernews/nfl/football-player-news'
req_news = requests.get(url_news)
soup_news = BeautifulSoup(req_news.content, "html.parser")
news_raw = soup_news.find_all('div', {'class': ['report', 'impact']})[1:]
news = [news.text for news in news_raw]
for new in news:
    print(new)

