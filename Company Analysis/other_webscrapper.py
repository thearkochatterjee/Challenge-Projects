import requests
from bs4 import BeautifulSoup
import webbrowser

def getPageGoogle(company: str) -> requests.models.Response:
    """
    Provides the request page for the search results of a company through google news.

    :param company: Company name to search for
    :return: Request page
    """
    return requests.get('https://www.google.com/search?q=' + company + '&tbm=nws')


def getPageYahoo(company: str) -> requests.models.Response:
    """
    Provides the request page for the search results of a company through yahoo news.

    :param company: Company name to search for
    :return: Request page
    """
    return requests.get('https://news.search.yahoo.com/search?p=' + company + '&fr2=piv-web&fr=news&guccounter=1')


def get_soup(page: requests.models.Response):
    """
    Creates soup based on page request.

    :param page: page request
    :return: soup
    """
    return BeautifulSoup(page.content, 'lxml')


def getData(company: str) -> []:
    """
    Provides the content shown in the articles for a specified company

    :param company: Company name to search for
    :return: list of urls of discovered articles, list of content from articles
    """
    soup = get_soup(getPageYahoo(company))
    links = []
    pages = []
    page_texts = []
    for link in soup.find_all('a'):
        temp = link.get('href')
        if 'yahoo.com' not in temp and len(temp) > 1 and 'yahoo.uservoice.com' not in temp and temp not in links:
            links.append(temp)
            pages.append(get_soup(requests.get(temp)))
            t = pages[-1].findAll('p')
            t2 = []
            for i in t:
                t2.append(i.text)
            page_texts.append(''.join(t2))
    soup2 = get_soup(getPageGoogle(company))
    for link in soup2.find_all('a'):
        temp = link.get('href')
        if len(temp) > 1 and 'https' in temp and '.google.com' not in temp:
            if not temp.startswith('https'):
                temp = temp[temp.index('https'):]
            if temp in links:
                continue
            links.append(temp)
            pages.append(get_soup(requests.get(temp)))
            t = pages[-1].findAll('p')
            t2 = []
            for i in t:
                t2.append(i.text)
            page_texts.append(''.join(t2))
    return links, page_texts
