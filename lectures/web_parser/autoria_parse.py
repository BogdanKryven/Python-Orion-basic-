import requests
from bs4 import BeautifulSoup, Tag
import pandas as pd


URL = "https://auto.ria.com/uk/newauto/marka-skoda/"
HOST = "https://auto.ria.com/uk"
HEADERS = ["title", "link", "price", "price_local", "region"]


def get_html(url, data={}):
    response = requests.get(url, data=data)

    if response.status_code != 200:
        return False

    return response.text


def get_pages(html):
    soup = BeautifulSoup(html, "html.parser")
    pages_buttons = soup.find_all("a", class_="page-link")

    if pages_buttons:
        return int(pages_buttons[-2].text)
    else:
        return 1


def parse_brand_page(html) -> list:
    cars_list = []

    soup = BeautifulSoup(html,"html.parser")
    items_list = soup.find_all("section", class_="proposition")

    for item in items_list:
        cars_list.append(parse_proposition(item))

    return cars_list


def parse_proposition(item: Tag) -> dict:

    price_str = item.find("div", class_="proposition_price").text.strip().replace(" ", "").replace("$", "").replace("грн", "")
    price, price_local = price_str.split("•")
    item_dict = {
        "title": item.find("h3", class_="proposition_name").text.strip(),
        "link": HOST + item.find("a", class_="proposition_link").get("href"),
        "price": float(price),
        "price_local": float(price_local),
        "region": item.find("span", class_="item region").text,
    }
    return item_dict


def main():
    html = get_html(URL)
    pages = get_pages(html)
    all_cars_by_brand = []
    for i in range(1, pages + 1):
        html = get_html(URL, data={"page": i})
        all_cars_by_brand.extend(parse_brand_page(html))

    save_to_xlsx_pandas(all_cars_by_brand)


def save_to_xlsx_pandas(list_):
    df = pd.DataFrame(list_)

    writer = pd.ExcelWriter("cars.xlsx", engine='xlsxwriter')
    df.to_excel(writer, sheet_name='x1')
    writer.save()


if __name__ == '__main__':
    main()
