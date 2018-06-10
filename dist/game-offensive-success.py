# Import all modules!

import getpass
import keyring
import re
import requests
import json
from bs4 import BeautifulSoup as bs

# Define how many yards define a success.
# Any tactic that worked below that is considered a success.

define_success = {
    'QB Rush': 4,
    'Outside Run': 4,
    'Inside Run': 4,
    'Pass': 0
}

# Modify for current season

season = 32

if isinstance(season, int):
    season = str(season)

# Checking/Prompting for username/password

user_name = keyring.get_password('glb2', 'user_name')
password = keyring.get_password('glb2', 'password')
if user_name is None:
    user_name = input('Your GLB2 Username: ')
    keyring.set_password('glb2', 'user_name', user_name)
if password is None:
    password = getpass.getpass('Your GLB2 Password: ')
    keyring.set_password('glb2', 'password', password)

login = {'action': 'login', 'user_name': user_name, 'password': password}

# Prompts for a team ID

game_id = input('Insert the Game ID here: ')

if not game_id.isdigit():
    raise Exception('A Game ID is only numbers. For example, the Game ID for http://glb2.warriorgeneral.com/game/game/54548 is only 54548')

# team_of_interest = input('''Insert your Team ID (use commas for more than one): ''')

# teams_of_interest = [team.strip() for team in team_of_interest.split(',')]

# Log in and grab the playbooks

with requests.Session() as c:
    c.post('http://glb2.warriorgeneral.com/game/login', data=login)
    r = c.get('http://glb2.warriorgeneral.com/game/playbook/O/ajax').content
    w = c.get('http://glb2.warriorgeneral.com/game/playbook/D/ajax').content
    pbp = c.get('http://glb2.warriorgeneral.com/game/game/{0}/json?type=pbp'.format(game_id)).content

offensive_playbook = json.loads(r.decode('utf-8'))
defensive_playbook = json.loads(w.decode('utf-8'))
play_by_play = json.loads(pbp.decode('utf-8'))

team_ids = list(set((play["offense"] for play in play_by_play.values())))
team_of_interest = input('''Here are the Team IDs available: {0} and {1}
Insert the ID from the team you\'d like to scout: '''.format(team_ids[0], team_ids[1]))
if not team_of_interest in team_ids:
    raise Exception('You must pick ONE of the Team IDs.')

the_play_list = [play for play in play_by_play.values() if play["offense"] == team_of_interest and play["down"] in ['1', '2', '3']]

# A pause for some data dictionaries

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

# Function to create percentages


def perc(kind, total):
    if total == 0 or kind == 0:
        return '0'
    else:
        return '{0}%'.format(int((kind * 100) / total))


def play_time(pbp):
    stats = {}
    global teams_of_interest
    for play_range in range(len(pbp) - 1):
        play = pbp[play_range]
        try:
            offense_play = offensive_playbook[play['offense_play']]
            offense_name = offense_play['name']
            offense_formation = offense_play['formation']
            offense_cat = play_formatting[offense_play['cat']]
            # defense_play = defensive_playbook[play['defense_play']]
            # defense_name = defense_play['name']
            # defense_cat = formation_formatting[defense_play['cat']]
        except:
            continue
        play_description = play['description']

        # Working on pass offensive

        if offense_cat == 'Pass':

            # Automatically passes sacks as failure

            if 'sacked QB' in play_description:
                success = 0
            else:
                pass_compile = re.match('(?!.*intercepted).*pass.*for a (\d+) yard (gain|loss)', play_description)

                if pass_compile:
                    yardage = int(pass_compile.group(1))

                    if pass_compile.group(2) == 'loss':
                        success = 0
                    else:
                        success = 1

                # Checks for scramble plays

                elif 'scrambled' in play_description:
                    scramble_compile = re.match('QB {\d+} scrambled(, who went out of bounds)? for a (\d+) yard (gain|loss).*', play_description)
                    yardage = int(scramble_compile.group(2))

                    if scramble_compile.group(3) == 'loss':
                        yardage = yardage * -1

                    if yardage < define_success['Outside Run']:
                        success = 0
                    else:
                        success = 1
                else:
                    success = 0

        # Checking out run plays

        elif offense_cat in ['Inside Run', 'Outside Run']:

            run_compile = re.match('.*for a (\d+) yard (gain|loss)', play_description)

            if run_compile:
                yardage = int(run_compile.group(1))

                if run_compile.group(2) == 'loss':
                    yardage = yardage * -1

                if yardage < define_success[offense_cat]:
                    success = 0
                else:
                    success = 1

        # Looking for Goal Line formations

        else:

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

                if yardage < define_success[gl_offense]:
                    success = 0
                else:
                    success = 1

        offense_fullname = '{0} ({1})'.format(offense_name, offense_formation)
        if offense_fullname in stats:
            stats[offense_fullname][0] += success
            stats[offense_fullname][1] += 1
        else:
            stats[offense_fullname] = [success, 1]
    return stats


def printer(play_dict):

    offenses = [{"name": offense, "success": play_dict[offense][0], "total": play_dict[offense][1]} for offense in play_dict.keys()]

    offenses = sorted(offenses, key=lambda k: k['total'], reverse=True)

    for offense in offenses:
        name = offense['name']
        success = offense['success']
        total = offense['total']
        print("{0}: {1}/{2} ({3})".format(name, success, total, perc(success, total)))
    print()

printer(play_time(the_play_list))
# printer(play_time([['542992']]))
