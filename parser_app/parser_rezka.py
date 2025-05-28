import requests
from bs4 import BeautifulSoup as BS


URL = 'https://kinovibe.co/'

HEADERS ={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*,q=0.8,application/signed-exchange,v=b3;q=0.7",
    "User-Agent": "Mozila/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/136.0.0.0 Safari/537.36",
}

def get_html(url,params=''):
    request = requests.get(url,headers=HEADERS, params=params)
    return request

def get_data(html):
    bs = BS(html,features='html.parser')
    items = bs.find_all("div", class_='custem1_item')
    rezka_list = []

    for item in items:
        title = item.find("div", class_='custem1_title')
        rezka_list.append({
            'title': title,
        })
    return rezka_list


def parsing_rezka():
    response = get_html(URL)
    if response.status_code == 200:
        rezka_list_2 = []
        for page in range(1, 2):
            response = get_html('https://kinovibe.co/genrefilm/action/', params={'page':page})
            rezka_list_2.extend(get_data(response.text))
        return rezka_list_2
    else:
        raise Exception('error in parse')
print(parsing_rezka)



