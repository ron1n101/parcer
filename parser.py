import requests
from bs4 import BeautifulSoup

def get_html(url: str):
    r = requests.get(url)
    if r.ok:
        return r.text


def get_data(html: str):
    soup = BeautifulSoup(html, 'lxml')
    text = soup.find('div', id='home-welcome').find('header').find('h1').text
    return text




def main():
    url = "https://wordpress.org/"
    print(get_data(get_html(url)))

if __name__ == "__main__":
    main()
