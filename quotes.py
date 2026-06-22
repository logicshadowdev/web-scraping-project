from bs4 import BeautifulSoup
import requests
import json

source = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(source.text, 'lxml')
contain = soup.find('div', class_='container')
title = contain.h1.a
print(title.text)

data = []

quote_block = contain.find_all('div', class_='quote')
for block in quote_block:
    quote = block.find('span', class_='text').text
    author = block.find('small', class_='author').text
    print(f"Quote: {quote}")
    print(f"Author: {author}")
    
    tags = []
    for tag in block.find_all('a', class_='tag'):
        tags.append(tag.text)
        print(f"Tag: {tag.text}")
    print("-" * 40)
    
    data.append({
        "quote": quote,
        "author": author,
        "tags": tags
    })

with open("quotes.json", "w") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
    print("✅ Quotes Saved to quotes.json")