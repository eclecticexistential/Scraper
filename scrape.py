from bs4 import BeautifulSoup
import requests

source = requests.get('http://eclecticexistential.github.io/').text
soup = BeautifulSoup(source, 'lxml')
for match in soup.find_all('div', class_='col'):
    print(match.p.text)
    print()

# source = requests.get('http://eclecticexistential.github.io/').text <- get website data
# soup = BeautifulSoup(source, 'lxml') <- get data with tags
# print(soup.prettify()) <- display data with indentation

# with open('simple.html') as html_file: <- local file usage
#    soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())
# to get html indented ^
# match = soup.title
# print(match)
# ^ gets first title of page with tags
# match = soup.title.text
# print(match)
# ^ gets first title string of page
# match = soup.div <- gets first div
# match = soup.find('div') <- gets first div
# match = soup.find('div', class_='footer') <- gets div with class footer
# article = soup.find('div', class_='footer')
# headline = article.h2.a.text <- gets text of headline anchor tag (<h2><a>text</a></h2>
# summary = article.p.text <- gets div paragraph text
# for article in soup.find_all('div', class_='article'): <- gets all divs with class article

