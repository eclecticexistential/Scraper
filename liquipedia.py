from bs4 import BeautifulSoup
import requests
import csv
import re

def player_lookup(name, opp):
	source = requests.get('https://liquipedia.net/fighters/{0}/Results'.format(name)).text
	soup = BeautifulSoup(source, 'lxml')
	table = soup.find('table')
	for section in table.find_all('tr'):
		for data in section.find_all('td'):
			links = data.find_all('a')
			for link in links:
				if link.text == opp:
					data = section.text
					data = data.replace('\n', ' ').replace('B3', '').replace('A3', '').replace('A1','').replace('A2','').replace('A9','')
					print(data)
					
player_lookup("Tokido","Infiltration")