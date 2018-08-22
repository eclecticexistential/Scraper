from bs4 import BeautifulSoup
import requests, csv

source = requests.get('http://eclecticexistential.github.io/').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('p_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary'])

for match in soup.find_all('div', class_='col'):
    headline = match.h3.text
    summary = match.p.text
    csv_writer.writerow([headline, summary])

csv_file.close()

with open('p_scrape.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

# to get embedded video:
# -grab url from iframe
# vid_src = article.find("iframe", class_="youtube-player")['src']
# vid_id = vid_src.split('/')[4]
# vid_id = vid_id.split('?')[0]
# yt_link = f'https://youtube.com/watch?v={vid_id}'

# to skip by missing info put into try/except

# try:
#    source = requests.get('http://eclecticexistential.github.io/').text
#    soup = BeautifulSoup(source, 'lxml')
#    for match in soup.find_all('div', class_='col'):
#        print(match.p.text)
#        print()
# except Exception as e:
#    yt_link = None (rather than pass)

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

