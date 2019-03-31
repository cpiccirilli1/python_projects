from datetime import datetime as dt
import time

def alarm():
	now = dt.now()
	print ("What time would you like to set your alarm for?")
	alarmTime = input('Please use yyyy/mm/dd 12:00 AM/PM format.')
	alarmFormat = dt.strptime(alarmTime, '%Y/%m/%d %I:%M %p')

	while alarmFormat >= now:

		now = dt.now()
		alert = alarmFormat - now

		time.sleep(alert.total_seconds())

	print("BING BONG BING BONG BING BONG!")	

alarm()			