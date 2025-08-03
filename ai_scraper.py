from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv

options = webdriver.ChromeOptions()
# options.add_argument("--headless")  
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=options)

productlinks = []

for x in range(1, 6): # 17 originially
    driver.get(f"https://www.lazada.com.ph/vans/?from=wangpu&page={x}&q=All-Products")
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_95X4G"))
    )
    soup = BeautifulSoup(driver.page_source, "lxml")
    productlist = soup.find_all("div", class_="_95X4G")

    for product in productlist:
        for link in product.find_all("a", href=True):
            productlinks.append("https:" + link['href'])
print(f"Total product links found: {len(productlinks)}")
print(productlinks[0:5])  # Print first 5 links for verification


product_names = []
product_prices = []
product_returnwarranty = []

for link in productlinks[0:5]:
    driver.get(link)
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "block-AALAovv7f9Z"))
    )
    soup = BeautifulSoup(driver.page_source, "lxml")

    # FINDS
    name = soup.find("h1", class_="pdp-mod-product-badge-title-v2").text.strip()
    price = soup.find("span", class_="pdp-v2-product-price-content-salePrice-amount").text.strip()
    returnWarranty = soup.find("span", class_="warranty-v2-label-text").text.strip()

    # Append to lists
    product_names.append(name)
    product_prices.append("₱" + price)
    product_returnwarranty.append(returnWarranty)


driver.quit()
print(product_names)
print(product_prices)
print(product_returnwarranty)  

# Save to CSV
with open("lazada_products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(["Name", "Price", "Return/Warranty"])

    for name, price, warranty in zip(product_names, product_prices, product_returnwarranty):
        writer.writerow([name, price, warranty])