import requests
from bs4 import BeautifulSoup
from time import sleep




headers = {"User-Agent": "CrookedHands/2.0 (EVM x8), CurlyFingers20/1;p"}


def get_url():
    for count in range(1, 7):
        
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'


        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all('div', class_="w-full rounded border")

        for i in data:    
            card_url = "https://scrapingclub.com" + i.find("a").get('href')
            yield card_url


def array():               
    for card_url in get_url():
        
        
        response = requests.get(card_url, headers=headers)
        sleep(3)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find('div', class_="my-8 w-full rounded border")
        
        name = data.find('h3', class_="card-title").text
        price = data.find("h4", class_="my-4 card-price").text
        text = data.find("p", class_="card-description").text
        url_img = "https://scrapingclub.com" + data.find("img", "card-img-top").get("src")
        
        yield name, price, text, url_img