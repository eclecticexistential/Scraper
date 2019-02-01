from bs4 import BeautifulSoup
import requests
import csv
import re

def get_python():
	source = requests.get('https://news.ycombinator.com/item?id=19055166').text
	soup = BeautifulSoup(source, 'lxml')
	csv_file = open('remoteJan.csv', 'w')
	csv_writer = csv.writer(csv_file)
	for group in soup.find_all('span', class_='commtext c00'):
		if group.findAll(text=re.compile('REMOTE')) or group.findAll(text=re.compile('remote')):
			try:
				csv_writer.writerow([group.text])
			except UnicodeEncodeError:
				apple = group.text
				apple = apple.replace('\u2028', '').replace('\u200b', '')
				try:
					csv_writer.writerow([apple])
				except UnicodeEncodeError:
					continue
		
get_python()