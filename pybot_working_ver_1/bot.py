#!/usr/bin/python3
from sys import exit
import argparse
from time import sleep
from internals import PyBot as PB


def options():
	parser = argparse.ArgumentParser('')
	parser.add_argument('-c', '--connect', action='store_true')
	parser.add_argument('--chan', nargs='?')
	parser.add_argument('-w', '--war', action='store_true')
	args = parser.parse_args()


def main():

	

	attempt = 0

	credentials = {
	'server': "chat.freenode.net",
	'channel': ["##bot-testing"],
	'botnick': "PyBot36",
	'adminname': ['seachel', 'mirage', 'sorceresschels']
	}

	while attempt < 6:
		bot = PB(server=credentials['server'], botnick=credentials['botnick'], adminnick=credentials['adminname'])
		bot.connect()
		bot.txt_loop(','.join(credentials['channel']))

		print("Sleeping for 10 seconds before reconnect.")
		sleep(10)
		attempt += 1


		

		
if __name__ == "__main__":
	main()