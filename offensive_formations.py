# Before we move on, you should install 1 new: keyring. Just do as when you installed requests and BeautifulSoup4
# This script doesn't display the team names anymore. Neither displays the information for both teams. I believe it makes the whole thing more focused.
# You'll be prompted for your username and password, they'll be stored in your machine (that's what the keyring module does). I need to create a GLB2 session so we can download the JSON with the entire offensive playbook, which we use to find out the kinds of plays and the nº of receivers. Let me know if you run into troubles with this module since I never used it previously.
# Instead of editing the code, now you'll be prompted to insert the Game ID and the Team ID of the team you want to scout afterwards.
# If you're feeling adventurous, you can look for a dictionary called yards. There you can customize what the script will consider as Very Short, Short, Medium and Long, just as in the Tactics section of GLB2
# Let's talk about improvements: This script is at least 8 times faster than the previous version. It displays only the valid information, so no more 0 (0%). It sorts all results in an order I consider pleasant to the eye. It shows percentages for the receivers considering the down, which may be great for you to decide your blitzes.
# Hope you enjoy, now let me sleep.

import getpass
import keyring # pip3 install keyring
import re

#Checking/Prompting for username/password

user_name = keyring.get_password('glb2', 'user_name')
password = keyring.get_password('glb2', 'password')
if user_name is None:
	user_name = input('Your GLB2 Username: ')
	keyring.set_password('glb2', 'user_name', user_name)
if password is None:
	password = getpass.getpass('Your GLB2 Password: ')
	keyring.set_password('glb2', 'password', password)

login = {'action': 'login','user_name': user_name,'password': password}

# Grabs the whole defensive playbook:

import requests # pip3 install requests
import json

team_of_interest = input('''Insert your Team ID: ''')

with requests.Session() as c:
	c.post('http://glb2.warriorgeneral.com/game/login', data=login)
	r = c.get('http://glb2.warriorgeneral.com/game/playbook/O/ajax').content
	y = c.get('http://glb2.warriorgeneral.com/game/team/{}/games/'.format(team_of_interest), params={'type':'json', 'season':'31'}).content

offensive_playbook = json.loads(r.decode('utf-8'))

from bs4 import BeautifulSoup as bs

soup = bs(y, 'lxml')

completed_games = [link.get('href')[11:] for link in soup.select('td.list_score a') if re.match('/game/game/\d+',link.get('href'))]

def perc(kind, total):
	if total == 0 or kind == 0:
		return '0'
	else:
		return '{0}%'.format(int((kind * 100) / total))
		
def play_time(game_id):
	stats = {}
	global team_of_interest
	#game_id = ['67241', '66231', '67721', '66161', '65667', '65703'] #Air Raid
	#game_id = ['61900', '66231', '66355', '65304', '64206'] #Sunday Funday
	#game_id = ['67422', '66384', '65334', '64234', '66161'] #Lost Lounge
	#game_id = ['67424', '58704', '58708', '66380', '65325', '64234', '63051', '61930', '67210', '61656', '61364', '61262', '61171'] #Atlantic City Hookers
	#game_id = ['60726', '67532']
	for game in game_id:
		try:
			p_b_p = requests.get('http://glb2.warriorgeneral.com/game/game/{0}/json?type=pbp'.format(game)).content
			play_by_play = json.loads(p_b_p.decode('utf-8'))
			pbp = [play for play in play_by_play.values() if play["offense"] == team_of_interest and play["down"] in ['1', '2', '3']]
		except:
			continue
		for play_range in range(len(pbp) - 1):
			play = pbp[play_range]
			try:
				offense_play = offensive_playbook[play['offense_play']]
				off_name = offense_play['name']
				formation = offense_play['formation']
			except:
				continue
			if formation in stats:
				if off_name in stats[formation]:
					stats[formation][off_name]+=1
				else:
					stats[formation][off_name] = 1
			else:
				stats[formation] = {off_name: 1}
	return stats

def the_printer(play_dict):
	for formation in play_dict.keys():
		print(formation)
		for off_name in [i[0] for i in sorted(play_dict[formation].items(), key=lambda l: l[1], reverse=True)]:
			print('\t\t{0}: {1}'.format(off_name, play_dict[formation][off_name]))
		print()

#game_id = input('Insert the Game ID here: ')
#game_id = game_id.split(',')
		
the_printer(play_time(completed_games))

