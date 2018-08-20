import requests
from bs4 import BeautifulSoup

HTML_PARSER = 'html.parser'
YAHOO_URL = 'https://tw.yahoo.com'

def get_yahoo_news_headline():
    res = requests.get(YAHOO_URL)
    if res.status_code == requests.codes.ok:
        soup = BeautifulSoup(res.content, HTML_PARSER)
        titles = soup.find_all('span', class_='Va-tt')

        for i in range(0, len(titles), 2):
            print(titles[i].getText())


if __name__ == '__main__':
    get_yahoo_news_headline()
