import requests
from bs4 import BeautifulSoup

url_hl = 'http://www.rotoworld.com/headlines/nfl/0/Football-headlines'
req_hl = requests.get(url_hl)
soup_hl = BeautifulSoup(req_hl.content, "html.parser")
headlines_raw = soup_hl.find_all('div', {'class': 'news'})[1]
headlines = headlines_raw.find('ul')
print(headlines.text)
# for i in headlines:
#     # data = i.find('a')['href']
#     print(i)
