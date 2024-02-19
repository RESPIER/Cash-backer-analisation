import requests
import lxml
from bs4 import BeautifulSoup

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
session = requests.Session()
for number_of_page in range(1, 7):
    url = f"https://cash-backer.club/shops?page={number_of_page}"
    response = session.get(url, headers=header)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        allProduct = soup.find("div", class_="container-fluid row")
        products = allProduct.find_all("div", class_="col-lg-2 col-md-3 shop-list-card pseudo-link no-link")
        for i in range(len(products)):
            try:
                title = products[i].find("div", class_='shop-title').text
                discount = products[i].find("div", class_="shop-rate").text
                chash_back = products[i].find("div", class_="shop-cashback").text
                with open("kesh_back.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{number_of_page} -> {title}, {discount}, {chash_back}\n")
            except:
                print("GG")
