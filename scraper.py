import requests
from bs4 import BeautifulSoup

baseurl = "https://www.lazada.com.ph/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/92.0.4515.131 Safari/537.36"
}

r = requests.get("https://www.lazada.com.ph/vans/?from=wangpu&page=1&q=All-Products")

soup = BeautifulSoup(r.content, "lxml")

productlist = soup.find_all("div", class_="Bm3ON")

print(productlist)