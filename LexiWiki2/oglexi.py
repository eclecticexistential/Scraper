from bs4 import BeautifulSoup
import requests
import csv
import re
import io

def get_q_id(lang, word):
	url = 'https://{0}.wikipedia.org/w/index.php?title={1}&action=info'.format(lang, word)
	source = requests.get(url).text
	soup = BeautifulSoup(source, 'lxml')
	data = soup.find('a', {'class':'extiw wb-entity-link external'})
	try:
		return data.text
	except AttributeError:
		return 000   #if no QID is found default to 0   example: https://en.wiktionary.org/w/index.php?title=anarchism&action=info

def read_file(file_name):
	with open(file_name, 'rb') as f:
		x = f.readlines()
		counter = 0
		with io.open('output', 'wb') as text_file:
			for word in x:
				a = word.decode()
				language = re.search(r'https:\/\/[a-z]*',a)
				if language:
					get_1 = language.group()
					get_2 = get_1[8:]
				titles = re.search(r'title=.*"', a)
				if titles:
					get_name = titles.group()
					get_len = len(get_name)-1
					without_tag = get_name[7:get_len]
					get_Q_wiki = get_q_id(get_2, without_tag)
					## write initial tag
					line = "\n<{0} {1}>\n".format(without_tag, get_Q_wiki)
					text_file.write(line.encode())
				anchor_tags = re.search(r'<a.*?<\/a>',a)
				if anchor_tags:
					apple = anchor_tags.group()
					peanut = re.search(r'".*?"',apple)
					shelled = peanut.group()
					shelled_len = len(shelled)-1
					shell_search = shelled[1:shelled_len]
					get_wiki_data = get_q_id(get_2, shell_search)
					pear = re.search(r'>.*?<', apple)
					if pear:
						sliced = pear.group()
						pear_len = len(sliced)-1
						pear_slice = sliced[1:pear_len]
						## write word
						details = "<{0}>...".format(pear_slice)
						text_file.write(details.encode())
						## write anchor
						add_anchor = "<inline_link {0}: {1} {2}>\n".format(counter, shell_search, get_wiki_data)
						text_file.write(add_anchor.encode())
						counter += 1
				## write close tag
				end_tag = re.search(r'</doc>',a)
				if end_tag:
					end_line = "</{0}>".format(without_tag)
					text_file.write(end_line.encode())
					counter = 0
						

read_file('wiki_00') # works with any binary file