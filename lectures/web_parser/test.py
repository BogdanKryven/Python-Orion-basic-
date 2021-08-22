import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.google.com.ua/")

html = response.text
soup = BeautifulSoup(html)

text = soup.find("input", class_='lsb').get("value")
pass