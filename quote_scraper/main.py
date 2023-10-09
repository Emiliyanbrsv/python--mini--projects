import requests
import json
from bs4 import BeautifulSoup

quotes = []

url = 'https://quotes.toscrape.com/'
page = 1

while True:
    response = requests.get(url)
    s = BeautifulSoup(response.content, 'html.parser')

    all_quotes = s.find_all('div', class_='quote')

    for quote in all_quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = ';'.join(tag.text for tag in quote.find_all('a', class_='tag'))

        url = f'https://quotes.toscrape.com/page/{page}/'

        quotes.append({
            'text': text,
            'author': author,
            'tags': tags,
            'url': url
        })

    next_page = s.find('li', class_='next')

    if next_page:
        page += 1
        url = f'https://quotes.toscrape.com/page/{page}/'

    else:
        break

with open('task_2_output.json', 'w') as jsonfile:
    json.dump(quotes, jsonfile, ensure_ascii=False, indent=4)
