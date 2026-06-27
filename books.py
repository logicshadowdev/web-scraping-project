from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(source.text, "lxml")
title = soup.find('div', class_="col-sm-8 h1")
print(title.a.text)

data = []

books = soup.find_all("article", class_="product_pod")
for book in books:
    title = book.h3.a['title']
    price = book.find("p", class_="price_color").text
    rating = book.find("p", class_="star-rating")
    rating_value = rating["class"][1]
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Rating: {rating_value}")
    print("-" * 40)

    data.append([
        title,
        price,
        rating_value
    ])

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Rating"])
    writer.writerows(data)