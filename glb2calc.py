# -*- coding: UTF-8 -*-

from functools import reduce
from operator import mul

class glb2calc:
	def __init__(self, position, height, weight, trait1, trait2, trait3, strength=5, speed=5, agility=5, stamina=5, awareness=5, confidence=5):
		if stamina + strength + confidence + awareness + agility + speed < 35:
			print('You have {0} attribute points left.'.format(35 - (stamina + strength + confidence + awareness + agility + speed)))
		elif stamina + strength + confidence + awareness + agility + speed > 35:
			print('You have {0} points too many.'.format((stamina + strength + confidence + awareness + agility + speed) - 35))
		heights_help = {'56':66, '57':67, '58':68, '59':69, '510':70, '511':71, '60':72, '61':73, '62':74, '63':75, '64':76, '65':77, '66':78, '67':79, '68':80}
		# Checking for height
		if isinstance(height, str):
			height = heights_help[height]
		# Checking for weight
		if isinstance(weight, int):
			pass
		else:
			weight = int(weight)
		# Checking for traits
		traits_help = {'Unpr-edic-table': 'unpredictable', 'Blocking Back': 'hb_blocking_back', 'Solid Frame': 'qb_solid_frame', 'Nerves of Steel': 'nerves_of_steel', 'Speedster': 'wr_speedster', 'Ball Hawk': 'ball_hawk', 'Blitzer': 'lb_blitzer', 'Tactician': 'tactician', 'Dominator': 'wr_control', 'Man Specialist': 'man_specialist', 'Consistent Blocker': 'ol_consistent_blocker', 'Early Bloomer': 'early_bloomer', 'Run Stuffer': 'dl_run_stuffer', 'Technical Blocker': 'ol_tech_blocker', 'Sure Tackler': 'sure_tackler', 'Precision Passer': 'qb_precision_passer', 'Fearsome': 'fearsome', 'Long Reach': 'long_reach', 'Thick Skin': 'thick_skin', 'Coverage LB': 'lb_coverage', 'Quick Feet': 'quick_feet', 'Slippery': 'slippery', 'Shifty': 'wr_shifty', 'Slot Receiver': 'wr_slot_receiver', 'Pass Rusher': 'dl_pass_rusher', 'Slow Built': 'slow_built', 'Lead Blocker': 'fb_lead_blocker', 'Workhorse': 'workhorse', 'Middle Man': 'lb_middle_man', 'Power Rusher': 'hb_power_rusher', 'Quick Snap': 'c_quick_snap', 'Unpredictable': 'hb_unpredictable', 'Rusher': 'fb_rusher', 'Dread-nought': 'dl_dreadnought', 'Scrambler': 'qb_scrambler', 'D Anchor': 'd_anchor', 'Easy Going': 'easy_going', 'Elusive Rusher': 'hb_elusive_rusher', 'Superstar': 'superstar_nonglam', 'Technique Man': 'dl_technique_man', 'Sure Hands': 'p_sure_hands', 'Spring Board': 'spring_board', 'Cool Headed': 'k_cool_headed', 'Chase Down Artist': 'chasedown_artist', 'Zone Specialist': 'zone_specialist', 'Leg of Steel': 'k_leg_of_steel', 'Fumble Creator': 'fumble_creator', 'Heavy Weight': 'dl_heavyweight', 'Tenacious': 'tenacious', 'Broad Jumper': 'broad_jumper', 'Shutdown Defender': 'shutdown_defender', 'Power Blocker': 'ol_power_blocker', 'Downfield Blocker': 'g_downfield_blocker', 'Run Blocker': 'ol_run_blocker', 'High Jumper': 'high_jumper', 'Lightning Reflexes': 'lightning_reflexes', 'Jugger NOT': 'dl_juggernaut', 'Return Specialist': 'return_specialist', 'Strong Base': 'strong_base', 'Quick Reaction': 'dl_quick_reaction', 'Flex Coverage': 'flex_coverage', 'Blocking Specialist': 'te_blocker', 'Scat Back': 'hb_scat_back', 'Field General': 'qb_field_general', 'Bruiser': 'bruiser', 'Meathead': 'meathead', 'Soft Hands': 'soft_hands', 'Kickoff King': 'k_kickoff_king', 'Pass Blocker': 'ol_pass_blocker', 'Brick Wall': 'brick_wall', 'Dual Threat': 'qb_dual_threat', 'Towering Man': 'dl_towering_man', 'Crusher': 'dl_crusher', 'Active Hands': 'active_hands', 'Egotist': 'egotist', 'Receiving Specialist': 'te_receiver', 'Pass Protector': 'ot_pass_protector', 'Sharp Shooter': 'k_sharpshooter', 'Gunslinger': 'qb_gunslinger', 'QB Rusher': 'qb_rusher', 'FB Scat Back': 'fb_scat_back', 'HB Rusher': 'hb_rushing_back'}
		traits = {"dl_quick_reaction": {"skill_modifiers": {"tackle_awareness": {"cost": -0.05,"max": 3},"blitz_awareness": {"cost": -0.05,"max": 3},"tackle_technique": {"cost": -0.05,"max": 3}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "LB", "FS", "SS", "CB", "K", "P"],"salary_modifier": 0,"name": "Quick Reaction","description": "<p>This defender has a nose for the ball.</p>\n\t\t\t\t\t\tBlitz Awareness: 5% lower SP cost, +3 max<br>\n\t\t\t\t\t\tTackling Tech: 5% lower SP cost, +3 max<br>\n\t\t\t\t\t\tPursuit: 4% lower SP cost, +3 max<br>"},"active_hands": {"skill_modifiers": {"tackle_strip": {"cost": -0.05,"max": 3}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C"],"salary_modifier": 0,"name": "Active Hands","description": "Strip Tech: 5% lower SP cost, +3 max"},"early_bloomer": {"skill_modifiers": {"punt_power": {"cost": -0.05,"max": -10},"tackle_awareness": {"cost": -0.05,"max": -10},"tackle_strip": {"cost": -0.05,"max": -10},"run_block_awareness": {"cost": -0.05,"max": -10},"coverage_interception": {"cost": -0.05,"max": -10},"break_run_block": {"cost": -0.05,"max": -10},"pass_rush_power": {"cost": -0.05,"max": -10},"conditioning": {"cost": -0.05,"max": -10},"route_elusiveness": {"cost": -0.05,"max": -10},"return_awareness": {"cost": -0.05,"max": -10},"catch_consistency": {"cost": -0.05,"max": -10},"catch_grip": {"cost": -0.05,"max": -10},"catch_hands": {"cost": -0.05,"max": -10},"tackle_technique": {"cost": -0.05,"max": -10},"snap_reaction": {"cost": -0.05,"max": -10},"block_consistency": {"cost": -0.05,"max": -10},"man_coverage_awareness": {"cost": -0.05,"max": -10},"footwork": {"cost": -0.05,"max": -10},"pass_block_awareness": {"cost": -0.05,"max": -10},"pass_consistency": {"cost": -0.05,"max": -10},"intimidation": {"cost": -0.05,"max": -10},"diving": {"cost": -0.05,"max": -10},"punt_hands": {"cost": -0.05,"max": -10},"kick_consistency": {"cost": -0.05,"max": -10},"pass_evasiveness": {"cost": -0.05,"max": -10},"toughness": {"cost": -0.05,"max": -10},"pass_accuracy": {"cost": -0.05,"max": -10},"pass_rush_deflection": {"cost": -0.05,"max": -10},"pass_power": {"cost": -0.05,"max": -10},"zone_coverage_awareness": {"cost": -0.05,"max": -10},"kick_power": {"cost": -0.05,"max": -10},"quickness": {"cost": -0.05,"max": -10},"pass_technique": {"cost": -0.05,"max": -10},"vertical": {"cost": -0.05,"max": -10},"balance": {"cost": -0.05,"max": -10},"carry_awareness": {"cost": -0.05,"max": -10},"pass_carry_power": {"cost": -0.05,"max": -10},"punt_accuracy": {"cost": -0.05,"max": -10},"kickoff_power": {"cost": -0.05,"max": -10},"hold_ground": {"cost": -0.05,"max": -10},"pass_awareness": {"cost": -0.05,"max": -10},"route_technique": {"cost": -0.05,"max": -10},"punt_consistency": {"cost": -0.05,"max": -10},"blitz_awareness": {"cost": -0.05,"max": -10},"carry_power": {"cost": -0.05,"max": -10},"pass_block_power": {"cost": -0.05,"max": -10},"catch_awareness": {"cost": -0.05,"max": -10},"carry_grip": {"cost": -0.05,"max": -10},"kick_accuracy": {"cost": -0.05,"max": -10},"carry_elusiveness": {"cost": -0.05,"max": -10},"pass_grip": {"cost": -0.05,"max": -10},"run_block_technique": {"cost": -0.05,"max": -10},"heart": {"cost": -0.05,"max": -10},"defense_consistency": {"cost": -0.05,"max": -10},"run_block_power": {"cost": -0.05,"max": -10},"coverage_technique": {"cost": -0.05,"max": -10},"lead_block_awareness": {"cost": -0.05,"max": -10},"sprinting": {"cost": -0.05,"max": -10},"tackle_power": {"cost": -0.05,"max": -10},"tackle_grip": {"cost": -0.05,"max": -10},"pass_block_technique": {"cost": -0.05,"max": -10},"pass_rush_technique": {"cost": -0.05,"max": -10},"coverage_deflection": {"cost": -0.05,"max": -10}},"position_descriptions": {},"position_exclusions": [],"name": "Early Bloomer","description": "<p>This player has lower potential but gets there easily.</p>\n\t\t\t\t\t\tAll Skills: 5% lower SP cost, -10 max","conflicts": ["slow_built"],"conflict_text": "<br><br>Conflicts with: Slow Built","salary_modifier": 0},"k_cool_headed": {"skill_modifiers": {"pass_consistency": {"cost": -0.05,"max": 3},"kick_consistency": {"cost": -0.05,"max": 3},"punt_consistency": {"cost": -0.05,"max": 3}},"conflicts": [],"position_descriptions": {"QB": "Pass Consistency: 5% lower SP cost, +3 max<br>Min Salary: +10%","P": "Punt Consistency: 5% lower SP cost, +3 max<br>Min Salary: +10%","K": "Kick Consistency: 5% lower SP cost, +3 max<br>Min Salary: +10%"},"position_exclusions": ["HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "P"],"salary_modifier": 0.1,"name": "Cool Headed","description": "Punt Consistency: 5% lower SP cost, +3 max<br>Min Salary: +10%"},"ball_hawk": {"skill_modifiers": {"coverage_interception": {"cost": -0.06,"max": 4},"coverage_deflection": {"cost": 0.1,"max": -6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "K", "P"],"name": "Ball Hawk","description": "<p>This defender is always looking for interceptions.</p>\n\t\t\t\t\t\tIntercepting: 6% lower SP cost, +5 max<br>\n\t\t\t\t\t\tDeflecting: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tMin Salary: +8%","conflicts": ["long_reach"],"conflict_text": "<br><br>Conflicts with: Long Reach","salary_modifier": 0.08},"high_jumper": {"skill_modifiers": {"vertical": {"cost": -0.05,"max": 3}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"salary_modifier": 0.1,"name": "High Jumper","description": "Vertical: 5% lower SP cost, +3 max<br>Min Salary: +10%"},"hb_power_rusher": {"skill_modifiers": {"carry_elusiveness": {"cost": 0.1,"max": -6},"carry_power": {"cost": -0.1,"max": 6},"carry_awareness": {"cost": -0.1,"max": 6},"catch_hands": {"cost": 0.05,"max": -2},"route_technique": {"cost": 0.05,"max": -3}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Power Rusher","description": "<p>This player focuses on his Power Running skills.</p>Power Running: 10% lower SP cost, +6 max<br>Carry Awareness: 10% lower SP cost, +6 max<br>Elusive Running: 10% higher SP cost, -6 max<br>Route Technique: 5% higher SP cost, -3 max<br>Receiving Hands: 5% higher SP cost, -2 max","conflicts": ["hb_scat_back", "hb_elusive_rusher", "hb_blocking_back", "hb_unpredictable"],"conflict_text": "<br><br>Conflicts with: Scat Back, Elusive Rusher, Blocking Back, Unpredictable","salary_modifier": 0.12},"ol_tech_blocker": {"skill_modifiers": {"run_block_technique": {"cost": -0.1,"max": 6},"run_block_power": {"cost": 0.1,"max": -6},"pass_block_power": {"cost": 0.1,"max": -6},"pass_block_technique": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "WR", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Technical Blocker","description": "<p>This player focuses on technique over power when blocking.</p>\n\t\t\t\t\t\tRun Blk Tech: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Blk Tech: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Blk Power: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tRun Blk Power: 10% higher SP cost, -6 max","conflicts": ["ol_power_blocker"],"conflict_text": "<br><br>Conflicts with: Power Blocker","salary_modifier": 0},"ol_run_blocker": {"skill_modifiers": {"run_block_awareness": {"cost": -0.08,"max": 8},"run_block_technique": {"cost": -0.08,"max": 8},"run_block_power": {"cost": -0.08,"max": 8}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Run Blocker","description": "<p>This player focuses on run blocking over pass blocking.</p>\n\t\t\t\t\t\tRun Blk Technique: 8% lower SP cost, +8 max<br>\n\t\t\t\t\t\tRun Blk Awareness: 8% lower SP cost, +8 max<br>\n\t\t\t\t\t\tRun Blk Power: 8% lower SP cost, +8 max<br>\n\t\t\t\t\t\tMin Salary: +10%","conflicts": ["ol_pass_blocker"],"conflict_text": "<br><br>Conflicts with: Pass Blocker","salary_modifier": 0.1},"k_kickoff_king": {"skill_modifiers": {"kickoff_power": {"cost": -0.05,"max": 3}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "P"],"salary_modifier": 0.1,"name": "Kickoff King","description": "Kickoff Power: 5% lower SP cost, +3 max<br>Min Salary: +10%"},"slippery": {"skill_modifiers": {"carry_elusiveness": {"cost": -0.05,"max": 3},"carry_power": {"cost": 0.05,"max": -3},"carry_awareness": {"cost": -0.04,"max": 2},"carry_grip": {"cost": 0.04,"max": -2}},"position_descriptions": {},"position_exclusions": ["QB", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Slippery","description": "<p>This player prefers to take the less direct approach when carrying the ball.</p>\n\t\t\t\t\t\tElusive Running: 5% lower SP cost, +3 max<br>\n\t\t\t\t\t\tCarry Awareness: 4% lower SP cost, +2 max<br>\n\t\t\t\t\t\tPower Running: 5% higher SP cost, -3 max<br>\n\t\t\t\t\t\tCarrying Grip: 4% higher SP cost, -2 max<br>\n\t\t\t\t\t\tMin Salary: +6%","conflicts": ["bruiser", "unpredictable"],"conflict_text": "<br><br>Conflicts with: Bruiser, Unpredictable","salary_modifier": 0.06},"ot_pass_protector": {"skill_modifiers": {"footwork": {"cost": -0.1,"max": 6},"pass_block_awareness": {"cost": -0.08,"max": 6}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"salary_modifier": 0.12,"name": "Pass Protector","description": "<p>This tackle is apt at protecting his quarterback.</p>\n\t\t\t\t\t\tFootwork: 8% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Blk Awareness: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMin Salary: +12%"},"zone_specialist": {"skill_modifiers": {"man_coverage_awareness": {"cost": 0.1,"max": -6},"zone_coverage_awareness": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "K", "P"],"name": "Zone Specialist","description": "<p>This defender is better in zone coverage than man coverage.</p>\n\t\t\t\t\t\tZone Awareness: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMan Awareness: 10% higher SP cost, -6 max","conflicts": ["man_specialist", "flex_coverage"],"conflict_text": "<br><br>Conflicts with: Man Specialist, Flex Coverage","salary_modifier": 0},"ol_pass_blocker": {"skill_modifiers": {"pass_block_awareness": {"cost": -0.08,"max": 8},"pass_block_power": {"cost": -0.08,"max": 8},"pass_block_technique": {"cost": -0.08,"max": 8}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Pass Blocker","description": "<p>This player focuses on pass blocking over run blocking.</p>\n\t\t\t\t\t\tPass Blk Tech: 8% lower SP cost, +8 max<br>\n\t\t\t\t\t\tPass Blk Power: 8% lower SP cost, +8 max<br>\n\t\t\t\t\t\tPass Blk Awareness: 8% lower SP cost, +8 max<br>\n\t\t\t\t\t\tMin Salary: +12%","conflicts": ["ol_run_blocker"],"conflict_text": "<br><br>Conflicts with: Run Blocker","salary_modifier": 0.12},"fb_rusher": {"skill_modifiers": {"carry_elusiveness": {"cost": -0.06,"max": 4},"carry_power": {"cost": -0.06,"max": 4},"carry_awareness": {"cost": -0.06,"max": 4},"carry_grip": {"cost": -0.06,"max": 4}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Rusher","description": "<p>This FB focuses on rushing over lead blocking.</p>\n\t\t\t\t\t\tPower Running: 6% lower SP cost, +4 max<br>\n\t\t\t\t\t\tElusive Running: 6% lower SP cost, +4 max<br>\n\t\t\t\t\t\tCarry Awareness: 6% lower SP cost, +4 max<br>\n\t\t\t\t\t\tCarrying Grip: 6% lower SP cost, +4 max<br>\n\t\t\t\t\t\tMin Salary: +12%","conflicts": ["fb_lead_blocker", "fb_scat_back"],"conflict_text": "<br><br>Conflicts with: Lead Blocker, Scat Back","salary_modifier": 0.12},"wr_shifty": {"skill_modifiers": {"route_elusiveness": {"cost": -0.1,"max": 6},"catch_hands": {"cost": -0.1,"max": 6},"route_technique": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Shifty","description": "<p>This WR is good at losing defenders with exceptional technique and eluisveness.</p>\n\t\t\t\t\t\tRoute Technique: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tRoute Elusiveness: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tReceiving Hands: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMin Salary: +14%","conflicts": ["wr_speedster", "wr_slot_receiver", "wr_control"],"conflict_text": "<br><br>Conflicts with: Speedster, Slot Receiver, Dominator","salary_modifier": 0.14},"strong_base": {"skill_modifiers": {"quickness": {"cost": -0.06,"max": -3},"balance": {"cost": -0.06,"max": 3}},"conflicts": [],"position_descriptions": {},"position_exclusions": [],"salary_modifier": 0,"name": "Strong Base","description": "<p>Fall once, shame on me.</p>\n\t\t\t\t\t\tBalance: 6% lower SP cost, +3 max<br>\n\t\t\t\t\t\tQuickness: 6% higher SP cost, -3 max"},"soft_hands": {"skill_modifiers": {"catch_in_traffic": {"cost": 0.05,"max": -3},"catch_awareness": {"cost": -0.08,"max": 4},"catch_grip": {"cost": 0.05,"max": -3},"catch_hands": {"cost": -0.08,"max": 4}},"position_descriptions": {},"position_exclusions": ["QB", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Soft Hands","description": "<p>You seen that glove on his left hand? Well, that glove\'s full of vaseline.</p>\n\t\t\t\t\t\tReceiving Hands: 8% lower SP cost, +4 max<br>\n\t\t\t\t\t\tReceiving Aware: 8% lower SP cost, +4 max<br>\n\t\t\t\t\t\tReceiving Grip: 5% higher SP cost, -3 max<br>\n\t\t\t\t\t\tCatching in Traffic: 5% higher SP cost, -3 max<br>\n\t\t\t\t\t\tMin Salary: +6%","conflicts": ["nerves_of_steel"],"conflict_text": "<br><br>Conflicts with: Nerves of Steel","salary_modifier": 0.06},"dl_dreadnought": {"skill_modifiers": {"toughness": {"cost": -0.05,"max": 6},"conditioning": {"cost": -0.05,"max": 6},"intimidation": {"cost": -0.05,"max": 6}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "FS", "CB", "K", "P"],"salary_modifier": 0.06,"name": "Dread-nought","description": "<p>This defender beats down and outlasts his opponent.</p>\n\t\t\t\t\t\tToughness: 5% lower SP cost, +6 max<br>\n\t\t\t\t\t\tConditioning: 5% lower SP cost, +6 max<br>\n\t\t\t\t\t\tIntimidation: 5% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMin Salary: +6%"},"ol_power_blocker": {"skill_modifiers": {"run_block_technique": {"cost": 0.1,"max": -6},"run_block_power": {"cost": -0.1,"max": 6},"pass_block_power": {"cost": -0.1,"max": 6},"pass_block_technique": {"cost": 0.1,"max": -6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "WR", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Power Blocker","description": "<p>This player focuses on power over technique when blocking.</p>\n\t\t\t\t\t\tRun Blk Power: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Blk Power: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Blk Tech: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tRun Blk Tech: 10% higher SP cost, -6 max","conflicts": ["ol_tech_blocker"],"conflict_text": "<br><br>Conflicts with: Technical Blocker","salary_modifier": 0},"qb_scrambler": {"skill_modifiers": {"pass_technique": {"cost": 0.1,"max": -6},"quickness": {"cost": -0.05,"max": 3},"pass_evasiveness": {"cost": -0.1,"max": 6},"toughness": {"cost": -0.05,"max": 3},"pass_accuracy": {"cost": 0.1,"max": -6},"footwork": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Scrambler","description": "<p>This QB prefers to stay on the move.</p>\n\t\t\t\t\t\tPocket Awareness: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tFootwork: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tQuickness: 5% lower SP cost, +3 max<br>\n\t\t\t\t\t\tToughness: 5% lower SP cost, +3 max<br>\n\t\t\t\t\t\tPass Accuracy: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tPass Technique: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tMin Salary: +10%","conflicts": ["qb_rusher", "qb_precision_passer", "qb_gunslinger", "qb_dual_threat"],"conflict_text": "<br><br>Conflicts with: Rusher, Precision Passer, Gunslinger, Dual Threat","salary_modifier": 0.1},"fearsome": {"skill_modifiers": {"intimidation": {"cost": -0.06,"max": 10}},"position_descriptions": {},"position_exclusions": [],"name": "Fearsome","description": "<p>It is much more secure to be feared than to be loved.</p>\n\t\t\t\t\t\tIntimidation: 6% lower SP cost, +10 max<br>\n\t\t\t\t\t\tMin Salary: +4%","conflicts": ["easy_going"],"conflict_text": "<br><br>Conflicts with: Easy Going","salary_modifier": 0.04},"nerves_of_steel": {"skill_modifiers": {"catch_in_traffic": {"cost": -0.08,"max": 4},"catch_consistency": {"cost": 0.05,"max": -3},"catch_hands": {"cost": 0.05,"max": -3},"catch_grip": {"cost": -0.08,"max": 4}},"position_descriptions": {},"position_exclusions": ["QB", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Nerves of Steel","description": "<p>When this player catches a pass, he holds on tight.</p>\n\t\t\t\t\t\tReceiving Grip: 8% lower SP cost, +4 max<br>\n\t\t\t\t\t\tCatching in Traffic: 8% lower SP cost, +4 max<br>\n\t\t\t\t\t\tReceiving Hands: 5% higher SP cost, -3 max<br>\n\t\t\t\t\t\tReceiving Aware: 5% higher SP cost, -3 max<br>\n\t\t\t\t\t\tMin Salary: +6%","conflicts": ["soft_hands"],"conflict_text": "<br><br>Conflicts with: Soft Hands","salary_modifier": 0.06},"chasedown_artist": {"skill_modifiers": {"tackle_awareness": {"cost": -0.05,"max": 3}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "P", "K"],"salary_modifier": 0,"name": "Chase Down Artist","description": "<p>This player is great at finding his way to the ball carrier.</p>\n\t\t\t\t\t\tPursuit: 5% lower SP cost, +3 max"},"lb_coverage": {"skill_modifiers": {"quickness": {"cost": -0.08,"max": 6},"man_coverage_awareness": {"cost": -0.1,"max": 6},"coverage_technique": {"cost": -0.1,"max": 6},"zone_coverage_awareness": {"cost": -0.1,"max": 6},"coverage_deflection": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "K", "P"],"name": "Coverage LB","description": "<p>This LB focuses his skills on coverage.</p>\n\t\t\t\t\t\tZone Cvg Aware: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMan Cvg Aware: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tCoverage Tech: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tDeflecting: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tQuickness: 8% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMin Salary: +12%","conflicts": ["lb_blitzer", "lb_middle_man"],"conflict_text": "<br><br>Conflicts with: Blitzer, Middle Man","salary_modifier": 0.12},"dl_juggernaut": {"skill_modifiers": {},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DE", "DT", "LB", "SS", "FS", "CB", "K", "P"],"salary_modifier": 0,"name": "Jugger NOT","description": "<p>This trait is now obsolete and does nothing.</p>"},"qb_precision_passer": {"skill_modifiers": {"pass_accuracy": {"cost": -0.1,"max": 6},"pass_power": {"cost": 0.1,"max": -6}},"position_descriptions": {},"position_exclusions": ["HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Precision Passer","description": "<p>This QB favors accuracy over arm strength.</p>\n\t\t\t\t\t\tPass Accuracy: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Power: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tMin Salary: +8%","conflicts": ["qb_rusher", "qb_gunslinger", "qb_scrambler", "qb_dual_threat"],"conflict_text": "<br><br>Conflicts with: Rusher, Gunslinger, Scrambler, Dual Threat","salary_modifier": 0.08},"spring_board": {"skill_modifiers": {"vertical": {"cost": -0.08,"max": 6},"diving": {"cost": -0.08,"max": 6}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "C", "OT", "G"],"salary_modifier": 0,"name": "Spring Board","description": "<p>Does he have springs in his shoes?</p>\n\t\t\t\t\t\tDiving: 8% lower SP cost, +6 max<br>\n\t\t\t\t\t\tVertical: 8% lower SP cost, +6 max<br>"},"te_receiver": {"skill_modifiers": {"catch_in_traffic": {"cost": -0.1,"max": 6},"catch_grip": {"cost": -0.1,"max": 6},"catch_hands": {"cost": -0.1,"max": 6},"route_technique": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Receiving Specialist","description": "<p>This TE focuses on going downfield for passes.</p>\n\t\t\t\t\t\tRoute Technique: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tReceiving Hands: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tReceiving Grip: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tCatch In Traffic: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMin Salary: +16%","conflicts": ["te_blocker"],"conflict_text": "<br><br>Conflicts with: Blocking Specialist","salary_modifier": 0.16},"bruiser": {"skill_modifiers": {"carry_elusiveness": {"cost": 0.05,"max": -3},"carry_power": {"cost": -0.05,"max": 3},"carry_awareness": {"cost": 0.04,"max": -2},"carry_grip": {"cost": -0.04,"max": 2}},"position_descriptions": {},"position_exclusions": ["QB", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Bruiser","description": "<p>This player is tough to bring down when he has the ball.</p>\n\t\t\t\t\t\tPower Running: 5% lower SP cost, +3 max<br>\n\t\t\t\t\t\tCarrying Grip: 4% lower SP cost, +2 max<br>\n\t\t\t\t\t\tElusive Running: 5% higher SP cost, -3 max<br>\n\t\t\t\t\t\tCarry Awareness: 4% higher SP cost, -2 max<br>\n\t\t\t\t\t\tMin Salary: +6%","conflicts": ["slippery", "unpredictable"],"conflict_text": "<br><br>Conflicts with: Slippery, Unpredictable","salary_modifier": 0.06},"qb_solid_frame": {"skill_modifiers": {"pass_evasiveness": {"cost": 0.05,"max": -3},"quickness": {"cost": 0.1,"max": -6},"toughness": {"cost": -0.05,"max": 3},"pass_grip": {"cost": -0.1,"max": 6},"footwork": {"cost": 0.05,"max": -2},"pass_carry_power": {"cost": -0.1,"max": 6},"sprinting": {"cost": 0.05,"max": -3}},"position_descriptions": {},"position_exclusions": ["HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Solid Frame","description": "<p>This QB can take a hit, but he is a little slow.</p>\n\t\t\t\t\t\tDrop Back Power: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tDrop Back Grip: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tToughness: 5% lower SP cost, +3 max<br>\n\t\t\t\t\t\tPocket Awareness: 5% higher SP cost, -3 max<br>\n\t\t\t\t\t\tQuickness: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tFootwork: 5% higher SP cost, -2 max<br>\n\t\t\t\t\t\tSprinting: 5% higher SP cost, -3 max","conflicts": [],"conflict_text": "","salary_modifier": 0},"qb_dual_threat": {"skill_modifiers": {"quickness": {"cost": -0.05,"max": -3},"carry_elusiveness": {"cost": -0.08,"max": -5},"pass_technique": {"cost": -0.08,"max": -5},"carry_awareness": {"cost": -0.08,"max": -5},"pass_accuracy": {"cost": -0.08,"max": -5},"sprinting": {"cost": -0.05,"max": -3}},"position_descriptions": {},"position_exclusions": ["HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Dual Threat","description": "<p>This QB can run and pass, but is a specialist at neither.</p>\n\t\t\t\t\t\tPass Accuracy: 8% lower SP cost, -5 max<br>\n\t\t\t\t\t\tPass Technique: 8% lower SP cost, -5 max<br>\n\t\t\t\t\t\tElusive Running: 8% lower SP cost, -5 max<br>\n\t\t\t\t\t\tCarrying Awareness: 8% lower SP cost, -5 max<br>\n\t\t\t\t\t\tQuickness: 5% lower SP cost, -3 max<br>\n\t\t\t\t\t\tSprinting: 5% lower SP cost, -3 max<br>\n\t\t\t\t\t\tMin Salary: +12%","conflicts": ["qb_rusher", "qb_precision_passer", "qb_gunslinger", "qb_scrambler"],"conflict_text": "<br><br>Conflicts with: Rusher, Precision Passer, Gunslinger, Scrambler","salary_modifier": 0.12},"dl_crusher": {"skill_modifiers": {"pass_rush_power": {"cost": -0.06,"max": 4},"toughness": {"cost": -0.06,"max": 4},"conditioning": {"cost": 0.06,"max": -4},"pass_rush_technique": {"cost": 0.06,"max": -4}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "LB", "SS", "FS", "CB", "K", "P"],"name": "Crusher","description": "<p>This defender prefers power over technique when pass rushing.</p>\n\t\t\t\t\t\tPass Rush Power: 6% lower SP cost, +4 max<br>\n\t\t\t\t\t\tToughness: 6% lower SP cost, +4 max<br>\n\t\t\t\t\t\tPass Rush Tech: 6% higher SP cost, -4 max<br>\n\t\t\t\t\t\tConditioning: 6% higher SP cost, -4 max","conflicts": ["dl_technique_man"],"conflict_text": "<br><br>Conflicts with: Technique Man","salary_modifier": 0},"egotist": {"skill_modifiers": {"heart": {"cost": 0.12,"max": -14},"toughness": {"cost": 0.1,"max": -12},"conditioning": {"cost": 0.1,"max": -12},"quickness": {"cost": -0.05,"max": 8},"balance": {"cost": -0.05,"max": 8},"vertical": {"cost": -0.05,"max": 8},"footwork": {"cost": -0.05,"max": 8},"sprinting": {"cost": -0.05,"max": 8},"diving": {"cost": -0.05,"max": 8}},"conflicts": [],"position_descriptions": {},"position_exclusions": [],"salary_modifier": 0.12,"name": "Egotist","description": "<p>This player is physically gifted, but he takes his gifts for granted.</p>\n\t\t\t\t\t\tBalance: 5% lower SP cost, +8 max<br>\n\t\t\t\t\t\tFootwork: 5% lower SP cost, +8 max<br>\n\t\t\t\t\t\tQuickness: 5% lower SP cost, +8 max<br>\n\t\t\t\t\t\tSprinting: 5% lower SP cost, +8 max<br>\n\t\t\t\t\t\tVertical: 5% lower SP cost, +8 max<br>\n\t\t\t\t\t\tDiving: 5% lower SP cost, +8 max<br>\n\t\t\t\t\t\tConditioning: 10% higher SP cost, -12 max<br>\n\t\t\t\t\t\tToughness: 10% higher SP cost, -12 max<br>\n\t\t\t\t\t\tHeart: 12% higher SP cost, -14 max<br>\n\t\t\t\t\t\tMin Salary: +12%"},"brick_wall": {"skill_modifiers": {"tackle_power": {"cost": -0.04,"max": 2},"hold_ground": {"cost": -0.05,"max": 3}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C"],"salary_modifier": 0,"name": "Brick Wall","description": "<p>Attacking this player is like hitting a brick wall.</p>\n\t\t\t\t\t\tHold Ground: 5% lower SP cost, +3 max<br>\n\t\t\t\t\t\tPower Tackling: 4% lower SP cost, +2 max<br>"},"dl_towering_man": {"skill_modifiers": {"blitz_awareness": {"cost": -0.05,"max": 3},"vertical": {"cost": -0.05,"max": 3},"pass_rush_deflection": {"cost": -0.05,"max": 3}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "LB", "SS", "FS", "CB", "K", "P"],"salary_modifier": 0,"name": "Towering Man","description": "<p>Next best thing to a sack.</p>\n\t\t\t\t\t\tPass Rush Deflect: 5% lower SP cost, +3 max<br>\n\t\t\t\t\t\tBlitz Awareness: 5% lower SP cost, +3 max<br>\n\t\t\t\t\t\tVertical: 5% lower SP cost, +3 max<br>"},"d_anchor": {"skill_modifiers": {"defense_consistency": {"cost": -0.05,"max": 3}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "P", "K"],"salary_modifier": 0,"name": "D Anchor","description": "<p>This player is always solid on defense, no matter the situation.</p>\n\t\t\t\t\t\tDefense Consistency: 5% lower SP cost, +3 max"},"tenacious": {"skill_modifiers": {"toughness": {"cost": -0.04,"max": 2},"tackle_grip": {"cost": -0.05,"max": 3}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C"],"name": "Tenacious","description": "<p>This defender doesn\'t like to give up.</p>\n\t\t\t\t\t\tTackling Grip: 6% lower SP cost, +3 max<br>\n\t\t\t\t\t\tToughness 4% lower SP cost, +2 max","conflicts": ["fumble_creator"],"conflict_text": "<br><br>Conflicts with: Fumble Creator","salary_modifier": 0},"dl_run_stuffer": {"skill_modifiers": {"break_run_block": {"cost": -0.1,"max": 6},"pass_rush_power": {"cost": 0.1,"max": -6},"hold_ground": {"cost": -0.1,"max": 6},"pass_rush_technique": {"cost": 0.1,"max": -6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "LB", "SS", "FS", "CB", "K", "P"],"name": "Run Stuffer","description": "<p>This defender focuses on stopping the run over pass rushing.</p>\n\t\t\t\t\t\tBreak Run Blk: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tHold Ground: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Rush Tech: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tPass Rush Power: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tMin Salary: +12%","conflicts": ["dl_pass_rusher"],"conflict_text": "<br><br>Conflicts with: Pass Rusher","salary_modifier": 0.12},"dl_technique_man": {"skill_modifiers": {"pass_rush_power": {"cost": 0.06,"max": -4},"toughness": {"cost": 0.06,"max": -4},"conditioning": {"cost": -0.06,"max": 4},"pass_rush_technique": {"cost": -0.06,"max": 4}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "LB", "SS", "FS", "CB", "K", "P"],"name": "Technique Man","description": "<p>This defender prefers technique over power when pass rushing.</p>\n\t\t\t\t\t\tPass Rush Tech: 6% lower SP cost, +4 max<br>\n\t\t\t\t\t\tConditioning: 6% lower SP cost, +4 max<br>\n\t\t\t\t\t\tPass Rush Power: 6% higher SP cost, -4 max<br>\n\t\t\t\t\t\tToughness: 6% higher SP cost, -4 max","conflicts": ["dl_crusher"],"conflict_text": "<br><br>Conflicts with: Crusher","salary_modifier": 0},"fb_lead_blocker": {"skill_modifiers": {"run_block_technique": {"cost": -0.1,"max": 6},"pass_block_power": {"cost": -0.1,"max": 6},"pass_block_awareness": {"cost": -0.1,"max": 6},"run_block_power": {"cost": -0.1,"max": 6},"lead_block_awareness": {"cost": -0.1,"max": 6},"pass_block_technique": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Lead Blocker","description": "<p>This FB focuses on blocking for his teammates.</p>\n\t\t\t\t\t\tLead Blk Aware: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tRun Blk Tech: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tRun Blk Power: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Blk Tech: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Blk Power: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Blk Aware: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMin Salary: +12%","conflicts": ["fb_rusher", "fb_scat_back"],"conflict_text": "<br><br>Conflicts with: Rusher, Scat Back","salary_modifier": 0.12},"workhorse": {"skill_modifiers": {"conditioning": {"cost": -0.06,"max": 10}},"conflicts": [],"position_descriptions": {},"position_exclusions": [],"salary_modifier": 0.05,"name": "Workhorse","description": "<p>This player just keeps going and going.</p>\n\t\t\t\t\t\tConditioning: 6% lower SP cost, +10 max<br>\n\t\t\t\t\t\tMin Salary: +5%"},"lb_middle_man": {"skill_modifiers": {"power_tackling": {"cost": -0.1,"max": 6},"pursuit": {"cost": -0.1,"max": 6},"toughness": {"cost": -0.1,"max": 6},"break_run_block": {"cost": -0.1,"max": 6},"intimidation": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "K", "P"],"name": "Middle Man","description": "<p>This LB focuses his skills on playing the run.</p>\n\t\t\t\t\t\tBreak Run Blk: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPower Tackling: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPursuit: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tToughness: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tIntimidation: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMin Salary: +10%","conflicts": ["lb_coverage", "lb_blitzer"],"conflict_text": "<br><br>Conflicts with: Coverage LB, Blitzer","salary_modifier": 0.1},"meathead": {"skill_modifiers": {"tackle_awareness": {"cost": 0.05,"max": -3},"blitz_awareness": {"cost": 0.05,"max": -3},"run_block_awareness": {"cost": 0.05,"max": -3},"pass_rush_power": {"cost": -0.05,"max": 3},"carry_power": {"cost": -0.05,"max": 3},"toughness": {"cost": -0.03,"max": 3},"pass_block_power": {"cost": -0.05,"max": 3},"run_block_power": {"cost": -0.05,"max": 3},"snap_reaction": {"cost": 0.06,"max": -6},"pass_block_awareness": {"cost": 0.05,"max": -3},"carry_awareness": {"cost": 0.05,"max": -3},"pass_carry_power": {"cost": -0.05,"max": 3},"intimidation": {"cost": -0.03,"max": 3},"tackle_power": {"cost": -0.05,"max": 3},"pass_awareness": {"cost": 0.05,"max": -3}},"position_descriptions": {"FS": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Power Tackling: 5% lower SP cost, +3 max<br>Pass Rush Power: 5% lower SP cost, +3 max<br>Snap Reaction: 6% higher SP cost, -6 max<br>Pursuit: 5% higher SP cost, -3 max<br>Blitz Awareness: 5% higher SP cost, -3 max","TE": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Power Running: 5% lower SP cost, +3 max<br>Run Blk Power: 5% lower SP cost, +3 max<br>Pass Blk Power: 5% lower SP cost, +3 max<br>Snap Reaction: 6% higher SP cost, -6 max<br>Carrying Awareness: 5% higher SP cost, -3 max<br>Run Blk Awareness: 5% higher SP cost, -3 max<br>Pass Blk Awareness: 5% higher SP cost, -3 max","HB": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Power Running: 5% lower SP cost, +3 max<br>Run Blk Power: 5% lower SP cost, +3 max<br>Pass Blk Power: 5% lower SP cost, +3 max<br>Snap Reaction: 6% higher SP cost, -6 max<br>Carrying Awareness: 5% higher SP cost, -3 max<br>Run Blk Awareness: 5% higher SP cost, -3 max<br>Pass Blk Awareness: 5% higher SP cost, -3 max","K": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Power Tackling: 5% lower SP cost, +3 max<br>Snap Reaction: 6% higher SP cost, -6 max<br>Pursuit: 5% higher SP cost, -3 max","CB": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Power Tackling: 5% lower SP cost, +3 max<br>Pass Rush Power: 5% lower SP cost, +3 max<br>Snap Reaction: 6% higher SP cost, -6 max<br>Pursuit: 5% higher SP cost, -3 max<br>Blitz Awareness: 5% higher SP cost, -3 max","FB": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Power Running: 5% lower SP cost, +3 max<br>Run Blk Power: 5% lower SP cost, +3 max<br>Pass Blk Power: 5% lower SP cost, +3 max<br>Snap Reaction: 6% higher SP cost, -6 max<br>Carrying Awareness: 5% higher SP cost, -3 max<br>Run Blk Awareness: 5% higher SP cost, -3 max<br>Pass Blk Awareness: 5% higher SP cost, -3 max","LB": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Power Tackling: 5% lower SP cost, +3 max<br>Pass Rush Power: 5% lower SP cost, +3 max<br>Snap Reaction: 6% higher SP cost, -6 max<br>Pursuit: 5% higher SP cost, -3 max<br>Blitz Awareness: 5% higher SP cost, -3 max","C": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Run Blk Power: 5% lower SP cost, +3 max<br>Pass Blk Power: 5% lower SP cost, +3 max<br>Snap Reaction: 6% higher SP cost, -6 max<br>Run Blk Awareness: 5% higher SP cost, -3 max<br>Pass Blk Awareness: 5% higher SP cost, -3 max","SS": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Power Tackling: 5% lower SP cost, +3 max<br>Pass Rush Power: 5% lower SP cost, +3 max<br>Snap Reaction: 6% higher SP cost, -6 max<br>Pursuit: 5% higher SP cost, -3 max<br>Blitz Awareness: 5% higher SP cost, -3 max","DT": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Power Tackling: 5% lower SP cost, +3 max<br>Pass Rush Power: 5% lower SP cost, +3 max<br>Snap Reaction: 6% higher SP cost, -6 max<br>Pursuit: 5% higher SP cost, -3 max<br>Blitz Awareness: 5% higher SP cost, -3 max","DE": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Power Tackling: 5% lower SP cost, +3 max<br>Pass Rush Power: 5% lower SP cost, +3 max<br>Snap Reaction: 6% higher SP cost, -6 max<br>Pursuit: 5% higher SP cost, -3 max<br>Blitz Awareness: 5% higher SP cost, -3 max","P": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Power Tackling: 5% lower SP cost, +3 max<br>Snap Reaction: 6% higher SP cost, -6 max<br>Pursuit: 5% higher SP cost, -3 max<br>","QB": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Drop Back Power: 5% lower SP cost, +3 max<br>Power Running: 5% lower SP cost, +3 max<br>Pass Awareness: 5% higher SP cost, -3 max<br>Carrying Awareness: 5% higher SP cost, -3 max","G": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Run Blk Power: 5% lower SP cost, +3 max<br>Pass Blk Power: 5% lower SP cost, +3 max<br>Snap Reaction: 6% higher SP cost, -6 max<br>Run Blk Awareness: 5% higher SP cost, -3 max<br>Pass Blk Awareness: 5% higher SP cost, -3 max","OT": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Run Blk Power: 5% lower SP cost, +3 max<br>Pass Blk Power: 5% lower SP cost, +3 max<br>Snap Reaction: 6% higher SP cost, -6 max<br>Run Blk Awareness: 5% higher SP cost, -3 max<br>Pass Blk Awareness: 5% higher SP cost, -3 max","WR": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Power Running: 5% lower SP cost, +3 max<br>Run Blk Power: 5% lower SP cost, +3 max<br>Snap Reaction: 6% higher SP cost, -6 max<br>Carrying Awareness: 5% higher SP cost, -3 max<br>Run Blk Awareness: 5% higher SP cost, -3 max"},"position_exclusions": [],"name": "Meathead","description": "<p>This player may be strong, but he is not the brightest.</p>Toughness: 3% lower SP cost, +3 max<br>Intimidation: 3% lower SP cost, +3 max<br>Power Tackling: 5% lower SP cost, +3 max<br>Drop Back Power: 5% lower SP cost, +3 max<br>Power Running: 5% lower SP cost, +3 max<br>Run Blk Power: 5% lower SP cost, +3 max<br>Pass Blk Power: 5% lower SP cost, +3 max<br>Pass Rush Power: 5% lower SP cost, +3 max<br>Snap Reaction: 6% higher SP cost, -6 max<br>Pursuit: 5% higher SP cost, -3 max<br>Pass Awareness: 5% higher SP cost, -3 max<br>Carrying Awareness: 5% higher SP cost, -3 max<br>Run Blk Awareness: 5% higher SP cost, -3 max<br>Pass Blk Awareness: 5% higher SP cost, -3 max<br>Blitz Awareness: 5% higher SP cost, -3 max","conflicts": ["tactician"],"conflict_text": "<br><br>Conflicts with: Tactician","salary_modifier": 0},"hb_scat_back": {"skill_modifiers": {"catch_in_traffic": {"cost": -0.1,"max": 6},"catch_grip": {"cost": -0.1,"max": 6},"catch_hands": {"cost": -0.1,"max": 6},"route_technique": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["QB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Scat Back","description": "<p>This HB focuses on his receiving skills first and foremost.</p>\n\t\t\t\t\t\tReceiving Grip: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tReceiving Hands: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tCatch in Traffic: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tRoute Technique: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMin Salary: +12%","conflicts": ["hb_rushing_back"],"conflict_text": "<br><br>Conflicts with: Rusher","salary_modifier": 0.12},"k_sharpshooter": {"skill_modifiers": {"punt_power": {"cost": 0.1,"max": -6},"punt_accuracy": {"cost": -0.1,"max": 6},"kick_power": {"cost": 0.1,"max": -6},"kick_accuracy": {"cost": -0.1,"max": 6}},"position_descriptions": {"P": "<p>This punter forgoes power for better accuracy.</p>Punt Accuracy: 10% lower SP cost, +6 max<br>Punt Power: 10% higher SP cost, -6 max","K": "<p>This kicker forgoes power for better accuracy.</p>Kick Accuracy: 10% lower SP cost, +6 max<br>Field Goal Power: 10% higher SP cost, -6 max"},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB"],"name": "Sharp Shooter","description": "Kick Accuracy: 10% lower SP cost, +6 max<br>Field Goal Power: 10% higher SP cost, -6 max","conflicts": ["k_leg_of_steel"],"conflict_text": "<br><br>Conflicts with: Leg of Steel","salary_modifier": 0},"wr_control": {"skill_modifiers": {"carry_power": {"cost": -0.1,"max": 6},"conditioning": {"cost": -0.1,"max": 6},"run_block_power": {"cost": -0.1,"max": 6},"intimidation": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Dominator","description": "<p>This WR focuses on wearing down his opponents.</p>\n\t\t\t\t\t\tRun Blk Power: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPower Running: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tIntimidation: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tConditioning: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMin Salary: +10%","conflicts": ["wr_speedster", "wr_shifty", "wr_slot_receiver"],"conflict_text": "<br><br>Conflicts with: Speedster, Possession WR, In-Traffic","salary_modifier": 0.1},"fumble_creator": {"skill_modifiers": {"tackle_strip": {"cost": -0.1,"max": 6},"tackle_grip": {"cost": 0.1,"max": -6},"tackle_technique": {"cost": 0.1,"max": -6},"tackle_power": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C"],"name": "Fumble Creator","description": "<p>This defender prefers to go for the fumble, even if he sometimes misses tackles.</p>\n\t\t\t\t\t\tPower Tackling: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tStrip Tech: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tTackling Tech: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tTackling Grip: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tMin Salary: +8%","conflicts": ["sure_tackler", "tenacious"],"conflict_text": "<br><br>Conflicts with: Sure Tackler, Tenacious","salary_modifier": 0.08},"unpredictable": {"skill_modifiers": {"carry_elusiveness": {"cost": -0.06,"max": -5},"carry_power": {"cost": -0.06,"max": -5},"carry_awareness": {"cost": -0.03,"max": 2},"carry_grip": {"cost": -0.03,"max": 2}},"short_name": "Unpre-dictable","position_descriptions": {},"position_exclusions": ["QB", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Unpr-edic-table","description": "<p>This HB is good at both power and Elusive Running, but is a specialist in neither.</p>\n\t\t\t\t\t\tElusive Running: 6% lower SP cost, -5 max<br>\n\t\t\t\t\t\tPower Running: 6% lower SP cost, -5 max<br>\n\t\t\t\t\t\tCarry Awareness: 3% lower SP cost, +2 max<br>\n\t\t\t\t\t\tCarrying Grip: 3% lower SP cost, +2 max<br>\n\t\t\t\t\t\tMin Salary: +6%","conflicts": ["bruiser", "slippery"],"conflict_text": "<br><br>Conflicts with: Bruiser, Slippery","salary_modifier": 0.06},"c_quick_snap": {"skill_modifiers": {"snap_reaction": {"cost": -0.15,"max": 10}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"salary_modifier": 0.04,"name": "Quick Snap","description": "<p>This center is great at getting off the line after the snap.</p>\n\t\t\t\t\t\tSnap Reaction: 15% lower SP cost, +10 max<br>\n\t\t\t\t\t\tMin Salary: +4%"},"quick_feet": {"skill_modifiers": {"quickness": {"cost": -0.1,"max": 6},"footwork": {"cost": -0.1,"max": 6},"sprinting": {"cost": 0.1,"max": -6}},"conflicts": [],"position_descriptions": {},"position_exclusions": [],"salary_modifier": 0,"name": "Quick Feet","description": "<p>Every which way but straight.</p>\n\t\t\t\t\t\tFootwork: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tQuickness: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tSprinting: 10% higher SP cost, -6 max"},"qb_rusher": {"skill_modifiers": {"carry_power": {"cost": -0.1,"max": 6},"pass_accuracy": {"cost": 0.1,"max": -6},"carry_grip": {"cost": -0.1,"max": 6},"carry_elusiveness": {"cost": -0.1,"max": 6},"pass_technique": {"cost": 0.1,"max": -6},"carry_awareness": {"cost": -0.1,"max": 6},"pass_consistency": {"cost": 0.1,"max": -6},"pass_awareness": {"cost": 0.1,"max": -6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Rusher","description": "<p>This QB is not afraid to carry the ball.</p>\n\t\t\t\t\t\tCarrying Grip: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPower Running: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tElusive Running: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tCarrying Awareness: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Technique: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tPass Accuracy: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tPass Awareness: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tPass Consistency: 10% higher SP cost, -6 max","conflicts": ["qb_dual_threat", "qb_precision_passer", "qb_gunslinger", "qb_scrambler"],"conflict_text": "<br><br>Conflicts with: Dual Threat, Precision Passer, Gunslinger, Scrambler","salary_modifier": 0},"return_specialist": {"skill_modifiers": {"return_awareness": {"cost": -0.05,"max": 3}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "OT", "G", "C", "DT", "DE", "LB", "K", "P"],"name": "Return Specialist","description": "<p>Half of a third of the game</p>\n\t\t\t\t\t\tReturn Awareness: 5% lower SP cost, +3 max"},"sure_tackler": {"skill_modifiers": {"tackle_strip": {"cost": 0.1,"max": -6},"tackle_grip": {"cost": -0.1,"max": 6},"tackle_technique": {"cost": -0.1,"max": 6},"tackle_power": {"cost": 0.1,"max": -6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C"],"name": "Sure Tackler","description": "<p>This defender goes for sure tackles over trying for fumbles.</p>\n\t\t\t\t\t\tTackling Tech: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tTackling Grip: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPower Tackling: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tStrip Tech: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tMin Salary: +6%","conflicts": ["fumble_creator"],"conflict_text": "<br><br>Conflicts with: Fumble Creator","salary_modifier": 0.06},"ol_consistent_blocker": {"skill_modifiers": {"snap_reaction": {"cost": 0.05,"max": -3},"block_consistency": {"cost": -0.1,"max": 6},"balance": {"cost": -0.05,"max": 3},"intimidation": {"cost": 0.05,"max": -3}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "WR", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"salary_modifier": 0.05,"name": "Consistent Blocker","description": "<p>We shall not falter.</p>\n\t\t\t\t\t\tBlk Consistency: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tBalance: 5% lower SP cost, +3 max<br>\n\t\t\t\t\t\tIntimidation: 5% higher SP cost, -3 max<br>\n\t\t\t\t\t\tSnap Reaction: 5% higher SP cost, -3 max<br>\n\t\t\t\t\t\tMin Salary: +6%"},"wr_slot_receiver": {"skill_modifiers": {"catch_in_traffic": {"cost": -0.1,"max": 6},"toughness": {"cost": -0.1,"max": 6},"catch_awareness": {"cost": -0.1,"max": 6},"catch_grip": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Slot Receiver","description": "<p>This WR is not afraid to lay his body on the line for a pass.</p>\n\t\t\t\t\t\tCatch In Traffic: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tReceiving Grip: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tReceiving Awareness: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tToughness: 10% lower SP cost, +10 max<br>\n\t\t\t\t\t\tMin Salary: +12%","conflicts": ["wr_speedster", "wr_shifty", "wr_control"],"conflict_text": "<br><br>Conflicts with: Speedster, Shifty, Dominator","salary_modifier": 0.12},"qb_field_general": {"skill_modifiers": {"leadership": {"cost": -0.05,"max": 3}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Field General","description": "<p>This QB is a great leader.</p>\n\t\t\t\t\t\tLeadership: 5% lower SP cost, +3 max"},"broad_jumper": {"skill_modifiers": {"diving": {"cost": -0.05,"max": 3}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"salary_modifier": 0.1,"name": "Broad Jumper","description": "Diving: 5% lower SP cost, +3 max<br>Min Salary: +10%"},"hb_elusive_rusher": {"skill_modifiers": {"carry_elusiveness": {"cost": -0.1,"max": 6},"carry_power": {"cost": 0.1,"max": -6},"carry_awareness": {"cost": -0.1,"max": 6},"carry_grip": {"cost": 0.1,"max": -6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Elusive Rusher","description": "<p>This player focuses on his Elusive Running skills.</p>Elusive Running: 10% lower SP cost, +6 max<br>Carry Awareness: 10% lower SP cost, +6 max<br>Power Running: 10% higher SP cost, -6 max<br>Carry Grip: 10% higher SP cost, -6 max","conflicts": ["hb_power_rusher", "hb_blocking_back", "hb_unpredictable"],"conflict_text": "<br><br>Conflicts with: Power Rusher, Blocking Back, Unpredictable","salary_modifier": 0.12},"k_leg_of_steel": {"skill_modifiers": {"punt_power": {"cost": -0.1,"max": 6},"punt_accuracy": {"cost": 0.1,"max": -6},"kick_power": {"cost": -0.1,"max": 6},"kick_accuracy": {"cost": 0.1,"max": -6}},"position_descriptions": {"P": "<p>This punter forgoes accuracy for greater power.</p>Punt Power: 10% lower SP cost, +6 max<br>Punt Accuracy: 10% higher SP cost, -6 max","K": "<p>This kicker forgoes accuracy for greater power.</p>Field Goal Power: 10% lower SP cost, +6 max<br>Kick Accuracy: 10% higher SP cost, -6 max"},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB"],"name": "Leg of Steel","description": "Field Goal Power: 10% lower SP cost, +6 max<br>Kick Accuracy: 10% higher SP cost, -6 max","conflicts": ["k_sharpshooter"],"conflict_text": "<br><br>Conflicts with: Sharpshooter","salary_modifier": 0},"wr_speedster": {"skill_modifiers": {"snap_reaction": {"cost": -0.1,"max": 6},"quickness": {"cost": -0.08,"max": 4},"sprinting": {"cost": -0.08,"max": 4}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Speedster","description": "<p>This WR focuses on speed, speed, and more speed.</p>\n\t\t\t\t\t\tSprinting: 8% lower SP cost, +4 max<br>\n\t\t\t\t\t\tQuickness: 8% lower SP cost, +4 max<br>\n\t\t\t\t\t\tSnap Reaction: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMin Salary: +18%","conflicts": ["wr_shifty", "wr_slot_receiver", "wr_control"],"conflict_text": "<br><br>Conflicts with: Shifty, Slot Receiver, Dominator","salary_modifier": 0.18},"g_downfield_blocker": {"skill_modifiers": {"lead_block_awareness": {"cost": -0.1,"max": 6},"sprinting": {"cost": -0.1,"max": 6}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"salary_modifier": 0.08,"name": "Downfield Blocker","description": "<p>This guard is great at pulling and getting into the secondary.</p>\n\t\t\t\t\t\tSprinting: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tLead Blk Aware: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMin Salary: +8%"},"qb_gunslinger": {"skill_modifiers": {"pass_accuracy": {"cost": 0.1,"max": -6},"pass_power": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Gunslinger","description": "<p>This QB favors arm strength over accuracy.</p>\n\t\t\t\t\t\tPass Power: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Accuracy: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tMin Salary: +8%","conflicts": ["qb_rusher", "qb_precision_passer", "qb_scrambler", "qb_dual_threat"],"conflict_text": "<br><br>Conflicts with: Rusher, Precision Passer, Scrambler, Dual Threat","salary_modifier": 0.08},"hb_blocking_back": {"skill_modifiers": {"run_block_awareness": {"cost": -0.1,"max": 6},"run_block_power": {"cost": -0.1,"max": 6},"pass_block_power": {"cost": -0.1,"max": 6},"pass_block_awareness": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["QB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Blocking Back","description": "<p>This HB focuses on blocking for his teammates.</p>\n\t\t\t\t\t\tPass Blk Tech: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Blk Power: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Blk Aware: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tRun Blk Tech: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tRun Blk Power: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tLead Blk Aware: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMin Salary: +6%","conflicts": [],"conflict_text": "","salary_modifier": 0.06},"superstar_nonglam": {"skill_modifiers": {"punt_power": {"cost": -0.2,"max": 10},"tackle_awareness": {"cost": -0.2,"max": 10},"tackle_strip": {"cost": -0.2,"max": 10},"run_block_awareness": {"cost": -0.2,"max": 10},"coverage_interception": {"cost": -0.2,"max": 10},"break_run_block": {"cost": -0.2,"max": 10},"pass_rush_power": {"cost": -0.2,"max": 10},"conditioning": {"cost": -0.2,"max": 10},"route_elusiveness": {"cost": -0.2,"max": 10},"return_awareness": {"cost": -0.2,"max": 10},"catch_consistency": {"cost": -0.2,"max": 10},"catch_grip": {"cost": -0.2,"max": 10},"catch_hands": {"cost": -0.2,"max": 10},"tackle_technique": {"cost": -0.2,"max": 10},"snap_reaction": {"cost": -0.2,"max": 10},"block_consistency": {"cost": -0.2,"max": 10},"man_coverage_awareness": {"cost": -0.2,"max": 10},"footwork": {"cost": -0.2,"max": 10},"pass_block_awareness": {"cost": -0.2,"max": 10},"pass_consistency": {"cost": -0.2,"max": 10},"intimidation": {"cost": -0.2,"max": 10},"diving": {"cost": -0.2,"max": 10},"punt_hands": {"cost": -0.2,"max": 10},"kick_consistency": {"cost": -0.2,"max": 10},"pass_evasiveness": {"cost": -0.2,"max": 10},"toughness": {"cost": -0.2,"max": 10},"pass_accuracy": {"cost": -0.2,"max": 10},"pass_rush_deflection": {"cost": -0.2,"max": 10},"pass_power": {"cost": -0.2,"max": 10},"zone_coverage_awareness": {"cost": -0.2,"max": 10},"kick_power": {"cost": -0.2,"max": 10},"quickness": {"cost": -0.2,"max": 10},"pass_technique": {"cost": -0.2,"max": 10},"vertical": {"cost": -0.2,"max": 10},"balance": {"cost": -0.2,"max": 10},"carry_awareness": {"cost": -0.2,"max": 10},"pass_carry_power": {"cost": -0.2,"max": 10},"punt_accuracy": {"cost": -0.2,"max": 10},"kickoff_power": {"cost": -0.2,"max": 10},"hold_ground": {"cost": -0.2,"max": 10},"pass_awareness": {"cost": -0.2,"max": 10},"route_technique": {"cost": -0.2,"max": 10},"punt_consistency": {"cost": -0.2,"max": 10},"blitz_awareness": {"cost": -0.2,"max": 10},"carry_power": {"cost": -0.2,"max": 10},"pass_block_power": {"cost": -0.2,"max": 10},"catch_awareness": {"cost": -0.2,"max": 10},"carry_grip": {"cost": -0.2,"max": 10},"kick_accuracy": {"cost": -0.2,"max": 10},"carry_elusiveness": {"cost": -0.2,"max": 10},"pass_grip": {"cost": -0.2,"max": 10},"run_block_technique": {"cost": -0.2,"max": 10},"heart": {"cost": -0.2,"max": 10},"defense_consistency": {"cost": -0.2,"max": 10},"run_block_power": {"cost": -0.2,"max": 10},"coverage_technique": {"cost": -0.2,"max": 10},"lead_block_awareness": {"cost": -0.2,"max": 10},"sprinting": {"cost": -0.2,"max": 10},"tackle_power": {"cost": -0.2,"max": 10},"tackle_grip": {"cost": -0.2,"max": 10},"pass_block_technique": {"cost": -0.2,"max": 10},"pass_rush_technique": {"cost": -0.2,"max": 10},"coverage_deflection": {"cost": -0.2,"max": 10}},"position_descriptions": {},"is_superstar": "nonglam","position_exclusions": ["QB", "HB", "FB", "WR", "TE", "DE", "SS", "FS", "CB", "LB"],"name": "Superstar","description": "<p>This is a special, highly skilled player. Each agent may only control <b>ONE</b> of each of the three types (150/100/50 Flex Pts) of superstars at a time, and they must be earned.</p>\n\t\t\t\t\t\tAll Skills: 20% lower SP cost, +10 max<br>\n\t\t\t\t\t\tGains 10,000 extra Skill Points over career<br>\n\t\t\t\t\t\tGains 3 extra Ability Points over career<br>\n\t\t\t\t\t\tMin Salary: +150%","conflicts": [],"salary_modifier": 1.5},"superstar_avg": {"skill_modifiers": {"punt_power": {"cost": -0.2,"max": 10},"tackle_awareness": {"cost": -0.2,"max": 10},"tackle_strip": {"cost": -0.2,"max": 10},"run_block_awareness": {"cost": -0.2,"max": 10},"coverage_interception": {"cost": -0.2,"max": 10},"break_run_block": {"cost": -0.2,"max": 10},"pass_rush_power": {"cost": -0.2,"max": 10},"conditioning": {"cost": -0.2,"max": 10},"route_elusiveness": {"cost": -0.2,"max": 10},"return_awareness": {"cost": -0.2,"max": 10},"catch_consistency": {"cost": -0.2,"max": 10},"catch_grip": {"cost": -0.2,"max": 10},"catch_hands": {"cost": -0.2,"max": 10},"tackle_technique": {"cost": -0.2,"max": 10},"snap_reaction": {"cost": -0.2,"max": 10},"block_consistency": {"cost": -0.2,"max": 10},"man_coverage_awareness": {"cost": -0.2,"max": 10},"footwork": {"cost": -0.2,"max": 10},"pass_block_awareness": {"cost": -0.2,"max": 10},"pass_consistency": {"cost": -0.2,"max": 10},"intimidation": {"cost": -0.2,"max": 10},"diving": {"cost": -0.2,"max": 10},"punt_hands": {"cost": -0.2,"max": 10},"kick_consistency": {"cost": -0.2,"max": 10},"pass_evasiveness": {"cost": -0.2,"max": 10},"toughness": {"cost": -0.2,"max": 10},"pass_accuracy": {"cost": -0.2,"max": 10},"pass_rush_deflection": {"cost": -0.2,"max": 10},"pass_power": {"cost": -0.2,"max": 10},"zone_coverage_awareness": {"cost": -0.2,"max": 10},"kick_power": {"cost": -0.2,"max": 10},"quickness": {"cost": -0.2,"max": 10},"pass_technique": {"cost": -0.2,"max": 10},"vertical": {"cost": -0.2,"max": 10},"balance": {"cost": -0.2,"max": 10},"carry_awareness": {"cost": -0.2,"max": 10},"pass_carry_power": {"cost": -0.2,"max": 10},"punt_accuracy": {"cost": -0.2,"max": 10},"kickoff_power": {"cost": -0.2,"max": 10},"hold_ground": {"cost": -0.2,"max": 10},"pass_awareness": {"cost": -0.2,"max": 10},"route_technique": {"cost": -0.2,"max": 10},"punt_consistency": {"cost": -0.2,"max": 10},"blitz_awareness": {"cost": -0.2,"max": 10},"carry_power": {"cost": -0.2,"max": 10},"pass_block_power": {"cost": -0.2,"max": 10},"catch_awareness": {"cost": -0.2,"max": 10},"carry_grip": {"cost": -0.2,"max": 10},"kick_accuracy": {"cost": -0.2,"max": 10},"carry_elusiveness": {"cost": -0.2,"max": 10},"pass_grip": {"cost": -0.2,"max": 10},"run_block_technique": {"cost": -0.2,"max": 10},"heart": {"cost": -0.2,"max": 10},"defense_consistency": {"cost": -0.2,"max": 10},"run_block_power": {"cost": -0.2,"max": 10},"coverage_technique": {"cost": -0.2,"max": 10},"lead_block_awareness": {"cost": -0.2,"max": 10},"sprinting": {"cost": -0.2,"max": 10},"tackle_power": {"cost": -0.2,"max": 10},"tackle_grip": {"cost": -0.2,"max": 10},"pass_block_technique": {"cost": -0.2,"max": 10},"pass_rush_technique": {"cost": -0.2,"max": 10},"coverage_deflection": {"cost": -0.2,"max": 10}},"position_descriptions": {},"is_superstar": "avg","position_exclusions": ["QB", "HB", "OT", "G", "C", "DT", "LB", "K", "P"],"name": "Superstar","description": "<p>This is a special, highly skilled player. Each agent may only control <b>ONE</b> of each of the three types (150/100/50 Flex Pts) of superstars at a time, and they must be earned.</p>\n\t\t\t\t\t\tAll Skills: 20% lower SP cost, +10 max<br>\n\t\t\t\t\t\tGains 10,000 extra Skill Points over career<br>\n\t\t\t\t\t\tGains 3 extra Ability Points over career<br>\n\t\t\t\t\t\tMin Salary: +150%","conflicts": [],"salary_modifier": 1.5},"p_sure_hands": {"skill_modifiers": {"punt_hands": {"cost": -0.05,"max": 3}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K"],"salary_modifier": 0.1,"name": "Sure Hands","description": "Punt Hands: 5% lower SP cost, +3 max<br>Min Salary: +10%"},"hb_rushing_back": {"skill_modifiers": {"carry_elusiveness": {"cost": -0.08,"max": 4},"carry_power": {"cost": -0.1,"max": 6},"carry_awareness": {"cost": -0.08,"max": 4},"carry_grip": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["QB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Rusher","description": "<p>This HB focuses on rushing the ball first and foremost.</p>\n\t\t\t\t\t\tPower Running: 8% lower SP cost, +4 max<br>\n\t\t\t\t\t\tElusive Running: 8% lower SP cost, +4 max<br>\n\t\t\t\t\t\tCarry Awareness: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tCarrying Grip: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMin Salary: +12%","conflicts": ["hb_scat_back"],"conflict_text": "<br><br>Conflicts with: Scat Back","salary_modifier": 0.12},"superstar_glam": {"skill_modifiers": {"punt_power": {"cost": -0.2,"max": 10},"tackle_awareness": {"cost": -0.2,"max": 10},"tackle_strip": {"cost": -0.2,"max": 10},"run_block_awareness": {"cost": -0.2,"max": 10},"coverage_interception": {"cost": -0.2,"max": 10},"break_run_block": {"cost": -0.2,"max": 10},"pass_rush_power": {"cost": -0.2,"max": 10},"conditioning": {"cost": -0.2,"max": 10},"route_elusiveness": {"cost": -0.2,"max": 10},"return_awareness": {"cost": -0.2,"max": 10},"catch_consistency": {"cost": -0.2,"max": 10},"catch_grip": {"cost": -0.2,"max": 10},"catch_hands": {"cost": -0.2,"max": 10},"tackle_technique": {"cost": -0.2,"max": 10},"snap_reaction": {"cost": -0.2,"max": 10},"block_consistency": {"cost": -0.2,"max": 10},"man_coverage_awareness": {"cost": -0.2,"max": 10},"footwork": {"cost": -0.2,"max": 10},"pass_block_awareness": {"cost": -0.2,"max": 10},"pass_consistency": {"cost": -0.2,"max": 10},"intimidation": {"cost": -0.2,"max": 10},"diving": {"cost": -0.2,"max": 10},"punt_hands": {"cost": -0.2,"max": 10},"kick_consistency": {"cost": -0.2,"max": 10},"pass_evasiveness": {"cost": -0.2,"max": 10},"toughness": {"cost": -0.2,"max": 10},"pass_accuracy": {"cost": -0.2,"max": 10},"pass_rush_deflection": {"cost": -0.2,"max": 10},"pass_power": {"cost": -0.2,"max": 10},"zone_coverage_awareness": {"cost": -0.2,"max": 10},"kick_power": {"cost": -0.2,"max": 10},"quickness": {"cost": -0.2,"max": 10},"pass_technique": {"cost": -0.2,"max": 10},"vertical": {"cost": -0.2,"max": 10},"balance": {"cost": -0.2,"max": 10},"carry_awareness": {"cost": -0.2,"max": 10},"pass_carry_power": {"cost": -0.2,"max": 10},"punt_accuracy": {"cost": -0.2,"max": 10},"kickoff_power": {"cost": -0.2,"max": 10},"hold_ground": {"cost": -0.2,"max": 10},"pass_awareness": {"cost": -0.2,"max": 10},"route_technique": {"cost": -0.2,"max": 10},"punt_consistency": {"cost": -0.2,"max": 10},"blitz_awareness": {"cost": -0.2,"max": 10},"carry_power": {"cost": -0.2,"max": 10},"pass_block_power": {"cost": -0.2,"max": 10},"catch_awareness": {"cost": -0.2,"max": 10},"carry_grip": {"cost": -0.2,"max": 10},"kick_accuracy": {"cost": -0.2,"max": 10},"carry_elusiveness": {"cost": -0.2,"max": 10},"pass_grip": {"cost": -0.2,"max": 10},"run_block_technique": {"cost": -0.2,"max": 10},"heart": {"cost": -0.2,"max": 10},"defense_consistency": {"cost": -0.2,"max": 10},"run_block_power": {"cost": -0.2,"max": 10},"coverage_technique": {"cost": -0.2,"max": 10},"lead_block_awareness": {"cost": -0.2,"max": 10},"sprinting": {"cost": -0.2,"max": 10},"tackle_power": {"cost": -0.2,"max": 10},"tackle_grip": {"cost": -0.2,"max": 10},"pass_block_technique": {"cost": -0.2,"max": 10},"pass_rush_technique": {"cost": -0.2,"max": 10},"coverage_deflection": {"cost": -0.2,"max": 10}},"position_descriptions": {},"is_superstar": "glam","position_exclusions": ["FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "K", "P"],"name": "Superstar","description": "<p>This is a special, highly skilled player. Each agent may only control <b>ONE</b> of each of the three types (150/100/50 Flex Pts) of superstars at a time, and they must be earned.</p>\n\t\t\t\t\t\tAll Skills: 20% lower SP cost, +10 max<br>\n\t\t\t\t\t\tGains 10,000 extra Skill Points over career<br>\n\t\t\t\t\t\tGains 3 extra Ability Points over career<br>\n\t\t\t\t\t\tMin Salary: +150%","conflicts": [],"salary_modifier": 1.5},"hb_unpredictable": {"skill_modifiers": {"carry_elusiveness": {"cost": -0.08,"max": -5},"carry_power": {"cost": -0.08,"max": -5}},"short_name": "Unpre-dictable","position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Unpredictable","description": "<p>This player is good at both power and Elusive Running, but is a specialist in neither.</p>Elusive Running: 8% lower SP cost, -5 max<br>Power Running: 8% lower SP cost, -5 max","conflicts": ["hb_scat_back", "hb_power_rusher", "hb_blocking_back", "hb_elusive_rusher"],"conflict_text": "<br><br>Conflicts with: Scat Back, Power Rusher, Blocking Back, Elusive Rusher","salary_modifier": 0.12},"lightning_reflexes": {"skill_modifiers": {"snap_reaction": {"cost": -0.05,"max": 3}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB"],"salary_modifier": 0,"name": "Lightning Reflexes","description": "<p>Flash before the bang.</p>\n\t\t\t\t\t\tSnap Reaction: 8% lower SP cost, +6 max"},"fb_scat_back": {"skill_modifiers": {"catch_in_traffic": {"cost": -0.08,"max": 4},"catch_hands": {"cost": -0.08,"max": 4},"route_technique": {"cost": -0.08,"max": 4}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Scat Back","description": "<p>This FB focuses on his receiving skills over blocking.</p>\n\t\t\t\t\t\tReceiving Hands: 8% lower SP cost, +4 max<br>\n\t\t\t\t\t\tReceiving Grip: 8% lower SP cost, +4 max<br>\n\t\t\t\t\t\tCatch In Traffic: 8% lower SP cost, +4 max<br>\n\t\t\t\t\t\tMin Salary: +12%","conflicts": ["fb_lead_blocker", "fb_rusher"],"conflict_text": "<br><br>Conflicts with: Lead Blocker, Rusher","salary_modifier": 0.12},"dl_pass_rusher": {"skill_modifiers": {"break_run_block": {"cost": 0.1,"max": -6},"pass_rush_power": {"cost": -0.1,"max": 6},"hold_ground": {"cost": 0.1,"max": -6},"pass_rush_technique": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "LB", "SS", "FS", "CB", "K", "P"],"name": "Pass Rusher","description": "<p>This defender focuses on pass rushing over stopping the run.</p>\n\t\t\t\t\t\tPass Rush Tech: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Rush Power: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tBreak Run Blk: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tHold Ground: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tMin Salary: +14%","conflicts": ["dl_run_stuffer"],"conflict_text": "<br><br>Conflicts with: Run Stuffer","salary_modifier": 0.14},"thick_skin": {"skill_modifiers": {"heart": {"cost": -0.04,"max": 2},"toughness": {"cost": -0.08,"max": 6}},"conflicts": [],"position_descriptions": {},"position_exclusions": [],"salary_modifier": 0,"name": "Thick Skin","description": "<p>Hit me once at least.</p>\n\t\t\t\t\t\tToughness: 8% lower SP cost, +6 max<br>\n\t\t\t\t\t\tHeart: 4% lower SP cost, +2 max"},
		"slow_built": {
			"skill_modifiers": {
				"punt_power": {
					"cost": 0.05, "max": 10
				},
				"tackle_awareness": {
					"cost": 0.05, "max": 10
				},
				"tackle_strip": {
					"cost": 0.05, "max": 10
				},
				"run_block_awareness": {
					"cost": 0.05,"max": 10
				},
				"coverage_interception": {
					"cost": 0.05,"max": 10
				},
				"break_run_block": {
					"cost": 0.05,"max": 10
				},
				"pass_rush_power": {
					"cost": 0.05,"max": 10
				},
				"conditioning": {
					"cost": 0.05,"max": 10
				},
				"route_elusiveness": {
					"cost": 0.05,"max": 10
				},
				"return_awareness": {
					"cost": 0.05,"max": 10
				},
				"catch_consistency": {
					"cost": 0.05,"max": 10
				},"catch_grip": {
					"cost": 0.05,"max": 10
				},
				"catch_hands": {
					"cost": 0.05,"max": 10
				},
				"tackle_technique": {
					"cost": 0.05,"max": 10
				},"snap_reaction": {"cost": 0.05,"max": 10},"block_consistency": {"cost": 0.05,"max": 10},"man_coverage_awareness": {"cost": 0.05,"max": 10},"footwork": {"cost": 0.05,"max": 10},"pass_block_awareness": {"cost": 0.05,"max": 10},"pass_consistency": {"cost": 0.05,"max": 10},"intimidation": {"cost": 0.05,"max": 10},"diving": {"cost": 0.05,"max": 10},"punt_hands": {"cost": 0.05,"max": 10},"kick_consistency": {"cost": 0.05,"max": 10},"pass_evasiveness": {"cost": 0.05,"max": 10},"toughness": {"cost": 0.05,"max": 10},"pass_accuracy": {"cost": 0.05,"max": 10},"pass_rush_deflection": {"cost": 0.05,"max": 10},"pass_power": {"cost": 0.05,"max": 10},"zone_coverage_awareness": {"cost": 0.05,"max": 10},"kick_power": {"cost": 0.05,"max": 10},"quickness": {"cost": 0.05,"max": 10},"pass_technique": {"cost": 0.05,"max": 10},"vertical": {"cost": 0.05,"max": 10},"balance": {"cost": 0.05,"max": 10},"carry_awareness": {"cost": 0.05,"max": 10},"pass_carry_power": {"cost": 0.05,"max": 10},"punt_accuracy": {"cost": 0.05,"max": 10},"kickoff_power": {"cost": 0.05,"max": 10},"hold_ground": {"cost": 0.05,"max": 10},"pass_awareness": {"cost": 0.05,"max": 10},"route_technique": {"cost": 0.05,"max": 10},"punt_consistency": {"cost": 0.05,"max": 10},"blitz_awareness": {"cost": 0.05,"max": 10},"carry_power": {"cost": 0.05,"max": 10},"pass_block_power": {"cost": 0.05,"max": 10},"catch_awareness": {"cost": 0.05,"max": 10},"carry_grip": {"cost": 0.05,"max": 10},"kick_accuracy": {"cost": 0.05,"max": 10},"carry_elusiveness": {"cost": 0.05,"max": 10},"pass_grip": {"cost": 0.05,"max": 10},"run_block_technique": {"cost": 0.05,"max": 10},"heart": {"cost": 0.05,"max": 10},"defense_consistency": {"cost": 0.05,"max": 10},"run_block_power": {"cost": 0.05,"max": 10},"coverage_technique": {"cost": 0.05,"max": 10},"lead_block_awareness": {"cost": 0.05,"max": 10},"sprinting": {"cost": 0.05,"max": 10},"tackle_power": {"cost": 0.05,"max": 10},"tackle_grip": {"cost": 0.05,"max": 10},"pass_block_technique": {"cost": 0.05,"max": 10},"pass_rush_technique": {"cost": 0.05,"max": 10},"coverage_deflection": {"cost": 0.05,"max": 10}},"position_descriptions": {},"position_exclusions": [],"name": "Slow Built","description": "<p>This player has higher potential but has trouble reaching it.</p>\n\t\t\t\t\t\tAll Skills: 5% higher SP cost, +10 max","conflicts": ["early_bloomer"],"conflict_text": "<br><br>Conflicts with: Early Bloomer","salary_modifier": 0},"long_reach": {"skill_modifiers": {"coverage_interception": {"cost": 0.1,"max": -6},"coverage_deflection": {"cost": -0.06,"max": 4}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "K", "P"],"name": "Long Reach","description": "<p>This defender just focuses on stopping the pass.</p>\n\t\t\t\t\t\tDeflecting: 6% lower SP cost, +4 max<br>\n\t\t\t\t\t\tIntercepting: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tMin Salary: +6%","conflicts": ["ball_hawk"],"conflict_text": "<br><br>Conflicts with: Ball Hawk","salary_modifier": 0.06},"shutdown_defender": {"skill_modifiers": {"coverage_technique": {"cost": -0.05,"max": 6}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "LB", "DT", "DE", "K", "P"],"salary_modifier": 0,"name": "Shutdown Defender","description": "<p>This defender sticks to his man like glue.</p>\n\t\t\t\t\t\tCoverage Tech: 5% lower SP cost, +6 max<br>"},"lb_blitzer": {"skill_modifiers": {"blitz_awareness": {"cost": -0.1,"max": 6},"pass_rush_power": {"cost": -0.1,"max": 6},"footwork": {"cost": -0.1,"max": 6},"pass_rush_technique": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "K", "P"],"name": "Blitzer","description": "<p>This LB focuses his skills on blitzing the quarterback.</p>\n\t\t\t\t\t\tPass Rush Tech: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Rush Power: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tBlitz Awareness: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tFootwork: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMin Salary: +12%","conflicts": ["lb_coverage", "lb_middle_man"],"conflict_text": "<br><br>Conflicts with: Coverage LB, Middle Man","salary_modifier": 0.14},"te_blocker": {"skill_modifiers": {"run_block_awareness": {"cost": -0.1,"max": 6},"run_block_power": {"cost": -0.1,"max": 6},"pass_block_power": {"cost": -0.1,"max": 6},"pass_block_awareness": {"cost": -0.1,"max": 6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "OT", "G", "C", "DT", "DE", "SS", "FS", "CB", "LB", "K", "P"],"name": "Blocking Specialist","description": "<p>This TE focuses on his blocking for his teammates.</p>\n\t\t\t\t\t\tPass Blk Tech: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tPass Blk Power: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tRun Blk Tech: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tRun Blk Power: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tMin Salary: +14%","conflicts": ["te_receiver"],"conflict_text": "<br><br>Conflicts with: Receiving Specialist","salary_modifier": 0.14},"tactician": {"skill_modifiers": {"tackle_awareness": {"cost": -0.05,"max": 3},"blitz_awareness": {"cost": -0.05,"max": 3},"run_block_awareness": {"cost": -0.05,"max": 3},"pass_rush_power": {"cost": 0.05,"max": -3},"carry_power": {"cost": 0.05,"max": -3},"toughness": {"cost": 0.03,"max": -3},"pass_block_power": {"cost": 0.05,"max": -3},"run_block_power": {"cost": 0.05,"max": -3},"snap_reaction": {"cost": -0.06,"max": 6},"pass_block_awareness": {"cost": -0.05,"max": 3},"carry_awareness": {"cost": -0.05,"max": 3},"pass_carry_power": {"cost": 0.05,"max": -3},"intimidation": {"cost": 0.03,"max": -3},"tackle_power": {"cost": 0.05,"max": -3},"pass_awareness": {"cost": -0.05,"max": 3}},"position_descriptions": {"FS": "<p>This player favors a tactical approach over power.</p>Snap Reaction: 6% lower SP cost, +6 max<br>Pursuit: 5% lower SP cost, +3 max<br>Blitz Awareness: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Power Tackling: 5% higher SP cost, -3 max<br>Pass Rush Power: 5% higher SP cost, -3 max","TE": "<p>This player favors a tactical approach over power.</p>Snap Reaction: 6% lower SP cost, +6 max<br>Carrying Awareness: 5% lower SP cost, +3 max<br>Run Blk Awareness: 5% lower SP cost, +3 max<br>Pass Blk Awareness: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Power Running: 5% higher SP cost, -3 max<br>Run Blk Power: 5% higher SP cost, -3 max<br>Pass Blk Power: 5% higher SP cost, -3 max","HB": "<p>This player favors a tactical approach over power.</p>Snap Reaction: 6% lower SP cost, +6 max<br>Carrying Awareness: 5% lower SP cost, +3 max<br>Run Blk Awareness: 5% lower SP cost, +3 max<br>Pass Blk Awareness: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Power Running: 5% higher SP cost, -3 max<br>Run Blk Power: 5% higher SP cost, -3 max<br>Pass Blk Power: 5% higher SP cost, -3 max","K": "<p>This player favors a tactical approach over power.</p>Snap Reaction: 6% lower SP cost, +6 max<br>Pursuit: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Power Tackling: 5% higher SP cost, -3 max","CB": "<p>This player favors a tactical approach over power.</p>Snap Reaction: 6% lower SP cost, +6 max<br>Pursuit: 5% lower SP cost, +3 max<br>Blitz Awareness: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Power Tackling: 5% higher SP cost, -3 max<br>Pass Rush Power: 5% higher SP cost, -3 max","FB": "<p>This player favors a tactical approach over power.</p>Snap Reaction: 6% lower SP cost, +6 max<br>Carrying Awareness: 5% lower SP cost, +3 max<br>Run Blk Awareness: 5% lower SP cost, +3 max<br>Pass Blk Awareness: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Power Running: 5% higher SP cost, -3 max<br>Run Blk Power: 5% higher SP cost, -3 max<br>Pass Blk Power: 5% higher SP cost, -3 max","LB": "<p>This player favors a tactical approach over power.</p>Snap Reaction: 6% lower SP cost, +6 max<br>Pursuit: 5% lower SP cost, +3 max<br>Blitz Awareness: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Power Tackling: 5% higher SP cost, -3 max<br>Pass Rush Power: 5% higher SP cost, -3 max","C": "<p>This player favors a tactical approach over power.</p>Snap Reaction: 6% lower SP cost, +6 max<br>Run Blk Awareness: 5% lower SP cost, +3 max<br>Pass Blk Awareness: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Run Blk Power: 5% higher SP cost, -3 max<br>Pass Blk Power: 5% higher SP cost, -3 max","SS": "<p>This player favors a tactical approach over power.</p>Snap Reaction: 6% lower SP cost, +6 max<br>Pursuit: 5% lower SP cost, +3 max<br>Blitz Awareness: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Power Tackling: 5% higher SP cost, -3 max<br>Pass Rush Power: 5% higher SP cost, -3 max","DT": "<p>This player favors a tactical approach over power.</p>Snap Reaction: 6% lower SP cost, +6 max<br>Pursuit: 5% lower SP cost, +3 max<br>Blitz Awareness: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Power Tackling: 5% higher SP cost, -3 max<br>Pass Rush Power: 5% higher SP cost, -3 max","DE": "<p>This player favors a tactical approach over power.</p>Snap Reaction: 6% lower SP cost, +6 max<br>Pursuit: 5% lower SP cost, +3 max<br>Blitz Awareness: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Power Tackling: 5% higher SP cost, -3 max<br>Pass Rush Power: 5% higher SP cost, -3 max","P": "<p>This player favors a tactical approach over power.</p>Snap Reaction: 6% lower SP cost, +6 max<br>Pursuit: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Power Tackling: 5% higher SP cost, -3 max","QB": "<p>This player favors a tactical approach over power.</p>Pass Awareness: 5% lower SP cost, +3 max<br>Carrying Awareness: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Drop Back Power: 5% higher SP cost, -3 max<br>Power Running: 5% higher SP cost, -3 max","G": "<p>This player favors a tactical approach over power.</p>Snap Reaction: 6% lower SP cost, +6 max<br>Run Blk Awareness: 5% lower SP cost, +3 max<br>Pass Blk Awareness: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Run Blk Power: 5% higher SP cost, -3 max<br>Pass Blk Power: 5% higher SP cost, -3 max","OT": "<p>This player favors a tactical approach over power.</p>Snap Reaction: 6% lower SP cost, +6 max<br>Run Blk Awareness: 5% lower SP cost, +3 max<br>Pass Blk Awareness: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Run Blk Power: 5% higher SP cost, -3 max<br>Pass Blk Power: 5% higher SP cost, -3 max","WR": "<p>This player favors a tactical approach over power.</p>Snap Reaction: 6% lower SP cost, +6 max<br>Carrying Awareness: 5% lower SP cost, +3 max<br>Run Blk Awareness: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Power Running: 5% higher SP cost, -3 max<br>Run Blk Power: 5% higher SP cost, -3 max"},"position_exclusions": [],"name": "Tactician","description": "<p>This player favors a tactical approach over power.</p>Snap Reaction: 6% lower SP cost, +6 max<br>Pursuit: 5% lower SP cost, +3 max<br>Pass Awareness: 5% lower SP cost, +3 max<br>Carrying Awareness: 5% lower SP cost, +3 max<br>Run Blk Awareness: 5% lower SP cost, +3 max<br>Pass Blk Awareness: 5% lower SP cost, +3 max<br>Blitz Awareness: 5% lower SP cost, +3 max<br>Toughness: 3% higher SP cost, -3 max<br>Intimidation: 3% higher SP cost, -3 max<br>Power Tackling: 5% higher SP cost, -3 max<br>Drop Back Power: 5% higher SP cost, -3 max<br>Power Running: 5% higher SP cost, -3 max<br>Run Blk Power: 5% higher SP cost, -3 max<br>Pass Blk Power: 5% higher SP cost, -3 max<br>Pass Rush Power: 5% higher SP cost, -3 max","conflicts": ["meathead"],"conflict_text": "<br><br>Conflicts with: Meathead","salary_modifier": 0},"flex_coverage": {"skill_modifiers": {"man_coverage_awareness": {"cost": -0.1,"max": -6},"zone_coverage_awareness": {"cost": -0.1,"max": -6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "K", "P"],"name": "Flex Coverage","description": "<p>This defender balances between zone and man coverage.</p>\n\t\t\t\t\t\tZone Awareness: 10% lower SP cost, -6 max<br>\n\t\t\t\t\t\tMan Awareness: 10% lower SP cost, -6 max","conflicts": ["man_specialist", "zone_specialist"],"conflict_text": "<br><br>Conflicts with: Man Specialist, Zone Specialist","salary_modifier": 0},"man_specialist": {"skill_modifiers": {"man_coverage_awareness": {"cost": -0.1,"max": 6},"zone_coverage_awareness": {"cost": 0.1,"max": -6}},"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DT", "DE", "K", "P"],"name": "Man Specialist","description": "<p>This defender is better in man coverage than zone coverage.</p>\n\t\t\t\t\t\tMan Awareness: 10% lower SP cost, +6 max<br>\n\t\t\t\t\t\tZone Awareness: 10% higher SP cost, -6 max","conflicts": ["zone_specialist", "flex_coverage"],"conflict_text": "<br><br>Conflicts with: Zone Specialist, Flex Coverage","salary_modifier": 0},"dl_heavyweight": {"skill_modifiers": {"break_run_block": {"cost": -0.04,"max": 2},"hold_ground": {"cost": -0.05,"max": 3}},"conflicts": [],"position_descriptions": {},"position_exclusions": ["QB", "HB", "FB", "WR", "TE", "OT", "G", "C", "DE", "DT", "LB", "SS", "FS", "CB", "K", "P"],"salary_modifier": 0.18,"name": "Heavy Weight","description": "<p>This defender is tough to push around.</p>\n\t\t\t\t\t\tHold Ground: 5% lower SP cost, +3 max<br>\n\t\t\t\t\t\tBreak Run Blk: 4% lower SP cost, +3 max<br>\n\t\t\t\t\t\tMin Salary: +18%"},"easy_going": {"skill_modifiers": {"heart": {"cost": -0.1,"max": 6},"intimidation": {"cost": 0.1,"max": -6}},"chemistry_modifier": 0.1,"position_descriptions": {},"position_exclusions": [],"name": "Easy Going","description": "<p>When one door is closed, another is opened.</p>\n\t\t\t\t\t\tHeart: 5% lower SP cost, +6 max<br>\n\t\t\t\t\t\tIntimidation: 10% higher SP cost, -6 max<br>\n\t\t\t\t\t\tChemistry Recovery: 10% faster","conflicts": ["fearsome"],"conflict_text": "<br><br>Conflicts with: Fearsome"}}
		init_traits = [trait1, trait2, trait3]
		for index in range(3):
			init_trait = init_traits[index]
			try:
				this_trait = traits[init_trait]
			except:
				this_trait = traits[traits_help[init_trait]]
			init_traits[index] = this_trait
		## Creating the player
		self.player = {
			"position": position,
			"attributes": {
				"strength": strength,
				"agility": agility,
				"speed": speed,
				"confidence": confidence,
				"stamina": stamina,
				"awareness": awareness
			},
			'height': height,
			'weight': weight,
			'traits': init_traits
		}
		self.skills = {
		"punt_power": {
			"name": "Punt Power",
			"height": 0,
			"position_multiplier": {
				"P": 100
			},
			"positions": [
				"P"
			],
			"weight": -0.025,
			"base_price": 4,
			"attributes": {
				"stamina": 0,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -0.5,
				"strength": -2.5
			}
		},
		"tackle_strip": {
			"name": "Strip Technique",
			"height": 0.5,
			"position_multiplier": {
				"DE": 125,
				"FS": 100,
				"P": 200,
				"K": 200,
				"CB": 100,
				"LB": 100,
				"SS": 110,
				"DT": 130
			},
			"positions": [
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS",
				"K",
				"P"
			],
			"weight": -0.025,
			"base_price": 2,
			"attributes": {
				"stamina": 0,
				"awareness": -1.25,
				"speed": 0,
				"agility": -1.25,
				"confidence": 0,
				"strength": -0.5
			}
		},
		"leadership": {
			"name": "Leadership",
			"height": 0,
			"position_multiplier": {
				"QB": 100
			},
			"positions": [
				"QB"
			],
			"weight": 0,
			"base_price": 1,
			"attributes": {
				"stamina": 0,
				"awareness": -1,
				"speed": 0,
				"agility": 0,
				"confidence": -2,
				"strength": 0
			}
		},
		"run_block_awareness": {
			"name": "Run Blk Awr",
			"height": 0,
			"full_name": "Run Blocking Awareness",
			"position_multiplier": {
				"C": 100,
				"TE": 100,
				"HB": 120,
				"FB": 100,
				"G": 100,
				"OT": 100,
				"WR": 130
			},
			"weight": 0,
			"positions": [
				"FB",
				"HB",
				"TE",
				"WR",
				"OT",
				"G",
				"C"
			],
			"base_price": 1,
			"attributes": {
				"stamina": 0,
				"awareness": -3,
				"speed": 0,
				"agility": 0,
				"confidence": 0,
				"strength": 0
			}
		},
		"coverage_interception": {
			"name": "Intercepting",
			"height": -0.25,
			"position_multiplier": {
				"LB": 130,
				"FS": 100,
				"CB": 110,
				"SS": 120
			},
			"positions": [
				"LB",
				"CB",
				"FS",
				"SS"
			],
			"weight": 0.025,
			"base_price": 3,
			"attributes": {
				"stamina": 0,
				"awareness": -1,
				"speed": 0,
				"agility": -1.5,
				"confidence": -0.25,
				"strength": 0.25
			}
		},
		"pass_rush_power": {
			"name": "Pass Rush Power",
			"height": 0.25,
			"position_multiplier": {
				"DE": 100,
				"LB": 110,
				"FS": 140,
				"CB": 140,
				"SS": 130,
				"DT": 100
			},
			"positions": [
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS"
			],
			"weight": -0.05,
			"base_price": 2,
			"attributes": {
				"stamina": -0.25,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -0.5,
				"strength": -2.25
			}
		},
		"route_elusiveness": {
			"name": "Route Elusiveness",
			"height": 0,
			"position_multiplier": {
				"TE": 120,
				"HB": 105,
				"FB": 140,
				"WR": 100
			},
			"positions": [
				"FB",
				"HB",
				"TE",
				"WR"
			],
			"weight": 0.025,
			"base_price": 2,
			"attributes": {
				"stamina": 0,
				"awareness": -0.5,
				"speed": -0.25,
				"agility": -2,
				"confidence": -0.25,
				"strength": 0
			}
		},
		"catch_consistency": {
			"name": "Rec Consistency",
			"height": 0,
			"full_name": "Receiving Consistency",
			"position_multiplier": {
				"TE": 100,
				"HB": 125,
				"FB": 130,
				"WR": 100
			},
			"weight": 0,
			"positions": [
				"FB",
				"HB",
				"TE",
				"WR"
			],
			"base_price": 1.25,
			"attributes": {
				"stamina": -0.3,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -2.7,
				"strength": 0
			}
		},
		"snap_reaction": {
			"name": "Snap Reaction",
			"height": 0,
			"position_multiplier": {
				"FS": 120,
				"TE": 100,
				"HB": 100,
				"K": 100,
				"CB": 130,
				"FB": 100,
				"LB": 110,
				"C": 95,
				"SS": 130,
				"DT": 100,
				"DE": 105,
				"P": 100,
				"QB": 90,
				"G": 100,
				"OT": 100,
				"WR": 110
			},
			"positions": [
				"FB",
				"HB",
				"TE",
				"WR",
				"OT",
				"G",
				"C",
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS",
				"K",
				"P"
			],
			"weight": 0,
			"base_price": 1,
			"attributes": {
				"stamina": -0.1,
				"awareness": -2.9,
				"speed": 0,
				"agility": 0,
				"confidence": 0,
				"strength": 0
			}
		},
		"block_consistency": {
			"name": "Block Consistency",
			"height": 0,
			"full_name": "Block Consistency",
			"position_multiplier": {
				"C": 100,
				"TE": 105,
				"HB": 110,
				"FB": 100,
				"G": 100,
				"OT": 100,
				"WR": 120
			},
			"weight": 0,
			"positions": [
				"FB",
				"HB",
				"TE",
				"WR",
				"OT",
				"G",
				"C"
			],
			"base_price": 1,
			"attributes": {
				"stamina": 0,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -3,
				"strength": 0
			}
		},
		"pass_block_awareness": {
			"name": "Pass Blk Awr",
			"height": 0,
			"full_name": "Pass Blocking Awareness",
			"position_multiplier": {
				"C": 100,
				"TE": 110,
				"HB": 130,
				"FB": 130,
				"G": 100,
				"OT": 90
			},
			"weight": 0,
			"positions": [
				"FB",
				"HB",
				"TE",
				"OT",
				"G",
				"C"
			],
			"base_price": 1,
			"attributes": {
				"stamina": 0,
				"awareness": -3,
				"speed": 0,
				"agility": 0,
				"confidence": 0,
				"strength": 0
			}
		},
		"diving": {
			"name": "Diving",
			"height": -0.2,
			"position_multiplier": {
				"FS": 100,
				"TE": 100,
				"HB": 100,
				"K": 140,
				"CB": 90,
				"FB": 110,
				"LB": 110,
				"C": 150,
				"SS": 110,
				"DT": 135,
				"DE": 120,
				"P": 130,
				"QB": 120,
				"G": 150,
				"OT": 150,
				"WR": 95
			},
			"positions": [
				"FB",
				"HB",
				"TE",
				"WR",
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS",
				"K",
				"P"
			],
			"weight": 0.025,
			"base_price": 2,
			"attributes": {
				"stamina": 0,
				"awareness": 0.25,
				"speed": 0,
				"agility": -2.25,
				"confidence": -0.5,
				"strength": 0
			}
		},
		"kick_consistency": {
			"name": "Kick Consistency",
			"height": 0,
			"position_multiplier": {
				"K": 100
			},
			"positions": [
				"K"
			],
			"weight": 0,
			"base_price": 3,
			"attributes": {
				"stamina": -0.3,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -2.7,
				"strength": 0
			}
		},
		"pass_evasiveness": {
			"name": "Pocket Awr",
			"height": 0.25,
			"full_name": "Pocket Awareness",
			"position_multiplier": {
				"QB": 100
			},
			"weight": 0.05,
			"positions": [
				"QB"
			],
			"base_price": 1.5,
			"attributes": {
				"stamina": -0.1,
				"awareness": -0.8,
				"speed": -0.4,
				"agility": -1.7,
				"confidence": 0,
				"strength": 0
			}
		},
		"toughness": {
			"name": "Toughness",
			"height": 0,
			"position_multiplier": {
				"FS": 110,
				"TE": 100,
				"HB": 110,
				"K": 180,
				"CB": 130,
				"FB": 100,
				"LB": 95,
				"C": 90,
				"SS": 100,
				"DT": 95,
				"DE": 100,
				"P": 170,
				"QB": 140,
				"G": 95,
				"OT": 100,
				"WR": 140
			},
			"positions": [
				"QB",
				"FB",
				"HB",
				"TE",
				"WR",
				"OT",
				"G",
				"C",
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS",
				"K",
				"P"
			],
			"weight": -0.05,
			"base_price": 1.25,
			"attributes": {
				"stamina": -1,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -1.5,
				"strength": -0.5
			}
		},
		"pass_accuracy": {
			"name": "Pass Accuracy",
			"height": -0.25,
			"position_multiplier": {
				"QB": 100
			},
			"positions": [
				"QB"
			],
			"weight": 0,
			"base_price": 3.5,
			"attributes": {
				"stamina": 0,
				"awareness": -1,
				"speed": 0,
				"agility": -2,
				"confidence": 0,
				"strength": 0
			}
		},
		"kick_power": {
			"name": "Field Goal Power",
			"height": 0,
			"position_multiplier": {
				"K": 100
			},
			"positions": [
				"K"
			],
			"weight": -0.025,
			"base_price": 4,
			"attributes": {
				"stamina": 0,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -0.5,
				"strength": -2.5
			}
		},
		"pass_technique": {
			"name": "Pass Technique",
			"height": 0,
			"position_multiplier": {
				"QB": 100
			},
			"positions": [
				"QB"
			],
			"weight": 0,
			"base_price": 2.5,
			"attributes": {
				"stamina": -0.25,
				"awareness": 0,
				"speed": 0,
				"agility": -2,
				"confidence": -0.5,
				"strength": -0.25
			}
		},
		"carry_awareness": {
			"name": "Carrying Awr",
			"height": 0,
			"full_name": "Carrying Awareness",
			"position_multiplier": {
				"TE": 120,
				"HB": 90,
				"QB": 150,
				"FB": 120,
				"WR": 110
			},
			"weight": 0,
			"positions": [
				"QB",
				"FB",
				"HB",
				"TE",
				"WR"
			],
			"base_price": 1.1,
			"attributes": {
				"stamina": 0,
				"awareness": -3,
				"speed": 0,
				"agility": 0,
				"confidence": 0,
				"strength": 0
			}
		},
		"route_technique": {
			"name": "Route Technique",
			"height": 0,
			"position_multiplier": {
				"TE": 105,
				"HB": 110,
				"FB": 130,
				"WR": 100
			},
			"positions": [
				"FB",
				"HB",
				"TE",
				"WR"
			],
			"weight": 0.025,
			"base_price": 1.25,
			"attributes": {
				"stamina": 0,
				"awareness": -1.5,
				"speed": 0,
				"agility": -1.5,
				"confidence": 0,
				"strength": 0
			}
		},
		"punt_consistency": {
			"name": "Punt Consistency",
			"height": 0,
			"position_multiplier": {
				"P": 100
			},
			"positions": [
				"P"
			],
			"weight": 0,
			"base_price": 3,
			"attributes": {
				"stamina": -0.3,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -2.7,
				"strength": 0
			}
		},
		"carry_grip": {
			"name": "Carrying Grip",
			"height": 0,
			"position_multiplier": {
				"TE": 95,
				"HB": 90,
				"QB": 150,
				"FB": 100,
				"WR": 130
			},
			"positions": [
				"QB",
				"FB",
				"HB",
				"TE",
				"WR"
			],
			"weight": -0.01,
			"base_price": 1,
			"attributes": {
				"stamina": -0.25,
				"awareness": -0.25,
				"speed": 0,
				"agility": 0,
				"confidence": -1,
				"strength": -1.5
			}
		},
		"carry_elusiveness": {
			"name": "Elusive Running",
			"height": 0,
			"position_multiplier": {
				"TE": 120,
				"HB": 100,
				"QB": 130,
				"FB": 120,
				"WR": 100
			},
			"positions": [
				"QB",
				"FB",
				"HB",
				"TE",
				"WR"
			],
			"weight": 0.06,
			"base_price": 3.5,
			"attributes": {
				"stamina": 0,
				"awareness": -0.8,
				"speed": -0.3,
				"agility": -1.9,
				"confidence": 0,
				"strength": 0
			}
		},
		"defense_consistency": {
			"name": "Def Consistency",
			"height": 0,
			"full_name": "Defense Consistency",
			"position_multiplier": {
				"DE": 100,
				"LB": 95,
				"FS": 100,
				"CB": 110,
				"SS": 100,
				"DT": 100
			},
			"weight": 0,
			"positions": [
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS"
			],
			"base_price": 1,
			"attributes": {
				"stamina": 0,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -3,
				"strength": 0
			}
		},
		"run_block_power": {
			"name": "Run Blk Power",
			"height": 0.5,
			"full_name": "Run Blocking Power",
			"position_multiplier": {
				"C": 95,
				"TE": 100,
				"HB": 120,
				"FB": 95,
				"G": 90,
				"OT": 100,
				"WR": 130
			},
			"weight": -0.025,
			"positions": [
				"FB",
				"HB",
				"TE",
				"WR",
				"OT",
				"G",
				"C"
			],
			"base_price": 2.5,
			"attributes": {
				"stamina": -0.25,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -0.5,
				"strength": -2.25
			}
		},
		"tackle_power": {
			"name": "Power Tackling",
			"height": 0,
			"position_multiplier": {
				"DE": 90,
				"FS": 120,
				"P": 160,
				"K": 160,
				"CB": 130,
				"LB": 95,
				"SS": 100,
				"DT": 90
			},
			"positions": [
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS",
				"K",
				"P"
			],
			"weight": -0.05,
			"base_price": 2,
			"attributes": {
				"stamina": 0,
				"awareness": 0,
				"speed": -0.25,
				"agility": 0,
				"confidence": -0.75,
				"strength": -2
			}
		},
		"pass_block_technique": {
			"name": "Pass Blk Tech",
			"height": -0.5,
			"full_name": "Pass Blocking Technique",
			"position_multiplier": {
				"C": 100,
				"TE": 110,
				"HB": 130,
				"FB": 120,
				"G": 100,
				"OT": 90
			},
			"weight": 0.025,
			"positions": [
				"FB",
				"HB",
				"TE",
				"OT",
				"G",
				"C"
			],
			"base_price": 2.5,
			"attributes": {
				"stamina": 0,
				"awareness": -0.5,
				"speed": -0.5,
				"agility": -1.75,
				"confidence": 0,
				"strength": -0.25
			}
		},
		"tackle_awareness": {
			"name": "Pursuit",
			"height": -0.5,
			"position_multiplier": {
				"DE": 115,
				"FS": 90,
				"P": 150,
				"K": 150,
				"CB": 95,
				"LB": 100,
				"SS": 90,
				"DT": 125
			},
			"positions": [
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS",
				"K",
				"P"
			],
			"weight": 0,
			"base_price": 1,
			"attributes": {
				"stamina": 0,
				"awareness": -2.7,
				"speed": 0,
				"agility": 0,
				"confidence": -0.3,
				"strength": 0
			}
		},
		"break_run_block": {
			"name": "Break Run Blk",
			"height": -0.25,
			"full_name": "Breaking Run Blocks",
			"position_multiplier": {
				"DE": 105,
				"LB": 95,
				"FS": 120,
				"CB": 130,
				"SS": 110,
				"DT": 100
			},
			"weight": 0.025,
			"positions": [
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS"
			],
			"base_price": 2,
			"attributes": {
				"stamina": 0,
				"awareness": -0.35,
				"speed": -0.35,
				"agility": -2,
				"confidence": -0.3,
				"strength": 0
			}
		},
		"conditioning": {
			"name": "Conditioning",
			"height": 0,
			"position_multiplier": {
				"FS": 100,
				"TE": 110,
				"HB": 100,
				"K": 180,
				"CB": 100,
				"FB": 110,
				"LB": 105,
				"C": 130,
				"SS": 105,
				"DT": 130,
				"DE": 120,
				"P": 180,
				"QB": 130,
				"G": 125,
				"OT": 120,
				"WR": 110
			},
			"positions": [
				"QB",
				"FB",
				"HB",
				"TE",
				"WR",
				"OT",
				"G",
				"C",
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS",
				"K",
				"P"
			],
			"weight": 0.05,
			"base_price": 1.25,
			"attributes": {
				"stamina": -2.9,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -0.1,
				"strength": 0
			}
		},
		"tackle_technique": {
			"name": "Tackling Tech",
			"height": -0.5,
			"full_name": "Tackling Technique",
			"position_multiplier": {
				"DE": 100,
				"FS": 100,
				"P": 140,
				"K": 140,
				"CB": 100,
				"LB": 90,
				"SS": 110,
				"DT": 110
			},
			"weight": 0.05,
			"positions": [
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS",
				"K",
				"P"
			],
			"base_price": 1,
			"attributes": {
				"stamina": -0.25,
				"awareness": -0.5,
				"speed": 0,
				"agility": -1.75,
				"confidence": -0.25,
				"strength": -0.25
			}
		},
		"catch_hands": {
			"name": "Receiving Hands",
			"height": -0.5,
			"position_multiplier": {
				"TE": 105,
				"HB": 110,
				"FB": 120,
				"WR": 100
			},
			"positions": [
				"FB",
				"HB",
				"TE",
				"WR"
			],
			"weight": 0.025,
			"base_price": 1.75,
			"attributes": {
				"stamina": 0,
				"awareness": -1,
				"speed": 0,
				"agility": -0.75,
				"confidence": -1,
				"strength": -0.25
			}
		},
		"catch_grip": {
			"name": "Receiving Grip",
			"height": 0.75,
			"position_multiplier": {
				"TE": 90,
				"HB": 100,
				"FB": 100,
				"WR": 130
			},
			"positions": [
				"FB",
				"HB",
				"TE",
				"WR"
			],
			"weight": -0.05,
			"base_price": 1.75,
			"attributes": {
				"stamina": -0.25,
				"awareness": -0.25,
				"speed": 0,
				"agility": 0,
				"confidence": -1,
				"strength": -1.5
			}
		},
		"return_awareness": {
			"name": "Return Awr",
			"height": 0,
			"full_name": "Return Awareness",
			"position_multiplier": {
				"FS": 130,
				"TE": 120,
				"HB": 100,
				"CB": 110,
				"FB": 120,
				"SS": 150,
				"WR": 100
			},
			"weight": 0,
			"positions": [
				"FB",
				"HB",
				"TE",
				"WR",
				"CB",
				"FS",
				"SS"
			],
			"base_price": 1.5,
			"attributes": {
				"stamina": 0,
				"awareness": -3,
				"speed": 0,
				"agility": 0,
				"confidence": 0,
				"strength": 0
			}
		},
		"man_coverage_awareness": {
			"name": "Man Awareness",
			"height": 0,
			"full_name": "Man Coverage Awareness",
			"position_multiplier": {
				"LB": 115,
				"FS": 110,
				"CB": 90,
				"SS": 120
			},
			"weight": 0,
			"positions": [
				"LB",
				"CB",
				"FS",
				"SS"
			],
			"base_price": 1,
			"attributes": {
				"stamina": 0,
				"awareness": -3,
				"speed": 0,
				"agility": 0,
				"confidence": 0,
				"strength": 0
			}
		},
		"pass_consistency": {
			"name": "Pass Consistency",
			"height": 0,
			"position_multiplier": {
				"QB": 100
			},
			"positions": [
				"QB"
			],
			"weight": 0,
			"base_price": 2.5,
			"attributes": {
				"stamina": -0.3,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -2.7,
				"strength": 0
			}
		},
		"footwork": {
			"name": "Footwork",
			"height": 0.5,
			"position_multiplier": {
				"FS": 90,
				"TE": 105,
				"HB": 100,
				"K": 140,
				"CB": 95,
				"FB": 105,
				"LB": 100,
				"C": 115,
				"SS": 100,
				"DT": 120,
				"DE": 110,
				"P": 140,
				"QB": 100,
				"G": 100,
				"OT": 95,
				"WR": 100
			},
			"positions": [
				"QB",
				"FB",
				"HB",
				"TE",
				"WR",
				"OT",
				"G",
				"C",
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS",
				"K",
				"P"
			],
			"weight": 0.025,
			"base_price": 2.25,
			"attributes": {
				"stamina": 0,
				"awareness": -0.25,
				"speed": 0,
				"agility": -2.5,
				"confidence": -0.25,
				"strength": 0
			}
		},
		"punt_hands": {
			"name": "Punt Hands",
			"height": -0.25,
			"position_multiplier": {
				"P": 100
			},
			"positions": [
				"P"
			],
			"weight": 0,
			"base_price": 2,
			"attributes": {
				"stamina": 0,
				"awareness": -1.75,
				"speed": 0,
				"agility": -1,
				"confidence": -0.25,
				"strength": 0
			}
		},
		"intimidation": {
			"name": "Intimidation",
			"height": -0.25,
			"position_multiplier": {
				"FS": 130,
				"TE": 110,
				"HB": 130,
				"K": 190,
				"CB": 150,
				"FB": 100,
				"LB": 90,
				"C": 100,
				"SS": 110,
				"DT": 90,
				"DE": 90,
				"P": 180,
				"QB": 140,
				"G": 100,
				"OT": 100,
				"WR": 150
			},
			"positions": [
				"QB",
				"FB",
				"HB",
				"TE",
				"WR",
				"OT",
				"G",
				"C",
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS",
				"K",
				"P"
			],
			"weight": -0.05,
			"base_price": 2,
			"attributes": {
				"stamina": -0.5,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -1.5,
				"strength": -1
			}
		},
		"zone_coverage_awareness": {
			"name": "Zone Awareness",
			"height": 0,
			"full_name": "Zone Coverage Awareness",
			"position_multiplier": {
				"LB": 100,
				"FS": 90,
				"CB": 110,
				"SS": 90
			},
			"weight": 0,
			"positions": [
				"LB",
				"CB",
				"FS",
				"SS"
			],
			"base_price": 1,
			"attributes": {
				"stamina": 0,
				"awareness": -3,
				"speed": 0,
				"agility": 0,
				"confidence": 0,
				"strength": 0
			}
		},
		"pass_power": {
			"name": "Pass Power",
			"height": 0,
			"position_multiplier": {
				"QB": 100
			},
			"positions": [
				"QB"
			],
			"weight": 0,
			"base_price": 3.5,
			"attributes": {
				"stamina": 0,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -0.25,
				"strength": -2.75
			}
		},
		"pass_rush_deflection": {
			"name": "Pass Rush Defl",
			"height": -0.5,
			"full_name": "Pass Rush Deflection",
			"position_multiplier": {
				"DE": 110,
				"LB": 100,
				"FS": 140,
				"CB": 140,
				"SS": 130,
				"DT": 115
			},
			"weight": 0.025,
			"positions": [
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS"
			],
			"base_price": 1.75,
			"attributes": {
				"stamina": 0,
				"awareness": -2,
				"speed": 0,
				"agility": -1,
				"confidence": 0,
				"strength": 0
			}
		},
		"quickness": {
			"name": "Quickness",
			"height": 0,
			"position_multiplier": {
				"FS": 100,
				"TE": 120,
				"HB": 100,
				"K": 120,
				"CB": 95,
				"FB": 120,
				"LB": 100,
				"C": 140,
				"SS": 110,
				"DT": 130,
				"DE": 110,
				"P": 120,
				"QB": 120,
				"G": 130,
				"OT": 110,
				"WR": 95
			},
			"positions": [
				"QB",
				"FB",
				"HB",
				"TE",
				"WR",
				"OT",
				"G",
				"C",
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS",
				"K",
				"P"
			],
			"weight": 0.05,
			"base_price": 3.2,
			"attributes": {
				"stamina": 0,
				"awareness": 0,
				"speed": -0.1,
				"agility": -2.9,
				"confidence": 0,
				"strength": 0
			}
		},
		"balance": {
			"name": "Balance",
			"height": 0.5,
			"position_multiplier": {
				"FS": 110,
				"TE": 110,
				"HB": 100,
				"K": 140,
				"CB": 120,
				"FB": 100,
				"LB": 100,
				"C": 95,
				"SS": 100,
				"DT": 100,
				"DE": 110,
				"P": 140,
				"QB": 120,
				"G": 100,
				"OT": 110,
				"WR": 120
			},
			"positions": [
				"QB",
				"FB",
				"HB",
				"TE",
				"WR",
				"OT",
				"G",
				"C",
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS",
				"K",
				"P"
			],
			"weight": -0.05,
			"base_price": 1.5,
			"attributes": {
				"stamina": 0,
				"awareness": 0,
				"speed": 0,
				"agility": -2.25,
				"confidence": -0.75,
				"strength": 0
			}
		},
		"vertical": {
			"name": "Vertical",
			"height": -0.25,
			"position_multiplier": {
				"FS": 90,
				"TE": 100,
				"HB": 110,
				"K": 130,
				"CB": 90,
				"FB": 120,
				"LB": 110,
				"C": 150,
				"SS": 110,
				"DT": 140,
				"DE": 135,
				"P": 130,
				"QB": 130,
				"G": 150,
				"OT": 140,
				"WR": 90
			},
			"positions": [
				"FB",
				"HB",
				"TE",
				"WR",
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS"
			],
			"weight": 0.03,
			"base_price": 2,
			"attributes": {
				"stamina": 0,
				"awareness": 0,
				"speed": 0,
				"agility": -2.5,
				"confidence": -0.5,
				"strength": 0
			}
		},
		"pass_carry_power": {
			"name": "Drop Back Power",
			"height": 0,
			"position_multiplier": {
				"QB": 100
			},
			"positions": [
				"QB"
			],
			"weight": -0.025,
			"base_price": 2,
			"attributes": {
				"stamina": -0.5,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -1,
				"strength": -1.5
			}
		},
		"punt_accuracy": {
			"name": "Punt Accuracy",
			"height": 0,
			"position_multiplier": {
				"P": 100
			},
			"positions": [
				"P"
			],
			"weight": 0.025,
			"base_price": 4,
			"attributes": {
				"stamina": 0,
				"awareness": -1,
				"speed": 0,
				"agility": -1.75,
				"confidence": -0.25,
				"strength": 0
			}
		},
		"hold_ground": {
			"name": "Hold Ground",
			"height": 0.25,
			"position_multiplier": {
				"DE": 95,
				"LB": 100,
				"FS": 115,
				"CB": 140,
				"SS": 100,
				"DT": 90
			},
			"positions": [
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS"
			],
			"weight": -0.025,
			"base_price": 2,
			"attributes": {
				"stamina": 0,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -1,
				"strength": -2
			}
		},
		"kickoff_power": {
			"name": "Kickoff Power",
			"height": 0,
			"position_multiplier": {
				"K": 100
			},
			"positions": [
				"K"
			],
			"weight": -0.025,
			"base_price": 2.5,
			"attributes": {
				"stamina": 0,
				"awareness": 0,
				"speed": -0.5,
				"agility": 0,
				"confidence": -0.5,
				"strength": -2
			}
		},
		"pass_awareness": {
			"name": "Pass Awareness",
			"height": -0.25,
			"full_name": "Passing Awareness",
			"position_multiplier": {
				"QB": 100
			},
			"weight": 0,
			"positions": [
				"QB"
			],
			"base_price": 2.75,
			"attributes": {
				"stamina": 0,
				"awareness": -3,
				"speed": 0,
				"agility": 0,
				"confidence": 0,
				"strength": 0
			}
		},
		"blitz_awareness": {
			"name": "Blitz Awr",
			"height": 0,
			"full_name": "Blitz Awareness",
			"position_multiplier": {
				"DE": 110,
				"LB": 90,
				"FS": 115,
				"CB": 130,
				"SS": 100,
				"DT": 110
			},
			"weight": 0,
			"positions": [
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS"
			],
			"base_price": 1,
			"attributes": {
				"stamina": 0,
				"awareness": -3,
				"speed": 0,
				"agility": 0,
				"confidence": 0,
				"strength": 0
			}
		},
		"carry_power": {
			"name": "Power Running",
			"height": 0,
			"position_multiplier": {
				"TE": 100,
				"HB": 100,
				"QB": 150,
				"FB": 90,
				"WR": 140
			},
			"positions": [
				"QB",
				"FB",
				"HB",
				"TE",
				"WR"
			],
			"weight": -0.05,
			"base_price": 4.25,
			"attributes": {
				"stamina": -0.5,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -0.5,
				"strength": -2
			}
		},
		"pass_block_power": {
			"name": "Pass Blk Power",
			"height": 0.5,
			"full_name": "Pass Blocking Power",
			"position_multiplier": {
				"C": 100,
				"TE": 120,
				"HB": 150,
				"FB": 120,
				"G": 95,
				"OT": 95
			},
			"weight": -0.025,
			"positions": [
				"FB",
				"HB",
				"TE",
				"OT",
				"G",
				"C"
			],
			"base_price": 2.5,
			"attributes": {
				"stamina": -0.5,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -0.5,
				"strength": -2
			}
		},
		"catch_awareness": {
			"name": "Rec Awareness",
			"height": -0.25,
			"full_name": "Receiving Awareness",
			"position_multiplier": {
				"TE": 100,
				"HB": 115,
				"FB": 120,
				"WR": 100
			},
			"weight": 0,
			"positions": [
				"FB",
				"HB",
				"TE",
				"WR"
			],
			"base_price": 1.25,
			"attributes": {
				"stamina": 0,
				"awareness": -3,
				"speed": 0,
				"agility": 0,
				"confidence": 0,
				"strength": 0
			}
		},
		"kick_accuracy": {
			"name": "Kick Accuracy",
			"height": 0,
			"position_multiplier": {
				"K": 100
			},
			"positions": [
				"K"
			],
			"weight": 0.025,
			"base_price": 4,
			"attributes": {
				"stamina": 0,
				"awareness": -1,
				"speed": 0,
				"agility": -1.75,
				"confidence": -0.25,
				"strength": 0
			}
		},
		"pass_grip": {
			"name": "Drop Back Grip",
			"height": 0.25,
			"position_multiplier": {
				"QB": 100
			},
			"positions": [
				"QB"
			],
			"weight": -0.025,
			"base_price": 2,
			"attributes": {
				"stamina": -0.4,
				"awareness": -0.1,
				"speed": 0,
				"agility": 0,
				"confidence": -0.8,
				"strength": -1.7
			}
		},
		"run_block_technique": {
			"name": "Run Blk Tech",
			"height": -0.5,
			"full_name": "Run Blocking Technique",
			"position_multiplier": {
				"C": 95,
				"TE": 100,
				"HB": 110,
				"FB": 100,
				"G": 90,
				"OT": 100,
				"WR": 120
			},
			"weight": 0.025,
			"positions": [
				"FB",
				"HB",
				"TE",
				"WR",
				"OT",
				"G",
				"C"
			],
			"base_price": 2.5,
			"attributes": {
				"stamina": 0,
				"awareness": -0.25,
				"speed": 0,
				"agility": -2,
				"confidence": -0.25,
				"strength": -0.5
			}
		},
		"heart": {
			"name": "Heart",
			"height": 0,
			"position_multiplier": {
				"FS": 110,
				"TE": 110,
				"HB": 100,
				"K": 100,
				"CB": 110,
				"FB": 110,
				"LB": 95,
				"C": 100,
				"SS": 100,
				"DT": 95,
				"DE": 100,
				"P": 100,
				"QB": 90,
				"G": 100,
				"OT": 100,
				"WR": 115
			},
			"positions": [
				"QB",
				"FB",
				"HB",
				"TE",
				"WR",
				"OT",
				"G",
				"C",
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS",
				"K",
				"P"
			],
			"weight": 0,
			"base_price": 2,
			"attributes": {
				"stamina": 0,
				"awareness": 0,
				"speed": 0,
				"agility": 0,
				"confidence": -3,
				"strength": 0
			}
		},
		"catch_in_traffic": {
			"name": "Catch in Traffic",
			"height": -0.5,
			"full_name": "Catching in Traffic",
			"position_multiplier": {
				"TE": 100,
				"HB": 110,
				"FB": 120,
				"WR": 115
			},
			"weight": -0.05,
			"positions": [
				"FB",
				"HB",
				"TE",
				"WR"
			],
			"base_price": 1.75,
			"attributes": {
				"stamina": 0,
				"awareness": -0.25,
				"speed": 0,
				"agility": 0,
				"confidence": -1.25,
				"strength": -1.5
			}
		},
		"coverage_technique": {
			"name": "Coverage Tech",
			"height": 0,
			"full_name": "Coverage Technique",
			"position_multiplier": {
				"LB": 120,
				"FS": 100,
				"CB": 90,
				"SS": 110
			},
			"weight": 0.05,
			"positions": [
				"LB",
				"CB",
				"FS",
				"SS"
			],
			"base_price": 1.5,
			"attributes": {
				"stamina": 0,
				"awareness": -0.5,
				"speed": -0.5,
				"agility": -1.75,
				"confidence": -0.25,
				"strength": 0
			}
		},
		"lead_block_awareness": {
			"name": "Lead Blk Awr",
			"height": 0,
			"full_name": "Lead Block Awareness",
			"position_multiplier": {
				"TE": 110,
				"HB": 120,
				"FB": 90,
				"G": 100,
				"OT": 115
			},
			"weight": 0,
			"positions": [
				"FB",
				"HB",
				"TE",
				"OT",
				"G"
			],
			"base_price": 1.3,
			"attributes": {
				"stamina": 0,
				"awareness": -2.5,
				"speed": -0.25,
				"agility": -0.25,
				"confidence": 0,
				"strength": 0
			}
		},
		"tackle_grip": {
			"name": "Tackling Grip",
			"height": 0.5,
			"position_multiplier": {
				"DE": 100,
				"FS": 110,
				"P": 140,
				"K": 140,
				"CB": 125,
				"LB": 100,
				"SS": 100,
				"DT": 100
			},
			"positions": [
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS",
				"K",
				"P"
			],
			"weight": 0.025,
			"base_price": 1,
			"attributes": {
				"stamina": -0.25,
				"awareness": 0,
				"speed": 0,
				"agility": -0.25,
				"confidence": -1,
				"strength": -1.5
			}
		},
		"sprinting": {
			"name": "Sprinting",
			"height": 0,
			"position_multiplier": {
				"FS": 95,
				"TE": 110,
				"HB": 100,
				"K": 130,
				"CB": 90,
				"FB": 115,
				"LB": 110,
				"C": 140,
				"SS": 110,
				"DT": 130,
				"DE": 115,
				"P": 130,
				"QB": 120,
				"G": 135,
				"OT": 125,
				"WR": 90
			},
			"positions": [
				"QB",
				"FB",
				"HB",
				"TE",
				"WR",
				"OT",
				"G",
				"C",
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS",
				"K",
				"P"
			],
			"weight": 0.05,
			"base_price": 3.4,
			"attributes": {
				"stamina": 0,
				"awareness": 0,
				"speed": -3,
				"agility": 0,
				"confidence": 0,
				"strength": 0
			}
		},
		"pass_rush_technique": {
			"name": "Pass Rush Tech",
			"height": -0.25,
			"full_name": "Pass Rush Technique",
			"position_multiplier": {
				"DE": 95,
				"LB": 110,
				"FS": 140,
				"CB": 140,
				"SS": 120,
				"DT": 110
			},
			"weight": 0.05,
			"positions": [
				"DT",
				"DE",
				"LB",
				"CB",
				"FS",
				"SS"
			],
			"base_price": 2,
			"attributes": {
				"stamina": 0,
				"awareness": -0.3,
				"speed": -0.8,
				"agility": -1.9,
				"confidence": 0,
				"strength": 0
			}
		},
		"coverage_deflection": {
			"name": "Deflecting",
			"height": -0.5,
			"position_multiplier": {
				"LB": 115,
				"FS": 100,
				"CB": 95,
				"SS": 110
			},
			"positions": [
				"LB",
				"CB",
				"FS",
				"SS"
			],
			"weight": 0.025,
			"base_price": 2,
			"attributes": {
				"stamina": 0,
				"awareness": -0.75,
				"speed": 0,
				"agility": -1.75,
				"confidence": -0.25,
				"strength": -0.25
			}
		}
	}
				# Defines the character builder
	def build(self):
		dict = {}
		for key in self.skills.keys():
			d = self.skills[key]
			try:
				multiplier = d['position_multiplier'][self.player['position']]
			except:
				continue
			attributes = d['attributes']
			name = d['name']
			# Attributes
			attr = [(self.player['attributes'][attr_key]**1.3)*attributes[attr_key] for attr_key in attributes.keys()]
			attr_sum = sum(attr)
			# Traits
			traits_mod = 0
			for trait in self.player['traits']:
				try: 
					this_trait = trait['skill_modifiers'][key]['max']
					traits_mod+=this_trait
				except:
					continue
			# Base Position Cost
			base = (100 - multiplier) * 0.4
			# Height/Weight modifiers
			physio = ((d['weight'] * self.player['weight']) * 0.25) + ((d['height'] * (self.player['height'] - 66)) * 0.5)
			# Calculating the max
			max = round(33 - attr_sum + traits_mod + base - physio)
			if max > 100:
				max = 100;
			elif max < 25:
				max = 25
			dict[name] = max
		return dict
	# This prints a pretty list of your build (:
	def pretty(self):
		builder = self.build()
		for (k,v) in sorted(builder.items(), key=lambda x: x[0]):
			print(k + ': ' + str(v))
	# Set your builds to variables using the build method, run this compare (:
	def compare(build, *args):
		for attr in sorted(build.keys()):
			attr_mod = '%s: %s' % (attr, build[attr])
			for diff in args:
				attr_mod+= ' | %s' % diff[attr]
			if build[attr] != diff[attr]:
				print('#',attr_mod)
			else:
				print(attr_mod)

#dt1 = glb2calc('DT', '60', 300, 'Quick Reaction', 'Run Stuffer', 'Dread-nought', speed=5, agility=9, confidence=2, awareness=6, strength=8, stamina=5).build()
#dt3 = glb2calc('DT', '60', 330, 'Quick Reaction', 'Run Stuffer', 'Dread-nought', speed=5, agility=9, confidence=2, awareness=6, strength=8, stamina=5).build()
#glb2calc.compare(dt1, dt3)

#te1 = glb2calc('TE', '68', '268', 'Receiving Specialist', 'Egotist', 'Workhorse', confidence=8, strength=1, stamina=5, speed=7, agility=8, awareness=6).build()
#te2 = glb2calc('TE', '68', '268', 'Receiving Specialist', 'Egotist', 'Workhorse', confidence=8, strength=1, stamina=5, speed=7, agility=7, awareness=7).build()
#glb2calc.compare(te1, te2)

#de1 = glb2calc('DE', '62', '280', 'Technique Man', 'Workhorse', 'Pass Rusher', stamina=3, confidence=3, agility=10, speed=6, strength=7, awareness=6).build()
#de2 = glb2calc('DE', '62', '280', 'Technique Man', 'Workhorse', 'Pass Rusher', stamina=3, strength=7, agility=10, speed=6, awareness=6, confidence=3).build()
#glb2calc.compare(de1, de2)

#k1 = glb2calc('K', '65', '178', 'Easy Going', 'Sharp Shooter', 'Cool Headed', stamina=1, speed=1, agility=10, strength=6, awareness=10, confidence=7).build()
#k2 = glb2calc('K', '65', '178', 'Easy Going', 'Sharp Shooter', 'Cool Headed', stamina=1, speed=1, agility=10, strength=7, confidence=6, awareness=10).build()
#k3 = glb2calc('K', '65', '178', 'Easy Going', 'Sharp Shooter', 'Cool Headed', stamina=1, speed=1, agility=10, strength=10, awareness=8).build()
#glb2calc.compare(k1, k2)

#lb1 = glb2calc('LB', '62', 256, 'Middle Man', 'Sure Tackler', 'Workhorse', stamina=3, speed=8, confidence=3, agility=8, strength=7, awareness=6).build()
#lb2 = glb2calc('LB', '62', 256, 'Middle Man', 'Sure Tackler', 'Workhorse', stamina=3, speed=8, confidence=3, agility=9, strength=6, awareness=6).build()
#
#glb2calc.compare(lb1, lb2)

#kr1 = glb2calc('WR', '58', 165, 'Speedster', 'Egotist', 'Workhorse', speed=8, agility=7, strength=1, awareness=7, confidence=7).build()
#kr2 = glb2calc('WR', '58', 165, 'Speedster', 'Egotist', 'Workhorse', speed=8, agility=7).build()
#glb2calc.compare(kr1, kr2)

#wr1 = glb2calc('WR', '66', 195, 'Workhorse', 'Soft Hands', 'Slot Receiver', stamina=3, agility=8, awareness=9, confidence=9, strength=3, speed=3).build()
#wr2 = glb2calc('WR', '66', 210, 'Workhorse', 'Soft Hands', 'Slot Receiver', stamina=3, agility=8, awareness=10, confidence=10, speed=1, strength=3).build()
#wr3 = glb2calc('WR', '66', 210, 'Workhorse', 'Soft Hands', 'Slot Receiver', stamina=3, agility=8, awareness=10, confidence=10, speed=2, strength=2).build()
#wr4 = glb2calc('WR', '66', 195, 'Shifty', 'Egotist', 'Workhorse').build()
#wr5 = glb2calc('WR', '66', 235, 'Shifty', 'Egotist', 'Workhorse').build()
#glb2calc.compare(wr1, wr2, wr3)

#cb1 = glb2calc('CB', '63', '184', 'Man Specialist', 'Shutdown Defender', 'Workhorse', agility=10, awareness=9, strength=1, stamina=3, speed=7).build()
#cb2 = glb2calc('CB', '63', '184', 'Man Specialist', 'Shutdown Defender', 'Workhorse', agility=10, awareness=10, strength=1, stamina=3, speed=6).build()
#glb2calc.compare(cb1, cb2)

## glb2calc('CB', '63', '184', 'Man Specialist', 'Shutdown Defender', 'Workhorse', agility=10, awareness=9, strength=1, stamina=3, speed=7).pretty()

#k1 = glb2calc('K', '65', 178, 'Kickoff King', 'Easy Going', 'Cool Headed', stamina=1, strength=10, awareness=3, agility=1, confidence=10, speed=10).build()
#k2 = glb2calc('K', '65', 228, 'Kickoff King', 'Easy Going', 'Cool Headed', stamina=1, strength=10, awareness=1, agility=3, confidence=10, speed=10).build()
#glb2calc.compare(k1, k2)

#sb1 = glb2calc('HB', '61', 224, 'Scat Back', 'Workhorse', 'Return Specialist', speed=8, stamina=3, confidence=8, strength=1, agility=8, awareness=7).build()
#sb2 = glb2calc('HB', '61', 224, 'Scat Back', 'Workhorse', 'Return Specialist', speed=8, stamina=3, confidence=7, strength=1, agility=8, awareness=8).build()
#sb3 = glb2calc('HB', '61', 224, 'Scat Back', 'Workhorse', 'Return Specialist', speed=8, stamina=3, confidence=6, strength=1, agility=9, awareness=8).build()
#glb2calc.compare(sb1, sb2, sb3)

#swr1 = glb2calc('WR', '61', 220, 'Egotist', 'Workhorse', 'Shifty', strength=1, speed=7, confidence=8, awareness=8, agility=6).build()
#swr2 = glb2calc('WR', '61', 220, 'Speedster', 'Workhorse', 'Egotist', strength=2, speed=7, stamina=5, confidence=8, awareness=7, agility=6).build()
#glb2calc.compare(swr1, swr2)

#qb1 = glb2calc('QB', '66', 201, 'Superstar', 'Tactician', 'Dual Threat', speed=9, strength=1, agility=8, awareness=7).build()
#qb2 = glb2calc('QB', '511', 201, 'Superstar', 'Workhorse', 'Dual Threat', speed=9, strength=1, agility=8, awareness=7).build()
#glb2calc.compare(qb1, qb2)

#glb2calc('WR', '66', 201, 'Shifty', 'Egotist', 'Workhorse').pretty()

ss1 = glb2calc('SS', '61', 205, 'Sure Tackler', 'Tenacious', 'Workhorse', stamina=1, speed=6, awareness=7, agility=9, strength=7).build()
ss2 = glb2calc('SS', '61', 205, 'Sure Tackler', 'Tenacious', 'Workhorse', stamina=1, speed=6, awareness=7, agility=9, strength=8, confidence=4).build()
ss3 = glb2calc('SS', '61', 205, 'Sure Tackler', 'Tenacious', 'Workhorse', stamina=1, speed=6, awareness=7, agility=9, strength=9, confidence=3).build()
ss4 = glb2calc('SS', '61', 205, 'Sure Tackler', 'Tenacious', 'Workhorse', stamina=1, speed=6, awareness=7, agility=10, strength=9, confidence=2).build()
glb2calc.compare(ss1, ss2, ss3, ss4)