
from bs4 import BeautifulSoup
import requests
import csv
import re

source = requests.get('https://www.cbcworldwide.com/properties/find').text
soup = BeautifulSoup(source, 'lxml')
table = soup.find_all('div', class_='card-body')
print(table)