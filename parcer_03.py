import requests
from bs4 import BeautifulSoup
import csv
from pprint import pprint as pp
def get_html(url: str):
    r = requests.get(url)
    if r.ok:
        return r.text

def write_data_to_csv(data):
    with open('names.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)



def get_data(html: str):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table', class_='cmc-table')
    th_s = table.find('thead').find_all('th')
    headers_count = len(th_s)
    headers = {}

    for i, th in enumerate(th_s):
        if len(th.text) > 0:
            headers[i] = th.text
    pp(headers)

    headers = {1: '#',
               2: 'Name',
               3: 'Price',
               4: '24h',
               8: 'Circulating Supply',
               9: 'Last 7 Days'}

    tr_s = table.find('tbody').find_all('tr')

    for tr in tr_s:
        if len(tr) == headers_count:
            data = []
            for i, td in enumerate(tr):
                if i in headers:

                        data.append(td.text.replace(',', ''))
            write_data_to_csv(tuple(data))

                    # data.append(td.text)



"""
    articles = soup.find_all('section')[2].find_all('article')


    for item in articles:
        head = item.find('header').text.strip()
        reviews_raw = item.find('span', class_ = 'rating-count').find('a').text
        reviews = reviews_raw.replace(',', '').strip()
        write_data_to_csv((head, reviews))
"""





def main():
    url = "https://coinmarketcap.com/"
    print(get_data(get_html(url)))

if __name__ == "__main__":
    main()
