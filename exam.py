import requests
from bs4 import BeautifulSoup
import lxml
import openpyxl

book = openpyxl.Workbook()
sheet1 = book.active

sheet1["A1"] = "Title"
sheet1["B1"] = "Reviews"
sheet1["C1"] = "Price"

user = f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
header = {"User-Agent": user}
session = requests.Session()

count = 2

with open("vinyl1.txt", "a", encoding="utf-8") as file:
    for j in range(1, 26):
        print(f"Page = {j}")
        url = f"https://allo.ua/ua/vinilovye-proigryvateli/p-={j}"
        response = session.get(url, headers=header)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            all_products = soup.find_all("div", class_="product-card")

            for product in all_products:
                title = product.find("a", class_="product-card__title")
                try:
                    review = product.find("span", class_="comments-preview__count").text
                except AttributeError:
                    review = 0
                price = product.find("div", class_="v-pb")
                print(title.text, review, price.text)
                file.write(f"{title.text} {review} {price.text}\n")
                sheet1[f"A{count}"] = title.text
                sheet1[f"B{count}"] = review
                sheet1[f"C{count}"] = price.text
                count += 1

            book.save("Catalog1.xlsx")
            book.close()

book1 = openpyxl.Workbook()
sheet2 = book1.active

sheet2["A1"] = "Title"
sheet2["B1"] = "Reviews"
sheet2["C1"] = "With discounts"

with open("vinyl2.txt", "a", encoding="utf-8") as file:
    for b in range(1, 26):
        print(f"Page = {b}")
        url = f"https://allo.ua/ua/vinilovye-proigryvateli/p-={b}"
        response = session.get(url, headers=header)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            all_products = soup.find_all("div", class_="product-card")

            for product in all_products:
                if product.find("div", class_="v-pb__old"):
                    title = product.find("a", class_="product-card__title")
                    try:
                        review = product.find("span", class_="comments-preview__count").text
                    except AttributeError:
                        review = 0
                    price = product.find("div", class_="v-pb__cur discount")
                    print(title.text, review, price.text)
                    file.write(f"{title.text} {review} {price.text}\n")
                    sheet2[f"A{count}"] = title.text
                    sheet2[f"B{count}"] = review
                    sheet2[f"C{count}"] = price.text
                    count += 1

            book1.save("Catalog2.xlsx")
            book1.close()