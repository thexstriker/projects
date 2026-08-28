from bs4 import BeautifulSoup
import requests
import csv

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    print(f"Title: {title}, Price: {price}")

with open("books.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Price"])
    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text
        writer.writerow([title, price])

