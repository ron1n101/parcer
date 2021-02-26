import requests
from bs4 import BeautifulSoup
import csv

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
    articles = soup.find_all('section')[2].find_all('article')


    for item in articles:
        head = item.find('header').text.strip()
        reviews_raw = item.find('span', class_ = 'rating-count').find('a').text
        reviews = reviews_raw.replace(',', '').strip()
        write_data_to_csv((head, reviews))






def main():
    url = "https://wordpress.org/plugins/"
    print(get_data(get_html(url)))

if __name__ == "__main__":
    main()
