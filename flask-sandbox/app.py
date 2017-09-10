from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    url_news = 'http://www.rotoworld.com/playernews/nfl/football-player-news'
    req_news = requests.get(url_news)
    soup_news = BeautifulSoup(req_news.content, "html.parser")
    news_raw = soup_news.find_all('div', {'class': ['report', 'impact']})[1:]
    news = [news.text for news in news_raw]
    return render_template('index.html', news=news)


@app.route('/headlines')
def headlines():
    url_hl = 'http://www.rotoworld.com/headlines/nfl/0/Football-headlines'
    req_hl = requests.get(url_hl)
    soup_hl = BeautifulSoup(req_hl.content, "html.parser")
    headlines_raw = soup_hl.find_all('div', {'class': 'news'})[1]
    headlines = headlines_raw.find('ul')
    return render_template('headlines.html', headlines=headlines)


@app.route('/rankings')
def rankings():
    url_cbs = 'https://www.cbssports.com/fantasy/football/rankings/standard/flex/'
    req_cbs = requests.get(url_cbs)
    soup_cbs = BeautifulSoup(req_cbs.content, "html.parser")
    cbs_raw = soup_cbs.find_all('span', {'class': 'player-name'})
    players = []
    for rank, player in enumerate(cbs_raw):
        if rank < 150:
            players.append(player.text)
    return render_template('cbs_rankings.html', players=players)


if __name__ == '__main__':
    app.run(debug=True)