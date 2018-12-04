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

def read_file(file_name, output_file):
	with open(file_name, 'rb') as f:
		x = f.readlines()
		with io.open(output_file, 'wb') as text_file:
			for word in x:
				a = word.decode()
				language = re.search(r'https:\/\/[a-z]*',a)
				if language:
					get_1 = language.group()
					get_2 = get_1[8:]
				get_div = re.search(r'<doc .*?>', a)
				titles = re.search(r'title=.*"', a)
				if titles:
					get_name = titles.group()
					get_len = len(get_name)-1
					without_tag = get_name[7:get_len]
					get_Q_wiki = get_q_id(get_2, without_tag)
					## write initial tag
					line = "\n[{0}: {1}]\n".format(get_Q_wiki, without_tag)
					a = a.replace(get_div.group(), line)
					text_file.write(a.encode())
				anchor_tags = re.findall(r'<a.*?<\/a>',a)
				if anchor_tags:
					time = len(anchor_tags)-1
					for key,link in enumerate(anchor_tags):
						peanut = re.search(r'".*?"',link)
						shelled = peanut.group()
						shelled_len = len(shelled)-1
						shell_search = shelled[1:shelled_len]
						get_wiki_data = get_q_id(get_2, shell_search)
						## write anchor
						add_anchor = "[{0}: {1}]".format(get_wiki_data, shell_search)
						a = a.replace(link, add_anchor)
						if key == time:
							text_file.write(a.encode())
				## write close tag
				end_tag = re.search(r'</doc>',a)
				if end_tag:
					end_line = "\n"
					a = a.replace(end_tag.group(), end_line)
					text_file.write(a.encode())
						

read_file('wiki_00', 'output') # works with any binary file