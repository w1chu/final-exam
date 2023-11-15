import requests
from bs4 import BeautifulSoup
import lxml

user = f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
header = {"User-Agent": user}
session = requests.Session()

for j in range(1, 26):
    print(f"Page = {j}")
    url = f"https://www.olx.ua/uk/elektronika/audiotehnika/cd-md-vinilovye-proigryvateli/?currency=UAH&page={j}"
    response = session.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        all_products = soup.find_all("div", class_="css-1sw7q4x")

        for product in all_products:
            if product.find("div", class_="css-1sw7q4x"):
                cond = product.find("span", class_="css-1sw7q4x")
                title = product.find("h6", class_="css-1sw7q4x")
                print(cond.text, title.text)
                cond = cond.text.replace(" ", " ")
                with open("vinyl.txt", "a", encoding="utf-8") as file:
                    file.write(f"{cond} {title.text}\n")