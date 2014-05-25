# Before we move on, you should install 1 new module: keyring. Just do as when you installed requests and BeautifulSoup4
# This script doesn't display the team names anymore. Neither displays the information for both teams. I believe it makes the whole thing more focused.
# You'll be prompted for your username and password, they'll be stored in your machine (that's what the keyring module does). I need to create a GLB2 session so we can download the JSON with the entire offensive playbook, which we use to find out the kinds of plays and the nº of receivers. Let me know if you run into troubles with this module since I never used it previously.
# Instead of editing the code, now you'll be prompted to insert the Game ID and the Team ID of the team you want to scout afterwards.
# If you're feeling adventurous, you can look for a dictionary called yards. There you can customize what the script will consider as Very Short, Short, Medium and Long, just as in the Tactics section of GLB2
# Let's talk about improvements: This script is at least 8 times faster than the previous version. It displays only the valid information, so no more 0 (0%). It sorts all results in an order I consider pleasant to the eye. It shows percentages for the receivers considering the down, which may be great for you to decide your blitzes.
# Hope you enjoy, now let me sleep.

import getpass
import keyring # pip3 install keyring

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
import json # pip3 install json

with requests.Session() as c:
	c.post('http://glb2.warriorgeneral.com/game/login', data=login)
	r = c.get('http://glb2.warriorgeneral.com/game/playbook/O/ajax').content

playbook = json.loads(r.decode('utf-8'))

# Prompts for the Game ID, throws an error if it is not numerical.

game_id = input('Insert the Game ID here: ')
if not game_id.isdigit():
	raise Exception('A Game ID is only numbers. For example, the Game ID for http://glb2.warriorgeneral.com/game/game/54548 is only 54548')
	
# Collects the play-by-play information
pbp = requests.get('http://glb2.warriorgeneral.com/game/game/{0}/json?type=pbp'.format(game_id)).content
play_by_play = json.loads(pbp.decode('utf-8'))

# The Team of Interest section: where you pick the team you want to scout (after all, who tracks two teams before a match?)

team_ids = list(set((play["offense"] for play in play_by_play.values())))
team_of_interest = input('''Here are the Team IDs available: {0} and {1}
Insert the ID from the team you\'d like to scout: '''.format(team_ids[0], team_ids[1]))
if not team_of_interest in team_ids:
	raise Exception('You must pick ONE of the Team IDs.')

# Dictionary with each formation and their respective receivers

formations = {
	'I': 'Two Receivers',
	'Singleback': 'Three Receivers',
	'Shotgun 5WR': 'Five Receivers',
	'Big I': 'Two TEs (Big)',
	'Shotgun': 'Three Receivers',
	'Pro Set': 'Two Receivers',
	'Weak I': 'Two Receivers',
	'Strong I': 'Two Receivers',
	'Singleback Trips': 'Three Receivers',
	'Singleback Big': 'Two TEs (Big)',
	'Singleback Spread': 'Four Receivers',
	'Goal Line': 'Goal Line'
}

# Dictionary with each offensive play and their respective outcomes

plays = {
	'run_outside_qb': 'Outside Run',
	'run_outside_fb': 'Outside Run',
	'run_outside_hb': 'Outside Run',
	'run_inside_fb': 'Inside Run',
	'run_inside_qb': 'Inside Run',
	'run_inside_hb': 'Inside Run',
	'run_goalline': 'Inside Run',
	'pass_long': 'Pass',
	'pass_medium': 'Pass',
	'pass_screen': 'Pass',
	'pass_short': 'Pass',
	'pass_goalline': 'Pass'
}

# Empty dictionary we're going to fill with our scouting stats.

stats = {}

# Dictionary with designinations to what is Very Short, etc, according to the offensive tactics. You can customize this if you want (:

yards = {
	'Very Short': 3,
	'Short': 5,
	'Medium': 10,
	'Long': 15
}

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
		raise Exception('There\'s something wrong with the yards from this play')
		
# The filtering loop

the_play_list = [play for play in play_by_play.values() if play["offense"] == team_of_interest and play["down"] in ['1', '2', '3']]

# The loop

def play_loop(play_list):
	for play in play_list:
		try:
			down_to_go = '{0} & {1}'.format(play["down"], down_yards(play["to_go"]))
			in_da_playbook = playbook[play["offense_play"]]
			receivers = formations[in_da_playbook["formation"]]
			play_kind = plays[in_da_playbook["cat"]]
			if down_to_go in stats:
				if receivers in stats[down_to_go]:
					if play_kind in stats[down_to_go][receivers]:
						stats[down_to_go][receivers][play_kind]+=1
					else:
						stats[down_to_go][receivers][play_kind] = 1
				else:
					stats[down_to_go][receivers] = {play_kind: 1}
			else:
				stats[down_to_go] = {receivers: {play_kind: 1}}
		except:
			continue
			
# Sorting lists for print

sort_down_to_go = {'1 & Medium': 0, '1 & G': 1, '2 & Very Short': 2, '2 & Short': 3, '2 & Medium': 4, '2 & Long': 5, '2 & Very Long': 6, '2 & G': 7, '3 & Very Short': 8, '3 & Short': 9, '3 & Medium': 10, '3 & Long': 11, '3 & Very Long': 12, '3 & G': 13}
sort_receivers = {'Two Receivers': 0, 'Three Receivers': 1, 'Four Receivers': 2, 'Five Receivers': 3, 'Two TEs (Big)': 4, 'Goal Line': 5}
sort_play_kinds = {'Inside Run': 0, 'Outside Run': 1, 'Pass': 2}

# Function to calculate percentages

def perc(kind, total):
	if total == 0 or kind == 0:
		return '0'
	else:
		return '{0}%'.format(int((kind * 100) / total))
		
# Function to print the output

def print_plays(dict):
	for down_to_go in [i[0] for i in sorted([(x,sort_down_to_go[x]) for x in dict.keys()], key=lambda l: l[1])]:
		print(down_to_go)
		for receivers in [i[0] for i in sorted([(x,sort_receivers[x]) for x in dict[down_to_go].keys()], key=lambda l: l[1])]:
			total_downs = sum(sum([i for i in y.values()]) for y in dict[down_to_go].values())
			total_receivers = sum([i for i in dict[down_to_go][receivers].values()])
			print('\t%s [%s]' % (receivers, perc(total_receivers, total_downs)))
			for play_kinds in [i[0] for i in sorted([(x,sort_play_kinds[x]) for x in dict[down_to_go][receivers].keys()], key=lambda l: l[1])]:
				total_kinds = sum([i for i in dict[down_to_go][receivers].values()])
				print('\t\t%s: %s (%s)' % (play_kinds, dict[down_to_go][receivers][play_kinds], perc(dict[down_to_go][receivers][play_kinds], total_kinds)))
		print('\n')
	total_passes =  sum([sum([receiv["Pass"] for receiv in downs.values() if "Pass" in receiv]) for downs in dict.values()])
	total_in_rushes = sum([sum([receiv["Inside Run"] for receiv in downs.values() if "Inside Run" in receiv]) for downs in dict.values()])
	total_out_rushes = sum([sum([receiv["Outside Run"] for receiv in downs.values() if "Outside Run" in receiv]) for downs in dict.values()])
	print('Total Passes:', total_passes)
	print('Total Rushes:', total_in_rushes + total_out_rushes, 'Inside Runs =>', perc(total_in_rushes, total_in_rushes + total_out_rushes))

play_loop(the_play_list)
print('\n')
print_plays(stats)
