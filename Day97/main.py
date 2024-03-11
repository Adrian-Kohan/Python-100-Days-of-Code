import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


USER = "adrian.kohan.sal@gmail.com"
PASSWORD = "**********"
DIGI_PASS = "**********"
DIGI_USER = "09385356909"
order = ""

GMAIL = "https://mail.google.com/mail/u/1/#inbox"
DIGI = "https://seller.digikala.com/orders/"

s = Service(r"C:/Users/Adrian/Downloads/Compressed/chromedriver-win64/chromedriver-win64/chromedriver.exe")

class OrderChecker:
    def __init__(self):
        self.driver = webdriver.Chrome(service=s)

    def email_login(self):
        self.driver.get(GMAIL)
        time.sleep(2)
        username = self.driver.find_element(By.NAME, "identifier")
        username.send_keys(USER)
        self.driver.find_element(By.ID,"identifierNext").click()
        time.sleep(6)
        password = self.driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
        password.send_keys(PASSWORD)
        self.driver.find_element(By.ID, "passwordNext").click()
        time.sleep(5)

    def send_message(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div').click()
        time.sleep(5)
        to = self.driver.find_element(By.ID, ":bp")
        to.send_keys(USER)
        subject = self.driver.find_element(By.XPATH, '//*[@id=":8f"]')
        subject.send_keys("Order Status")
        message = self.driver.find_element(By.ID, ":9d")
        message.send_keys(f"You have {order} order.")
        self.driver.find_element(By.ID, ':7t').click()
        time.sleep(15)

    def digi_login(self):
        self.driver.get(DIGI)
        time.sleep(10)
        username = self.driver.find_element(By.XPATH, '//*[@id="app"]/section/div[1]/form/label/div/section/input')
        username.send_keys(DIGI_USER)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/div[1]/form/div/button/div').click()
        time.sleep(5)

    def find_order(self):
        global order
        time.sleep(5)
        order = self.driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div/div/div/p/strong[2]')
        return order


bot = OrderChecker()
bot.digi_login()
bot.find_order()
bot.email_login()
bot.send_message()
