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

# Customize this!

define_success = {
	'QB Rush': 4,
	'Outside Run': 3,
	'Inside Run': 1,
	'Pass': 0
}

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

with requests.Session() as c:
	c.post('http://glb2.warriorgeneral.com/game/login', data=login)
	r = c.get('http://glb2.warriorgeneral.com/game/playbook/O/ajax').content
	w = c.get('http://glb2.warriorgeneral.com/game/playbook/D/ajax').content

offensive_playbook = json.loads(r.decode('utf-8'))
defensive_playbook = json.loads(w.decode('utf-8'))

play_formatting = {
	'run_outside_qb': 'Outside QB',
	'run_outside_fb': 'Outside Run',
	'run_outside_hb': 'Outside Run',
	'run_inside_fb': 'Inside Run',
	'run_inside_qb': 'Inside QB',
	'run_inside_hb': 'Inside Run',
	'run_goalline': 'GL Run',
	'pass_long': 'Pass',
	'pass_medium': 'Pass',
	'pass_screen': 'Pass',
	'pass_short': 'Pass',
	'pass_goalline': 'Pass'
}

formation_formatting = {
	'zone_Dime': 'Dime [Z]',
	'zone_Dime 3-2-6': 'Dime 3-2-6 [Z]',
	'man_5-2': '5-2 [M]',
	'man_Goal Line D': 'Goal Line D [M]',
	'zone_4-4': '4-4 [Z]',
	'man_Nickel 3-3-5': 'Nickel 3-3-5 [M]',
	'zone_Nickel': 'Nickel [Z]',
	'zone_4-4 Big': '4-4 Big [Z]',
	'man_3-4': '3-4 [M]',
	'man_Quarter': 'Quarter [M]',
	'man_Dime 3-2-6': 'Dime 3-2-6 [M]',
	'man_Nickel': 'Nickel [M]',
	'zone_3-4': '3-4 [Z]',
	'man_4-3': '4-3 [M]',
	'zone_4-3': '4-3 [Z]',
	'zone_Quarter': 'Quarter [Z]',
	'man_Dime': 'Dime [M]',
	'man_4-4': '4-4 [M]',
	'man_4-4 Big': '4-4 Big [M]',
	'zone_Nickel 3-3-5': 'Nickel 3-3-5 [Z]',
	'zone_5-2': '5-2 [Z]'
}

def perc(kind, total):
	if total == 0 or kind == 0:
		return '0'
	else:
		return '{0}%'.format(int((kind * 100) / total))
		
def play_time(pbp):
	stats = {}
	for play_range in range(len(pbp) - 1):
		play = pbp[play_range]
		try:
			offense_play = offensive_playbook[play['offense_play']]
			offense_name = offense_play['name']
			offense_formation = offense_play['formation']
			offense_cat = play_formatting[offense_play['cat']]
			defense_play = defensive_playbook[play['defense_play']]
			defense_name = defense_play['name']
			defense_cat = formation_formatting[defense_play['cat']]
		except:
			continue
		play_description = play['description']
		if offense_cat == 'Pass':
			if 'sacked QB' in play_description:
				success = 1
			else:
				pass_compile = re.match('(?!.*intercepted).*pass.*for a (\d+) yard (gain|loss)', play_description)
				if pass_compile:
					yardage = int(pass_compile.group(1))
					if pass_compile.group(2) == 'loss':
						success = 1
					else:
						success = 0
				elif 'scrambled' in play_description:
					scramble_compile = re.match('QB {\d+} scrambled for a (\d+) yard (gain|loss).*', play_description)
					yardage = int(scramble_compile.group(1))
					if scramble_compile.group(2) == 'loss':
						yardage = yardage * -1
					if yardage > define_success['Outside Run']:
						success = 0
					else:
						success = 1
				else:
					success = 1
		elif offense_cat in ['Inside Run', 'Outside Run']:
			run_compile = re.match('.*for a (\d+) yard (gain|loss)', play_description)
			if run_compile:
				yardage = int(run_compile.group(1))
				if run_compile.group(2) == 'loss':
					yardage = yardage * -1
				if yardage > define_success[offense_cat]:
					success = 0
				else:
					success = 1
		elif offense_cat is 'GL Run':
			gl_compile = re.match('.*(pitched|rushed|handed off).*for a (\d+) yard (gain|loss).*', play_description)
			if gl_compile:
				yardage = int(gl_compile.group(2))
				if gl_compile.group(3) == 'loss':
					yardage = yardage * -1
				if gl_compile.group(1) == 'pitched':
					gl_offense = 'Outside Run'
				elif gl_compile.group(1) == 'handed off':
					gl_offense = 'Inside Run'
				else:
					gl_offense = 'QB Rush'
				if yardage > define_success[gl_offense]:
					success = 0
				else:
					success = 1
		formation = '{0} % {1}'.format(defense_name, defense_cat)
		if offense_cat in stats:
			if offense_name in stats[offense_cat]:
				if formation in stats[offense_cat][offense_name]:
					stats[offense_cat][offense_name][formation][0]+=success
					stats[offense_cat][offense_name][formation][1]+=1
				else:
					stats[offense_cat][offense_name][formation] = [success, 1]
			else:
				stats[offense_cat][offense_name] = {formation: [success, 1]}
		else:
			try:
				stats[offense_cat] = {offense_name: {formation: [success, 1]}}
			except:
				print(offense_cat, offense_name, formation, play)
	return stats
# Prompts for the Game ID, throws an error if it is not numerical.

def the_printer(play_dict):
	for offense_play in play_dict.keys():
		print(offense_play)
		for offense_formation in play_dict[offense_play].keys():
			print('\t%s' % offense_formation)
			for defense_play in play_dict[offense_play][offense_formation].keys():
				the_success = play_dict[offense_play][offense_formation][defense_play][0]
				total = play_dict[offense_play][offense_formation][defense_play][1]
				print('\t\t{0}: {1} ({2})'.format(defense_play, the_success, perc(the_success, total)))
		print()

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
	
the_play_list = [play for play in play_by_play.values() if play["offense"] == team_of_interest and play["down"] in ['1', '2', '3']]

#for play in play_by_play.values():
#	try:
#		is_offense = offensive_playbook[play['offense_play']]
#	except:
#		continue
#	if play_formatting[is_offense['cat']] == 'Pass':
#		print(play['description'])
		
the_printer(play_time(the_play_list))

