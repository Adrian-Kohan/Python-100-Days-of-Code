from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from bs4 import BeautifulSoup
import requests
import time

GOOGLE_URL = "https://docs.google.com/forms/d/e/1FAIpQLSepfHVQvoKwAnklD2FgpwwBqnOTz4UHVi4QgX0Kw00OSdPynw/viewform?usp=sf_link"
ZILLOW = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A37.85706439724543%2C%22south%22%3A37.693428965157956%2C%22east%22%3A-122.3066434038086%2C%22west%22%3A-122.5600155961914%7D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22mapZoom%22%3A12%7D"

header = {
    "Accept-Language": "en-US,en;q=0.9,fa;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"
}
s = Service(r"C:/Users/Adrian/Downloads/Compressed/chromedriver-win64/chromedriver-win64/chromedriver.exe")


response = requests.get(ZILLOW, headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")

links =[]
list_of_links = soup.find_all(name="a", class_="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0", href=True)
for link in list_of_links:
    href = link['href']
    if "https" not in href:
        links.append(f"https://www.zillow.com{href}")
    else:
        links.append(href)

prices = []
list_of_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr")
for price in list_of_prices:
    prices.append(price.getText().split("/")[0].split("+")[0])


addresses = []
list_of_addresses = soup.select("address")
for address in list_of_addresses:
    addresses.append(address.getText().split("|")[-1])

driver = webdriver.Chrome(service=s)

for i in range(len(links)):
    driver.get(GOOGLE_URL)

    time.sleep(2)
    address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_field.send_keys(addresses[i])

    price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.send_keys(prices[i])

    link_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field.send_keys(links[i])

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()




