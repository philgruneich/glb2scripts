import requests
#import json
import ujson
from bs4 import BeautifulSoup as bs

game_id = 54562 #Change this value only

yards = {
	'Very Short': 3,
	'Short': 5,
	'Medium': 10,
	'Long': 15
}

# Create list of replay links

game_soup = bs(requests.get('http://glb2.warriorgeneral.com/game/game/{0}/pbp'.format(game_id)).content)
da_replays = ('http://glb2.warriorgeneral.com%s/1' % the_link.get('href') for the_link in game_soup.select('tr.pbp_play_row a'))

# Dictionary we gonna fill after every play.

home_team = {
	'1st': {
		'Two Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Three Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Four Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Two TE': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Goal Line': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0}
	},
	'1st & G': {
			'Two Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
			'Three Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
			'Four Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
			'Two TE': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
			'Goal Line': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0}
		},
	'2nd & Very Short': {
		'Two Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Three Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Four Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Two TE': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Goal Line': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0}
	},
	'2nd & Short': {
		'Two Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Three Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Four Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Two TE': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Goal Line': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0}
	},
	'2nd & Medium': {
		'Two Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Three Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Four Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Two TE': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Goal Line': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0}
	},
	'2nd & Long': {
		'Two Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Three Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Four Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Two TE': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Goal Line': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0}
	},
	'2nd & Very Long': {
		'Two Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Three Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Four Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Two TE': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Goal Line': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0}
	},
	'2nd & G': {
		'Two Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Three Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Four Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Two TE': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Goal Line': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0}
	},
	'3rd & Very Short': {
		'Two Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Three Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Four Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Two TE': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Goal Line': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0}
	},
	'3rd & Short': {
		'Two Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Three Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Four Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Two TE': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Goal Line': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0}
	},
	'3rd & Medium': {
		'Two Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Three Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Four Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Two TE': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Goal Line': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0}
	},
	'3rd & Long': {
		'Two Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Three Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Four Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Two TE': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Goal Line': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0}
	},
	'3rd & Very Long': {
		'Two Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Three Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Four Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Two TE': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Goal Line': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0}
	},
	'3rd & G': {
		'Two Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Three Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Four Receivers': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Two TE': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0},
		'Goal Line': {'Inside Run': 0, 'Outside Run': 0, 'Pass': 0}
	}
}
away_team = home_team

def play_kind(play):
	if 'handed off' in play:
		return 'Inside Run'
	elif 'pitched to' in play:
		return 'Outside Run'
	elif 'threw a pass' in play or 'forced a hurried pass' in play or 'sacked' in play:
		return 'Pass'
	else:
		return 'Other'
		
def down_yards(to_go):
	if to_go == 'G':
		return to_go
	elif to_go == 'inches' or 0 < int(to_go) <= yards['Very Short']:
		return 'Very Short'
	elif 0 < int(to_go) <= yards['Short']:
		return 'Short'
	elif 0 < int(to_go) <= yards['Medium']:
		return 'Medium'
	elif 0 < int(to_go) <= yards['Long']:
		return 'Long'
	elif 0 < int(to_go) > yards['Long']:
		return 'Very Long'
	else:
		return 'What the fuck?'
		
def receiver_check(rec):
	if isinstance(rec, tuple):
		if rec[0] == 2:
			return 'Two Receivers'
		elif rec[0] == 3:
			return 'Three Receivers'
		elif rec[0] == 4:
			return 'Four Receivers'
		elif rec[0] == 0:
			return 'Goal Line'
		elif rec[1] == 2:
			return 'Two TE'
		else:
			return 'Five Receivers'
			
versus = game_soup.select('.scoresInner .stat_left a')
home_team_name = versus[0].text
home_team_id = versus[0].get('href').replace('/game/team/','')
away_team_name = versus[1].text
away_team_id = versus[1].get('href').replace('/game/team/','')

for replay in da_replays:
#	if replay == da_replays[5]:
#		break
	data_replay = requests.get(replay)
	data_table = ujson.loads(data_replay.content.decode('latin-1'))
#	data_table = json.loads(data_replay.content.decode('latin-1'))
	# Checks for the kind of play, inside run, pass, etc. Skips otherwise.
	kind_play = play_kind(data_table['description'])
	if kind_play == 'Other':
		continue
	# Counts the number of WRs and TEs
	players_keys = data_table['players'].keys()
	rec = receiver_check((len([wr for wr in players_keys if data_table['players'][wr]['pos'].startswith('WR')]), len([te for te in players_keys if data_table['players'][te]['pos'].endswith('TE')])))
	if rec == 'Five Receivers':
#		print(kind_play)
		continue
	# Uncovers the down and distance of the play
	da_down = data_table['down']
	da_go = data_table['to_go']
	if da_down == '4th' or da_down == '0th':
		continue
	if da_down == '1st':
		if da_go == 'G':
			down_play = '1st & G'
		else:
			down_play = da_down
	else:
		down_play = '{0} & {1}'.format(da_down, down_yards(da_go))
	# Adds the number to the correct dictionary
	try:
		if data_table['offense_id'] == home_team_id:
			home_team[down_play][rec][kind_play]+=1
		else:
			away_team[down_play][rec][kind_play]+=1
	except KeyError:
		print(replay)
		print(da_down)
		
def perc(kind, total):
	if total == 0 or kind == 0:
		return '0'
	else:
		return '{0}%'.format(int((kind * 100) / total))

def print_team(team):
	for receivers in sorted(team.keys()):
		print('{0}:'.format(receivers))
		for kind in team[receivers].items():
			total = sum(kind[1].values())
			if total == 0:
				continue
			print('\t{0} => I: {1} ({2}); O: {3} ({4}); P: {5} ({6})'.format(kind[0], kind[1]['Inside Run'], perc(kind[1]['Inside Run'], total), kind[1]['Outside Run'], perc(kind[1]['Outside Run'], total), kind[1]['Pass'], perc(kind[1]['Pass'], total)))

print(home_team_name)
print_team(home_team)
print('---------')
print(away_team_name)
print_team(away_team)