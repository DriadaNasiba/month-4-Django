import requests
from bs4 import BeautifulSoup as BS


URL = 'https://rezka.ag/'

HEADERS ={
    "Accept": "",
    "User-Agent": "",
}

def get_html(url,params=''):
    request = requests.get(url,headers=HEADERS, params=params)
    return request

def get_data(html):
    bs = BS(html,features='html.parser')
    items = bs.find_all("div", class_='')
    rezka_list = []

    for item in items:
        title = item.find("div", class = '').get_text(strip=True)
        rezka_list.append({
            'title': title,
        })
    return rezka_list


def parsing_rezka():
    response = get_html(URL)
    if response.status_code == 200:
        rezka_list_2 = []
        for page in range(1, 2):
            response = get_html('https://rezka.ag/series/', params={'page':page})
            rezka_list_2.extend(get_data(response.text))
        return rezka_list_2
    else:
        raise Exception('error in parse')
print(parsing_rezka)



