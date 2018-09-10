from bs4 import BeautifulSoup
import requests
import csv
import re

def runThis() :
	source = requests.get('https://www.kylottery.com/apps/draw_games/powerball/powerball_pastwinning.html').text
	soup = BeautifulSoup(source, 'lxml')
	tableAll = soup.find('table', class_="greeStyleLeftNoLines")
	csv_file = open('lot_scrape.csv', 'w')
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(tableAll.text)
		
#runThis()

infoArray = []

with open('lot_scrape.csv') as csv_file:
	reader = csv.reader(csv_file)
	for row in reader:
		for thing in row:
			infoArray.append(thing)
grouped = "".join(infoArray)
dates = re.findall(r"\d{2}/\d{2}/\d{4}",grouped)

new_text = grouped
for date in dates:
	new_text = re.sub(date, '', new_text)
	
numbersWith = re.findall(r"[^$]\d{1,2} ?-?",new_text)
numbers = []
counter = 0
oneSet = []

for num in numbersWith:
	if counter == 8:
		counter = 0
		numbers.append(oneSet)
		oneSet = []
	if counter > 5 and counter < 8:
		counter+=1
	if counter < 6:
		oneSet.append(int(num))
		counter+=1
	
for num in numbers:
	print(len(num))





















		
		

























