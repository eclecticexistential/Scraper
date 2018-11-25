
from bs4 import BeautifulSoup
import requests
import csv
import re

source = requests.get('https://www.imdb.com/name/nm2255973/#writer').text
soup = BeautifulSoup(source, 'lxml')
table = soup.find('div',class_='filmo-category-section')
print(table)