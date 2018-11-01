from bs4 import BeautifulSoup
import requests
import csv
import re

def info_loop(item_name):
	cap_name = item_name.title()
	url_name = item_name.replace(' ', '+')
	url_link = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw={0}&_sacat=0&LH_TitleDesc=0&_ipg=200&_sop=15'.format(url_name)
	source = requests.get(url_link).text
	soup = BeautifulSoup(source, 'lxml')
	pages = 0
	for group in soup.find_all('li', class_='x-pagination__li'):
		pages += 1
	csv_file = open('ebay.csv', 'w')
	csv_writer = csv.writer(csv_file)
	current_page = 1
	while current_page <= pages:
		if current_page == 1:
			csv_writer.writerow(['Title', 'Price', 'Shipping', 'Description'])
			get_info(source, csv_writer, cap_name)
			current_page += 1
		if current_page > 1:
			next_page = '&_pgn={0}'.format(current_page)
			next_page_url = url_link + next_page
			source = requests.get(next_page_url).text
			get_info(source, csv_writer, cap_name)
			current_page += 1
	csv_file.close()

def get_info(source, csv_writer, item_name):
	soup = BeautifulSoup(source, 'lxml')
	for group in soup.find_all('div', class_='s-item__info'):
		for content in group.find_all('a', class_='s-item__link'):
			if content.find_all(text = re.compile(item_name)):
				price = group.find('span',class_='s-item__price')
				next_price = price.text
				next_page = requests.get(content['href']).text
				next_listing = BeautifulSoup(next_page, 'lxml')
				title = next_listing.find('h1', id='itemTitle')
				next_title = str((title.text)[16:])
				shipping = next_listing.find('span', id='fshippingCost')
				loc_ship = next_listing.find('span', id='fShippingSvc')
				next_shipping = shipping.text if shipping != None else loc_ship.text if loc_ship != None else 'No data'
				description = next_listing.find('div', class_='prodDetailSec')
				next_description = description.text if description != None else 'No data'
				try:
					csv_writer.writerow([next_title, next_price, next_shipping, next_description])
				except UnicodeEncodeError:
					update_title = next_title[2:]
					try:
						csv_writer.writerow([update_title, next_price, next_shipping, next_description])
					except:
						print(update_title, next_price, next_shipping, next_description)
info_loop('resident evil 7')