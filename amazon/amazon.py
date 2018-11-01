from bs4 import BeautifulSoup
import requests
import csv
import re

def info_loop(title, link):
	source = requests.get(link).text
	soup = BeautifulSoup(source, 'lxml')
	page_links = 1
	for page in soup.find_all('span', class_='pagnLink'):
		page_links += 1
	csv_file = open('amazon.csv', 'w')
	csv_writer = csv.writer(csv_file)
	current_page = 1
	while current_page <= page_links:
		if current_page == 1:
			csv_writer.writerow(['Title', 'Price', 'Description'])
			get_info(soup, csv_writer, title)
			current_page += 1
		if current_page > 1:
			next_link = 'https://www.amazon.com/s/ref=sr_pg_{0}?fst=as%3Aoff&rh=n%3A468642%2Cn%3A6427814011%2Cn%3A6427831011%2Ck%3Adragon+ball+fighter&page={0}&keywords=dragon+ball+fighter&ie=UTF8&qid=1540158933'.format(current_page)
			source = requests.get(next_link).text
			soup = BeautifulSoup(source, 'lxml')
			get_info(soup, csv_writer, title)
			current_page += 1

def get_info(soup, csv_writer, item_name):
	for group in soup.find_all('a', class_='s-access-detail-page'):
		title = group.find('h2', class_='a-size-medium')
		if title.find(text=re.compile(item_name)):
			det_link = group['href']
			next_source = requests.get(det_link).text
			soup1 = BeautifulSoup(next_source, 'lxml')
			total_price = ''
			description = []
			for spans in soup1.find_all('table', id='price'):
				if spans.find('div', id='newPrice').text != '':
					new_price = spans.find('div', id='newPrice').text
					total_price = new_price.replace('\n', '.').replace('/t', '').replace('$', '').replace('...', '')
				if spans.find('div', id='usedPrice').text != '':
					used_price = spans.find('div', id='usedPrice').text
					total_price = used_price.replace('\n', '.').replace('/t', '').replace('$', '').replace('...', '')
			data = soup1.find('div', id='feature-bullets')
			if data != None:
				for listI in data.find_all('span', class_='a-list-item'):
					des = listI.text[9:].replace('\n','').replace('\t','')
					description.append(des)
			try:
				csv_writer.writerow([title.text, total_price, description])
			except UnicodeEncodeError:
				print(title.text, total_price, description)
	
info_loop('Dragon Ball Fighter','https://www.amazon.com/s/ref=sr_nr_n_2?fst=as%3Aoff&rh=n%3A6427831011%2Ck%3Adragon+ball+fighter&keywords=dragon+ball+fighter&ie=UTF8&qid=1540158911&rnid=2941120011')