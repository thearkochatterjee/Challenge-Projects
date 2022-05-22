import requests
import lxml
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
    "q": "gta san andreas",
    "hl": "en",
    "tbm": "nws",
}

print("header and params constructed")
response = requests.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen", headers=headers, params=params)
soup = BeautifulSoup(response.text, 'lxml')

print(str(response.status_code) + " is the response status code")
full_text = soup.prettify()
full_text_arr = full_text.split('\n')
for i in range(0, len(full_text_arr)):
    if full_text_arr[i][0] == "<":
        print(full_text_arr[i])
    else:
        pass

print("response found and bs call made")

count = 0
for result in soup.select('.dbsr'):
    print("result " + count + " found")
    count = count + 1
    title = result.select_one('.nDgy9d').text
    link = result.a['href']
    source = result.select_one('.WF4CUc').text
    snippet = result.select_one('.Y3v8qd').text
    date_published = result.select_one('.WG9SHc span').text
    print(f'{title}\n{link}\n{snippet}\n{date_published}\n{source}\n')
