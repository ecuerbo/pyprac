from bs4 import BeautifulSoup
import requests

url = "https://www.pararius.com/apartments/amsterdam?ac=1"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="listing-search-item")

for list in lists:
    title = lists.find('a', class_="listing-search-item_link--title").text.replace('\n','')
    location = lists.find('div', class_="listing-search-item_link__location").text.replace('\n','')
    price = lists.find('span', class_="listing-search-item_link__price").text.replace('\n','')
    area = lists.find('span', class_="illustrated-features__description").text.replace('\n','')
    info = [title,location,price,area]
    print(info)