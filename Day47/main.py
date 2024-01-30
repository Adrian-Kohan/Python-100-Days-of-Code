import requests
from bs4 import BeautifulSoup
import lxml
import smtplib


MY_EMAIL = "f.kohansal.fk@gmail.com"
MY_PASSWORD = "fnzldfsjhegdsgk"
URL = "https://www.amazon.com/dp/B08F31PJ16/ref=sbl_dpx_kitchen-electric-cookware_B08CFZF16Y_0"
header = {
    "Accept-Language": "en-US,en;q=0.9,fa;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"
}

response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.content, "lxml")
price = soup.find(class_="a-offscreen").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
title = soup.find(id="productTitle").get_text().strip()
goal_price = 5

if price <= goal_price:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )