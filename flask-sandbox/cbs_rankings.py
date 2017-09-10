import requests
from bs4 import BeautifulSoup


url_cbs = 'https://www.cbssports.com/fantasy/football/rankings/standard/flex/'
req_cbs = requests.get(url_cbs)
soup_cbs = BeautifulSoup(req_cbs.content, "html.parser")
cbs_raw = soup_cbs.find_all('div', {'class': ['player-row', 'rank', 'player-name']})
# players = soup_cbs.find_all('span', {'class': 'player-name'})
# cbs_raw = soup_cbs.find_all('a')
# for rank, player in enumerate(players):
#     if rank < 150:
#         print("{rank}) {player}".format(rank=rank+1, player=player.text))
players = []
for rank, player in enumerate(cbs_raw):
    if rank < 150:
        players.append(player.text)
print(players)
# print(cbs_raw)
# cbs = [cbs.text for cbs in cbs_raw]
# for new in cbs:
#     print(new)

