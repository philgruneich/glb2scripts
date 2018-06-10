import requests
import json
from bs4 import BeautifulSoup as bs

data = requests.get('http://glb2.warriorgeneral.com/game/game/52751/pbp') # Insert the play-by-play direct link here.
home_team = False # True if the team you want to track is the HOME team, False otherwise
team_of_interest_id = '344' # Insert the ID of the team you want to track here

soup = bs(data.content)
replay_links = soup.select('tr.pbp_play_row a')
da_replays = ['http://glb2.warriorgeneral.com' + the_link.get('href') + '/1' for the_link in replay_links]

def defense_tactic(rec):
	if rec[1] == 2:
		return 'Two TEs'
	elif rec[0] == 2:
		return 'Two Receivers'
	elif rec[0] == 3:
		return 'Three Receivers'
	elif rec[0] == 4:
		return 'Four Receivers'
	elif rec[0] == 5:
		return 'Five Receivers'

def play_kind(play):
	if 'rushed' in desc:
		return 'QB Rush'
	elif 'handed' in desc:
		return 'Run Inside'
	elif 'pitched' in desc:
		return 'Run Outside'
	else:
		return 'Pass'

stats = {
	'Two Receivers': 
		{'QB Rush': 0, 'Run Outside': 0, 'Run Inside': 0, 'Pass': 0},
	'Three Receivers':
		{'QB Rush': 0, 'Run Outside': 0, 'Run Inside': 0, 'Pass': 0},
	'Four Receivers':
		{'QB Rush': 0, 'Run Outside': 0, 'Run Inside': 0, 'Pass': 0},
	'Five Receivers':
		{'QB Rush': 0, 'Run Outside': 0, 'Run Inside': 0, 'Pass': 0},
	'Two TEs':
		{'QB Rush': 0, 'Run Outside': 0, 'Run Inside': 0, 'Pass': 0}
}

for replay in da_replays:
	data_replay = requests.post(replay)
	data_table = json.loads(data_replay.content.decode('latin-1'))
	players_round = []
	if team_of_interest_id != data_table['offense_id']:
		continue
	for player in data_table['players'].keys():
		try:
			homie = data_table['players'][player]['home']
			if home_team is True:
				players_round.append(data_table['players'][player]['pos'])
		except:
			if home_team is False:
				players_round.append(data_table['players'][player]['pos'])
	WRs = len([pos for pos in players_round if pos.startswith('WR')])
	TEs = len([pos for pos in players_round if pos.startswith('TE')])
	receivers = (WRs, TEs)
	desc = data_table['description']
	if receivers == (0, 0) or 'attempted' in desc or 'took a knee' in desc or receivers[0] < 2 or 'spiked' in desc:
		continue
	else:
#		print(receivers, desc)
#		print(play_kind(desc))
#		print(defense_tactic(receivers))
#		print('-----')
		kind = play_kind(desc)
		receivs = defense_tactic(receivers)
		stats[receivs][kind]+=1
		
for key in stats.keys():
	print('''{0}
		QB Rush: {1}
		Run Outside: {2}
		Run Inside: {3}
		Pass: {4}
		Total Plays: {5}
		'''.format(key, stats[key]['QB Rush'], stats[key]['Run Outside'], stats[key]['Run Inside'], stats[key]['Pass'], sum(stats[key].values())))