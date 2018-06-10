import requests
from bs4 import BeautifulSoup as bs

login = {
	'action': 'login',
	'user_name':'kaiijy',
	'password':'B)6s@VJDA'
}

with requests.Session() as c:
	c.post('http://glb2.warriorgeneral.com/game/login', data=login)
	r = c.get('http://glb2.warriorgeneral.com/game/hof?season=3&type=off_data&position=WR&league_id=0&tier=All')
	soup = bs(r.content)
	
# print(soup.prettify())

prefix = 'http://glb2.warriorgeneral.com'

#print(soup.select('h1 > a:nth-of-type(1)'))
#print(soup.select('.rank_col + td > a:first-child'))

hof = soup.select('h1 > a:nth-of-type(1)') + soup.select('.rank_col + td > a:first-child')

clean_hof = {player.text: prefix + player.get('href') for player in hof}

# print(clean_hof)

test = bs(requests.get('http://glb2.warriorgeneral.com/game/player/11158/stats').content)
print(test)

#for k,v in clean_hof.items():
#	if k == 'End Zone':
#		player = bs(requests.get(v + '#player_skills').content).prettify()
#		print(player)
#		break
#	else:
#		continue


