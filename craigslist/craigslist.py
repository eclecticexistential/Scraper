from bs4 import BeautifulSoup
import datetime
import calendar
import time
import requests
import csv
import re
import random

cities = []
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
	job_links = []
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
			#consider removing from both
			pattern = re.search(r'oftware', title)
			pattern2 = re.search(r'loper', title)
			if pattern or pattern2:
				details = requests.get(get_link.get('href')).text
				job_links.append(get_link.get('href'))
	return job_links
	
def get_web(city):
	job_links = []
	url = 'https://{0}.craigslist.org/d/web-html-info-design/search/web'.format(city)
	headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
	source = requests.get(url, headers=headers).text
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
	return job_links
			
def display_info():
	get_cities()
	with open('Jobs/sofWeb.csv', 'w') as write:
		csv_writer = csv.writer(write)
		for city in cities:
			url = 'https://{0}.craigslist.org'.format(city)
			source = requests.get(url)
			sof = get_software(city)
			web = get_web(city)
			job_links = sof+web
			amount = len(job_links)
			if amount > 0:
				for link in job_links:
					csv_writer.writerow([city, link])
				time.sleep(random.randint(20,60))
	
# cd downloads/coding/python/beautifulsoup/craigslist

def read_file():
	display_info()
	returnArray = []
	with open('Jobs/final.csv', 'w') as write:
		csv_writer = csv.writer(write)
		csv_writer.writerow(['Title', 'City', 'Link'])
		with open('Jobs/sofWeb.csv', 'r') as f:
			reader = csv.reader(f)
			headers = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.8',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
			}
			for key,row in enumerate(reader):
				if len(row) > 0:
					source = requests.get(row[1], headers=headers).text
					soup = BeautifulSoup(source, 'lxml')
					data = soup.find('span', {'id':'titletextonly'})
					returnArray.append(data.text)
					links = soup.find_all('a')
					for link in links:
						href = link.get('href')
						if href not in [None,'#','/']:
							if len(href) > 15:
								if 'craigslist' not in href:
									if 'google' not in href:
										if href[0] != '/':
											returnArray.append(href)
					email = soup.find('section', {'id':'postingbody'})
					pattern = re.search(r'[a-zA-Z0-9]*@.*com', email.text)
					if pattern:
						returnArray.append(pattern.group())
				if len(returnArray) == 1:
					returnArray = []
				if len(returnArray) > 1:
					csv_writer.writerow([returnArray[0], row[0], returnArray[1]])
					returnArray = []
		
		
read_file()