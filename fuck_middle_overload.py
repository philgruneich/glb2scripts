import getpass
import keyring
import requests
import json
from bs4 import BeautifulSoup as bs
import re

stats = {}

# Login

user_name = keyring.get_password('glb2', 'user_name')
password = keyring.get_password('glb2', 'password')
if user_name is None:
	user_name = input('Your GLB2 Username: ')
	keyring.set_password('glb2', 'user_name', user_name)
if password is None:
	password = getpass.getpass('Your GLB2 Password: ')
	keyring.set_password('glb2', 'password', password)
login = {'action': 'login','user_name': user_name,'password': password}

# Prompt for Team

team_id = input('''Insert your Team ID: ''').split(',')
	
# Request AJAX

with requests.Session() as c:
		c.post('http://glb2.warriorgeneral.com/game/login', data=login)
		r = c.get('http://glb2.warriorgeneral.com/game/playbook/O/ajax').content
#		y = [c.get('http://glb2.warriorgeneral.com/game/team/{}/games/'.format(team), params={'type':'json', 'season':'4'}).content for team in team_id]

offensive_playbook = json.loads(r.decode('utf-8'))

# Function to calculate percentages

def perc(kind, total):
	if total == 0 or kind == 0:
		return 0
	else:
		return int((kind * 100) / total)

# Loop through matches and all that jazz

for team in team_id:
	with requests.Session() as c:
		team_soup = bs(c.get('http://glb2.warriorgeneral.com/game/team/{}/games/'.format(team), params={'type':'json', 'season':'31'}).content)
	game_ids = [link.get('href')[11:] for link in team_soup.select('td.list_score a') if re.match('/game/game/\d+', link.get('href'))]
	for game in game_ids:
		try:
			p_b_p = requests.get('http://glb2.warriorgeneral.com/game/game/{0}/json?type=pbp'.format(game)).content
			play_by_play = json.loads(p_b_p.decode('utf-8'))
			pbp = [play for play in play_by_play.values() if play["offense"] == team and play["down"] in ['1', '2', '3'] and play['defense_play'] == '270']
		except:
			continue
		for play_range in range(len(pbp) - 1):
			play = pbp[play_range]
			if play['offense_play'] in ['127', '162']:
				continue
			if re.match('pass_(long|medium|screen|short|goalline)', offensive_playbook[play['offense_play']]['cat']):
				offense_play = '{0} ({1})'.format(offensive_playbook[play['offense_play']]['name'], offensive_playbook[play['offense_play']]['formation'])
			else:
				continue
			if 'sacked QB' in play['description']:
				sacked = 1
			else:
				sacked = 0
			if offense_play in stats:
				stats[offense_play]['total']+=1
				stats[offense_play]['sacked']+=sacked
			else:
				stats[offense_play] = {'total': 1, 'sacked': sacked}
				
sorted_list = sorted([(x,perc(stats[x]['sacked'],stats[x]['total'])) for x in stats.keys()], key=lambda l: l[1])
for play in sorted_list:
	print('{0}: {1}/{2} ({3}%)'.format(play[0], stats[play[0]]['sacked'], stats[play[0]]['total'], play[1]))
