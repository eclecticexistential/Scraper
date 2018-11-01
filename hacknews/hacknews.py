from bs4 import BeautifulSoup
import requests
import csv
import re

python = []
selenium = []
react = []

def get_python(name, array):
	source = requests.get('https://news.ycombinator.com/item?id=18354503').text
	soup = BeautifulSoup(source, 'lxml')
	for group in soup.find_all('span', class_='commtext c00'):
		if group.findAll(text=re.compile('REMOTE')) or group.findAll(text=re.compile('remote')):
			if group.findAll(text=re.compile(name)):
				array.append(group.text)
	csv_file = open('{0}Nov.csv'.format(name), 'w')
	csv_writer = csv.writer(csv_file)
	if array != []:
		for pos in array:
			try:
				csv_writer.writerow([pos])
			except:
				continue
		
get_python('ython', python)
get_python('elenium', selenium)
get_python('eact', react)