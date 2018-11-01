from bs4 import BeautifulSoup
import datetime
import calendar
from time import strptime
import requests
import csv
import re

cities = []
job_links = []
date = datetime.datetime.today().strftime('%m-%d')
day = int(date.replace('-','')[2:])
mtn = int(date.replace('-','')[:2])

if day > 7:
	window = day - 7
elif day <= 7:
	get_end = 31 - day
	if mtn not in [2,4,9,11]:
		if day != 1:
			window = [range(1,day), range(get_end,32)]
		else: 
			window = [day, range(get_end,32)]
	if mtn not in [1,2,3,5,7,8,10,12]:
		if day != 1:
			window = [range(1,day), range(get_end,31)] 
		else: 
			window = [day, range(get_end,31)]
	if mtn == 2:
		if day != 1:
			[range(1,day), range(get_end,29)]
		else: 
			window = [day, range(get_end,29)]
			

def get_cities():
	with open('cities.csv') as csv_file:
		reader = csv.reader(csv_file)
		for row in reader:
			for city in row:
				if city != 'municipios':
					cities.append(city)
			
def get_software(city):
	url = 'https://{0}.craigslist.org/d/software-qa-dba-etc/search/sof'.format(city)
	source = requests.get(url).text
	soup = BeautifulSoup(source, 'lxml')
	for title in soup.find_all('p', class_='result-info'):
		get_date = title.find('time', class_='result-date')
		check_day = int((get_date.text)[4:])
		check_mtn = (get_date.text)[:3]
		get_num_mtn = calendar.month_abbr[mtn]
		if check_day > window and get_num_mtn == check_mtn:
			get_link = title.find('a', class_='result-title')
			title = get_link.text
			pattern = re.search(r'oftware', title)
			pattern2 = re.search(r'loper', title)
			if pattern or pattern2:
				details = requests.get(get_link.get('href')).text
				job_links.append(get_link.get('href'))
	
def get_web(city):
	url = 'https://{0}.craigslist.org/d/web-html-info-design/search/web'.format(city)
	source = requests.get(url).text
	soup = BeautifulSoup(source, 'lxml')
	for title in soup.find_all('p', class_='result-info'):
		get_date = title.find('time', class_='result-date')
		check_day = int((get_date.text)[4:])
		check_mtn = (get_date.text)[:3]
		get_num_mtn = calendar.month_abbr[mtn]
		if check_day > window and get_num_mtn == check_mtn:
			get_link = title.find('a', class_='result-title')
			title = get_link.text
			pattern = re.search(r'loper', title)
			if pattern:
				job_links.append(get_link.get('href'))
			
def display_info():
	get_cities()
	for city in cities:
		get_software(city)
		get_web(city)
		break
	print(job_links)
	
display_info()
	
	