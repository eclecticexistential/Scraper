from translate import english, german, italian, arabic
import requests
import csv
import re
import os
import io

cwd = os.getcwd()

for folder in os.listdir(cwd):
	if not folder.endswith('.py') and not folder.endswith('.git') and not folder.endswith('.md'):
		if folder != "__pycache__":
			csv_file = io.open('{0}/{1}combined.csv'.format(folder,folder), 'w', encoding="utf-8-sig")
			csv_writer = csv.writer(csv_file)
			csv_writer.writerow(['Language', 'Word', 'URL', 'Id', 'Source'])
			for file in os.listdir(folder):
				loc = '{0}/{1}'.format(folder, file)
				lang = file[0:2]
				pos = english.index(folder)
				languages = ['en', 'de', 'ar', 'it']
				if lang in languages:
					if lang == 'en':
						translation = folder
					if lang == 'de':
						translation = german[pos]
					if lang == 'ar':
						translation = arabic[pos]
					if lang == 'it':
						translation = italian[pos]
					url = 'https://{0}.wikipedia.org/wiki/{1}'.format(lang, translation)
					with io.open(loc, encoding="utf-8-sig") as f:
						counter = 0
						for line in f:
							if len(line) != 1:
								csv_writer.writerow([lang, translation, line, counter, url])
								counter += 1

		


#English URL - German URL - Italian URL - Arabic URL - Same id/url order - Diff id/url order

#[script to read wiki page, CSV file with ordered link/ids, compare/contrast]