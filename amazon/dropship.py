from bs4 import BeautifulSoup
import requests
import csv
import re
import schedule
import datetime
import time

def info_loop():
	curr_stats = datetime.datetime.now().hour
	req_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
	source = requests.get('https://www.amazon.com/Best-Sellers/zgbs',headers=req_headers).text
	soup = BeautifulSoup(source, 'lxml')
	table = soup.find('div', id='zg_left_col1')
	titles = table.find_all('h3')
	item_links = table.find_all('a', class_='a-link-normal')
	product_name = []
	product_links = []
	
	for link in item_links:
		try:
			pattern = re.search(r'/product-reviews', link['href']).group()
		except AttributeError:
			try:
				pattern = re.search(r'/[b|B]est-[s|S]ellers', link['href']).group()
			except AttributeError:
				com_link = 'https://www.amazon.com/' + link['href']
				remove = link.text
				remove = remove.replace('\n','')
				remove = remove.split(' ')
				new_array = []
				if remove[0] == '':
					for item in remove:
						if item != '':
							new_array.append(item)
				new_array = str(' '.join(new_array))
				product_name.append(new_array)
				product_links.append(com_link)
	file_name = 'topPro{0}.csv'.format(curr_stats)
	with open(file_name, 'w') as write:
		csv_writer = csv.writer(write)
		csv_writer.writerow(['Category', 'ProductName', 'Link'])
		num_prod = 0
		cat_list = 0
		while cat_list < len(titles)-2:
			cat = titles[cat_list].text
			csv_writer.writerow([cat,product_name[num_prod],product_links[num_prod]])
			num_prod += 1
			if num_prod % 3 == 0:
				cat_list += 1
	print('It is nice to see you my love <3')
	
schedule.every().hour.do(info_loop)

while True:
	schedule.run_pending()
	time.sleep(1)