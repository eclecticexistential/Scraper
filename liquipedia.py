from bs4 import BeautifulSoup
import requests
import csv
import re

source = requests.get('https://liquipedia.net/fighters/Tokido/Results').text
soup = BeautifulSoup(source, 'lxml')
table = soup.find('table')
for section in table.find_all('tr'):
	for data in section.find_all('td'):
		print(data.text)