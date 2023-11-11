import requests
from bs4 import BeautifulSoup
import lxml
user = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
header = {"User-Agent": user}
session = requests.Session()

for j in range(1, 68):
    print(f"Page = {j}")
    url = f"https://rozetka.com.ua/mobile-phones/c80003/page={j}"
    response = session.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        all_products = soup.find_all('li', class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")

        for product in all_products:
            if product.find("div", class_="goods-tile__price--old price--gray ng-star-inserted"):
                price = product.find('span', class_="goods-tile__price-value")
                title = product.find("span", class_="goods-tile__title")
                # print(price.text, title.text)
                price = price.text.replace(" ", " ")
                with open("phone.txt", "a", encoding="utf-8") as file:
                    file.write(f"{price} {title.text}\n")