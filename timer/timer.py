#!/usr/bin/python3

from time import sleep
from datetime import timedelta as TD
from datetime import datetime as DT
from sys import exit, argv
import pygame
import sqlite3

class Database:
	def __init__(self, db_file):
		self.db_file = db_file

	def connect_database(self):
		'''
		Connects to sqlite3 Database.
		'''
		try:
			conn = sqlite3.connect(self.db_file)
			cur = conn.cursor()
			return conn, cur
		except Exception as e:
			print(str(e))
			sys.exit()	

		return

	def tables(self, cur):
		cur.execute("CREATE TABLE IF NOT EXISTS	session(sitting_date TEXT, sitting_length TEXT, warm_up TEXT)")

	def add_session(self, cur, conn, sDate, sLength, warmUp):
		cur.execute('INSERT OR IGNORE INTO session(sitting_date, sitting_length, warm_up) VALUES (?, ?, ?)', (sDate, sLength, warmUp))
		conn.commit()

	def db_main(self):
		conn, cur = self.connect_database()
		self.tables(cur)
		return conn, cur

	def last_seven_days(self, cur):
		cur.execute("SELECT sitting_date, sitting_length FROM session ORDER BY sitting_date ASC LIMIT 7")
		data = cur.fetchall()
		return data

	def delete_test(self, cur, conn):
		cur.execute('DELETE FROM session WHERE sitting_length=? OR sitting_length=?', (str(TD(minutes=1)), str(TD(minutes=0))))
		conn.commit()		

class MeditationTimer(Database):

	def __init__(self, db_file):
		super().__init__(db_file)
		self.conn, self.cur = super().db_main()

	def session_input(self):
		wu_validate = False
		wu_time = 5
		length_val = False
		print(
'''
Welcome to Meditation Timer.
I have a few questions for you 
before we get started.
''')	

		while not wu_validate:
			print('''Do you need a warm up period? 
Typing "n" will give you the 
default of 5 seconds.''')
			warm_up = input('(y/n/quit): ')
			warm_up = warm_up.lower()
			if warm_up == "y":
				while not wu_validate:
					print
					wu_time = input('How long do you need? Tell me how many seconds between 0-59: ')
					check = self.interger_check(wu_time, "wu") # checks to make sure the interger is valid.
					if check:
						wu_validate = True #breaks both loops
					else:
						print("Please enter a valid number 0-59.")	

			elif warm_up == 'quit': #exits
				print('Thanks for using Meditation Timer. Bye!')
				exit()
			elif warm_up == 'n': #default 5 seconds
				wu_validate = True

			else:
				print("Please enter a valid answer.")
		print('''
[+] Alright! Sounds good! A {} second warm up.
		
How long would you like to meditate? 
For beginners I recommend anywhere 
between 10 - 20 minutes.
'''.format(wu_time))

		while not length_val:		
			
			med_length = input("How long in minutes between 1-90:")
			length_val = self.interger_check(med_length)
			if not length_val: print('Please enter a valid number.')
			print('')
		print("[+] Alright! {} minute meditation session with a {} second warm up.".format(med_length, wu_time))	
		

		return int(wu_time), int(med_length)
						

	def interger_check(self, response, period="med"):

		try:
			interger = int(response)
			
		except ValueError:
			return False

		if period == "wu":	
			if interger > 59: #This block checks the warm up time params
				return False
			elif interger < 0:
				return False	
			else:
				return True
		else:
			if interger > 90: #This block checks the meditation time params
				return False
			elif interger < 1:
				return False
			else:
				return True							

	def entry(self):
		entry_dict = {
		"sDate": DT.strftime(DT.now(), '%Y/%m/%d %I:%M %p'),
		"sLength": "",
		"warmUp": "",
		"cur": "",
		"conn": ""
		}
		return entry_dict			

	def timer(self):

		warm_up, med_length = self.session_input()
		
		td_length_remaining = TD(minutes=int(med_length))
		print('')
		start= input("Push any key to start. Push Ctrl-C to exit.")
		entry = self.entry()
		entry["conn"], entry["cur"] = self.conn, self.cur
		
		
		try:	
			if warm_up != 0: #checks if warm_up is non-zero number
				print("Warm up start!")
				while warm_up != 0: #keeps looping until warm_up is 0
				
					warm_string = str(TD(seconds = int(warm_up))) #converts to human readable
					print (warm_string, end ='\r')
					warm_up -= 1 #deincriments by 1
					
					sleep(1) #sleeps so it doesn't run through micro seconds printing same thing.
				entry['warmUp'] = warm_string	
		except KeyboardInterrupt:
			exit("Goodbye!")
						
		print("")
		print("Meditation time....")
		print("Push Ctrl-C to end at any time.")
		print("")
		
		try:
			sfx = self.bells("tinsha.wav", 12000)	
			while td_length_remaining != TD(hours=0, minutes=0, seconds=0):
				print(str(td_length_remaining), end='\r')
				td_length_remaining -= TD(seconds=1)
				
				sleep(1)

		except KeyboardInterrupt:
			print('')
			short_time = str(TD(minutes=int(med_length))-td_length_remaining)
			print ("You sat {} minutes".format(short_time))
			entry["sLength"] = short_time
			exit('Goodbye!')

		
		entry["sLength"] = str(TD(minutes=int(med_length)))
		self.bells("tinsha.wav", 4800)
		print("Yay! You made it!")

		super().add_session( **entry)
		sleep(5)
		self.session_records()
		

	def session_records(self):
		record = super().last_seven_days(self.cur)	
		if not record:
			print('Nobody here but us chickens!')
		else:				
			for r in record:
				print("[+] Date: {0}, Sitting Length: {1}".format(r[0], r[1]))

	def tear_down_test(self):
		super().delete_test(self.cur, self.conn)			
		
	def bells(self, soundfile, max_time):		
		pygame.init()
		sfx = pygame.mixer.Sound(soundfile)
		sfx.play(maxtime=max_time)


			
def main():
	script, command = argv
	med_timer = MeditationTimer("meditation.db")
	
	if command == "Del":
		med_timer.tear_down_test()
	elif command == "Rec":
		med_timer.session_records()
	else:	
		med_timer.timer()
	

	

	

if __name__ == "__main__":
	main()

			
