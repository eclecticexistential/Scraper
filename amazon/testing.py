import schedule
import time

def info_loop():
	print('It is nice to see you my love <3')

schedule.every().minute.do(info_loop)

while True:
	schedule.run_pending()
	time.sleep(1)