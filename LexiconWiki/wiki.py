from bs4 import BeautifulSoup
from translate import english, german, italian, arabic
import requests
import csv
import re
import os
import io


for word in english:
	if not os.path.exists(word):
		os.makedirs(word)


def get_data_save(folder, lang, category):
	csv_file = io.open('{0}/{1}{2}.csv'.format(folder, lang, category), 'w', encoding="utf-8-sig")
	csv_writer = csv.writer(csv_file)
	url = 'https://{0}.wikipedia.org/wiki/{1}'.format(lang, category)
	source = requests.get(url).text
	soup = BeautifulSoup(source, 'lxml')
	content = soup.find('div', {'id':'mw-content-text'})
	for item in content:
		anchor_tags = item.find_all('a', href=True)
		for a in anchor_tags:
			tots = a['href']
			find_end = len(tots)-4
			if tots[0] == '/':
				if tots[find_end:] not in ['.svg', '.jpg', '.JPG', '.png', '.PNG']:
					update_url = 'https://{0}.wikipedia.org{1}'.format(lang, tots)
					csv_writer.writerow([update_url])

					
for key, file_name in enumerate(english):
	for k, word in enumerate(english):
		if key == k:
			get_data_save(file_name, 'en', word)
	for ke, word in enumerate(german):
		if key == ke:
			get_data_save(file_name, 'de', word)
	for keyy, word in enumerate(italian):
		if key == keyy:
			get_data_save(file_name, 'it', word)
	for kkey, word in enumerate(arabic):
		if key == kkey:
			get_data_save(file_name, 'ar', word)