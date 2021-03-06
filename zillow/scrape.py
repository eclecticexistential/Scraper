from bs4 import BeautifulSoup
import requests
import csv

current_stats = {}
page_count = []


def info_loop(url_link):
    csv_file = open('zillow_scrapeNov.csv', 'w')
    csv_writer = csv.writer(csv_file)
    current_page = 1
    get_data(url_link, current_page, csv_writer)
    end_link = url_link[-6:]
    next_link = url_link[:-6]
    if len(page_count) > 0:
        while current_page < max(page_count):
            current_page += 1
            apple = next_link
            apple += str(current_page) + "_p/" + end_link
            get_data(apple, current_page, csv_writer)
    csv_file.close()


def get_data(url_link, current_page, csv_writer):
    req_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    with requests.Session() as s:
        url = url_link
        r = s.get(url, headers=req_headers)
        soup = BeautifulSoup(r.content, 'lxml')
        prices = soup.find_all('span', {'class': 'zsg-photo-card-price'})
        data = soup.find_all('span', {'class': 'zsg-photo-card-info'})
        addresses = soup.find_all('span', {'itemprop': 'address'})
        laugh = soup.find('ol', class_="zsg-pagination")
        if laugh is not None and current_page == 1:
            joy = laugh.find_all('li')
            for giggle in joy:
                if giggle.text != "Next" and giggle.text != "...":
                    page_count.append(int(giggle.text))
        if current_page == 1:
            csv_writer.writerow(['Price', 'Info', 'Location'])
        for key, price in enumerate(prices):
            csv_writer.writerow([price.text, data[key].text, addresses[key].text])


def who_knew():
    with open('zillow_scrapeNov.csv') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)
        for row in reader:
            for key, info in enumerate(row):
                if key == 2:
                    zip_code = int(info[-3:])
                    if zip_code not in [203, 208, 210, 211, 212]:
                        # goog_search = "https://www.google.com/search?client=firefox-b-1-ab&ei=L_iEW876EoXatAXtibWABw&q=zillow+"
                        # goog_end = "&gs_l=psy-ab.3..33i299k1.1528.1528.0.2517.1.1.0.0.0.0.460.460.4-1.1.0..1..0...1..64.psy-ab..0.1.456....0.yS0H9KLqlxk"
                        # divi = info.replace(" ", "+")
                        # tot_url = divi + "&oq=zillow+"+divi
                        print(row)
                        # print(goog_search + tot_url + goog_end)


info_loop('https://www.zillow.com/homes/for_sale/KY/house,land,townhouse_type/24_rid/1-_beds/1-_baths/0-20000_price/0-68_mp/priced_sort/42.884014,-77.014161,32.481963,-92.021485_rect/5_zm/0_mmm/')
who_knew()
# source = requests.get('https://eclecticexistential.github.io').text
# soup = BeautifulSoup(source, 'lxml')
# csv_file = open('p_scrape.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Headline', 'Summary'])
# for match in soup.find_all('div', class_='col'):
#     headline = match.h3.text
#     summary = match.p.text
#     csv_writer.writerow([headline, summary])
# csv_file.close()
#
# with open('p_scrape.csv') as csv_file:
#     reader = csv.reader(csv_file)
#     for row in reader:
#         print(row)

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

