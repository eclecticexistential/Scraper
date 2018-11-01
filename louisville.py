from bs4 import BeautifulSoup
import datetime
import calendar
from time import strptime
import requests
import csv
import re
import time
import random
from pathlib import Path

links = []
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
			
def get_duplex(url):
	status = ''
	headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
	with requests.Session() as s:
		get_data = s.get(url, headers=headers)
		soup = BeautifulSoup(get_data.content, 'lxml')
		for title in soup.find_all('p', class_='result-info'):
			get_date = title.find('time', class_='result-date')
			check_day = int((get_date.text)[4:])
			if check_day < window:
				status = 'done'
				break
			check_mtn = (get_date.text)[:3]
			get_num_mtn = calendar.month_abbr[mtn]
			if check_day > window and get_num_mtn == check_mtn:
				get_link = title.find('a', class_='result-title')
				title = get_link.text
				data = [get_link.get('href'),title, get_date.text]
				links.append(data)
		print('made it')
		if status == 'done':
			return status
				
def cycle(url):
	multi = 140
	get_duplex(url)
	while multi < 2900:
		time.sleep(random.randint(2,9))
		t0 = time.time()
		end_url = '?s={0}'.format(multi)
		combo = url + end_url
		if get_duplex(combo) == 'done':
			break
		response_delay = time.time()- t0
		time.sleep(response_delay+23)
		print('NEEEEXT!')
		multi = multi + 140

def write_info(url, place):
	get_area = re.search(r"\/\/\w+", url)
	city = (get_area.group())[2:]
	cycle(url)
	csv_file = open('louisville{0}.csv'.format(place), 'w')
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(['City', 'URL', 'Title', 'DatePosted', 'Price', 'Email', 'Phone'])
	for link in links:
		csv_writer.writerow([city, link[0], link[1], link[2]])

		
#print(time.time())
#write_info('https://louisville.craigslist.org/search/roo', 'Roo')
#print(time.time())
#time.sleep(150)

my_file = Path("louisvilleApa.csv")

print(time.time())

done = False

while done == False:
	if my_file.is_file():
		done=True
		print(time.time())
	else:
		try:
			write_info('https://louisville.craigslist.org/search/apa', 'Apa')
		except:
			continue








