import random
from datetime import datetime as DT
from os import path, getcwd

#TODO: make a battle class
#TODO: Figure out admin commands

class BotFunActions:

	def __init__(self):
		pass

	def throw(self, msg):
		#!throw an apple at NICK
		#!throw a pillow to NICK
		message_list = msg.split(' ')
		message_pop = message_list.pop(0)
		now = DT.now()
		taco_tuesday = DT.strftime(now, '%A')
		message, file_name, followup = " ", " ", " "
		
		item, name = message_list[0], message_list[2]
		if 'at' in message_list:
			
			if 'lawful' in message_list or 'chaotic' in message_list or 'evil' in message_list or 'random' in message_list:
				item = item.lower()

				if item == 'lawful':
					file_name = path.join(getcwd(), 'actions', 'lawful.txt')
				elif item == 'chaotic':
					file_name = path.join(getcwd(), 'actions','chaos.txt')
				elif item == 'evil':
					file_name = path.join(getcwd(), 'actions', 'evil.txt')		
				elif item == 'random':
					if taco_tuesday == 'Tuesday':
						file_name = path.join(getcwd(),'actions', 'taco.txt')
					else:	
						rand_name = random.choice(['lawful.txt', 'chaos.txt', 'evil.txt'])
						file_name = path.join(getcwd(), 'actions', rand_name)
			
				
				with open(file_name, 'r') as action_list:
					action = [line.strip('\n') for line in action_list]
				
				rand_action = random.choice(action)
				txt_item = rand_action.split(' | ', 1)
				message = '/me throws {0} at {1}'.format(txt_item[0], name)
				followup = txt_item[1]
			else:	
				message = "/me hurls {0} so hard at {1} it is engulfed in flames.".format(item, name)
				followup = '/me Cackles'
				
		elif 'to' in message_list:
			message = "/me uses telekineses to give {0} {1}.".format(name, item)
			followup = 'There you go dear.'
	
		else:
			message = 'Your throw sytax is off the mark for sure. Format: !throw <item> at/to NICK'
			followup = 'You can let me choose too by using the Format: !throw <lawful/chaotic/evil/random> at NICK'

		return message, followup

	def insult(self, msg):
		#!insult NICK
		name = msg.split(' ', 1)[1]
		file_name = path.join(getcwd(), 'actions', 'shakey.txt')
		cols = [[] for _ in range(3)]
		with open(file_name, 'r') as insult:
			for en, line in enumerate(insult):
				cols[en % 3].append(line.strip())

		message = '{3}: Thou art a(n) {0} {1} {2}!'.format(random.choice(cols[0]), random.choice(cols[1]), random.choice(cols[2]), name)
		return message

	def time_check(self):
		now = DT.now()
		current = DT.strftime(now, "%I:%M %p %Z")
		return current


class BotAdminActions:

	def __init__(self, response):
		self.resp = response

	def kick(self):
		pass

	def ban(self):
		pass

	def kickban(self):
		pass	

	def king(self):
		pass

	def promote(self):
		pass

	def demote(self):
		pass

	def topic(self):
		pass						