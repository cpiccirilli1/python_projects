class PyBot:

	irc_conn = socket.socket()

	def __init__ (self, botnick, adminnick, server=None):
		self.nick = botnick
		self.admin = adminnick
		self.server = server
		self.exit_code = "bye " + botnick
		self.irc_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self):
		self.irc_conn.connect((self.server, 6667))
		self.irc_conn.send(bytes("USER {0} {1} {2} I am the chosen one.\n".format(self.nick, self.nick, self.nick), "UTF-8"))
		self.irc_conn.send(bytes("NICK "+self.nick+"\n", "UTF-8"))
	
	def joinchan(self, chan):
		self.irc_conn.send(bytes("JOIN " + chan + "\n", "UTF-8"))

	def pong(self):
		self.irc_conn.send(bytes("PONG :pingis\n", "UTF-8"))

	def send_msg(self, msg, target):
		self.irc_conn.send(bytes("PRIVMSG " + target + " :"+ msg + "\n", "UTF-8"))		
		
					
	def txt_loop(self, chan):
		#:[Nick]!~[hostname]@[IP Address] PRIVMSG [channel] :[message]
		self.joinchan(chan)
		name, message, channel = " ", " ", " "
		actions = bfa()

		while 1:
			irc_msg = self.irc_conn.recv(2048).decode("UTF-8")
			irc_msg = irc_msg.strip("\n\r")
			print(irc_msg)

			if irc_msg.find("PRIVMSG") != -1:
				name = irc_msg.split("!", 1)[0].strip(':')
				channel, message = irc_msg.split('PRIVMSG ', 1)[1].split(' :', 1)

			if len(name) < 17:
				if message.find("Hi " + self.nick) != -1:
					self.send_msg("Hello " + name + "!", channel)

				if message[:6].find("!pybot") != -1:
					about = "{0}: I am a fully automatic semi sentient sorceress bot who was sent from the {1}th dimension.".format(name, str(random.choice(range(100))))
					self.send_msg(msg=about, target=channel)

				if message[:6].find("!throw") != -1:
					resp, followup = actions.throw(message)
					self.send_msg(resp, channel)
					self.send_msg(followup, channel)

				if message[:8].find("!insult") != -1:
					resp = actions.insult(message)
					self.send_msg(resp, channel)

				if message[:5].find("!time") != -1:
					resp = "{0}: It is {1}".format(name, actions.time_check())
					self.send_msg(resp, channel)	 	

				if message[:5].find('!tell') != -1:
					target = message.split(' ', 1)[1]
					if target.find(' ') != -1:
						message = target.split(' ', 1)[1]
						target = target.split(' ')[0]
					else:
						target = name
						message = "Could not parse. The message should be in the format: !tell NICK MESSAGE"
					self.send_msg(msg=message, target=target)

				if message.rstrip() == self.exit_code:
					if name.lower() in admin: 
						self.send_msg("Oh, ok... bye.", channel)
						self.irc_conn(bytes("QUIT \n", "UTF-8"))
						return
					else:
						self.send_msg("You can't tell me what to do, {}!".format(name), channel)
				
				message = " "			
			else:
				if irc_msg.find("PING :") != -1:
					self.pong()		 			

	def war_loop(self, chan):
		pass				