from bs4 import BeautifulSoup
import requests
import csv
import re

source = requests.get('https://news.ycombinator.com/item?id=17902901').text
soup = BeautifulSoup(source, 'lxml')
for group in soup.find_all('span', class_='commtext c00'):
	if group.findAll(text=re.compile('REMOTE')) or group.findAll(text=re.compile('remote')):
		if group.findAll(text=re.compile('Python')):
			print(group.text)
			print()