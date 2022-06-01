import requests
from bs4 import BeautifulSoup


def getPageGoogle(company: str) -> requests.models.Response:
    # webbrowser.open('https://google.com/search?q=' + company + '&tbm=nws')
    return requests.get('https://www.google.com/search?q=' + company + '&tbm=nws')


def getPageYahoo(company: str) -> requests.models.Response:
    return requests.get('https://news.search.yahoo.com/search?p=' + company + '&fr2=piv-web&fr=news&guccounter=1')


def get_soup(page: requests.models.Response):
    return BeautifulSoup(page.content, 'lxml')


def getData(company: str) -> []:
    soup = get_soup(getPageYahoo(company))
    links = []
    pages = []
    page_texts = []
    for link in soup.find_all('a'):
        temp = link.get('href')
        if 'yahoo.com' not in temp and len(temp) > 1:
            links.append(temp)
            pages.append(get_soup(requests.get(temp)))
            t = pages[-1].findAll('p')
            t2 = []
            for i in t:
                t2.append(i.text)
            page_texts.append(''.join(t2))
            print(page_texts[-1])
    return links, page_texts

