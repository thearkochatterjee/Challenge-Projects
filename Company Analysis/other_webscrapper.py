import requests
from bs4 import BeautifulSoup
import webbrowser


def getPage(company: str) -> requests.models.Response:
    # webbrowser.open('https://google.com/search?q=' + company + '&tbm=nws')
    return requests.get('https://www.google.com/search?q=' + company + '&tbm=nws')


def get_soup(page: requests.models.Response):
    return BeautifulSoup(page.content, 'lxml')

company = 'apple'
# response = requests.get('https://www.google.com/search?q=' + company + '&tbm=nws&start=0')
response = requests.get('https://news.search.yahoo.com/search?p=' + company + '&fr2=piv-web&fr=news&guccounter=1')
soup = BeautifulSoup(response.content, 'lxml')
print(soup)
# page = getPage('apple')
# print(page.url)
# soup = get_soup(page)
# h = soup.find_all('h3')
# for info in h:
#     print(info.getText())
#     print('\n\n\n')
# print(soup.prettify())
# body = soup.body
# for i in list(body.children):
#     print(i)
#     print('\n\n\n')

# for i in l:
#     print(i)
#     print('\n\n\n')
# print(len(list(body.children)))
# for link in body.find_all('a'):
#     print(link.get('href'))
# soup = get_soup(getPage('apple'))
# full_text = soup.prettify()
# full_text_arr = full_text.split('\n')
# print(full_text_arr)
# for i in range(0, len(full_text_arr)):
#     if full_text_arr[i].strip().startswith('<'):
#         print(full_text_arr[i])
#     else:
#         pass
# print(soup.select('main'))
# main = list(soup.find_all(id='main'))
# main = list(main[0].children)
# print(main[0].prettify())
# print('hi')
