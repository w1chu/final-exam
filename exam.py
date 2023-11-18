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
            all_products = soup.find_all("div", class_="products-layout__item without-options-1 without-options-3 without-options-4")

            for product in all_products:
                if product.find("div", class_="product-card"):
                    title = product.find("a", class_="product-card__title")
                    review = product.find("span", class_="comments-preview__count")
                    price = product.find("span", class_="sum")
                    print(title.text, review.text, price.text)
                    # price = price.text.replace(" ", " ")
                    file.write(f"{title.text} {review.text} {price.text}\n")
                    sheet1[f"A{count}"] = title.text
                    sheet1[f"B{count}"] = review.text
                    sheet1[f"C{count}"] = price.text
                    count += 1

            book.save("Catalog1.xlsx")
            book.close()

book = openpyxl.Workbook()
sheet2 = book.active

sheet2["A1"] = "Title"
sheet2["B1"] = "Reviews"
sheet2["C1"] = "With discounts"

with open("vinyl2.txt", "a", encoding="utf-8") as file:
    for j in range(1, 26):
        print(f"Page = {j}")
        url = f"https://allo.ua/ua/vinilovye-proigryvateli/p-={j}"
        response = session.get(url, headers=header)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            all_products = soup.find_all("div", class_="products-layout__item without-options-1 without-options-3 without-options-4")

            for product in all_products:
                if product.find("div", class_="v-pb"):
                    title = product.find("a", class_="product-card__title")
                    review = product.find("span", class_="comments-preview__count")
                    price = product.find("span", class_="sum")
                    print(title.text, review.text, price.text)
                    # price = price.text.replace(" ", " ")
                    file.write(f"{title.text} {review.text} {price.text}\n")
                    sheet2[f"A{count}"] = title.text
                    sheet2[f"B{count}"] = review.text
                    sheet2[f"C{count}"] = price.text
                    count += 1

            book.save("Catalog2.xlsx")
            book.close()