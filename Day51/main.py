from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

URL = "https://www.speedtest.net/"
EMAIL = "f...com"
PASSWORD = "H!.-w"
PHONE = "+98938...909"
DOWNLOAD_SPEED = 10
s = Service(r"C:/Users/Adrian/Downloads/Compressed/chromedriver-win64/chromedriver-win64/chromedriver.exe")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=s)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(URL)
        time.sleep(2)
        run = self.driver.find_element(By.CLASS_NAME, "start-text")
        run.click()
        time.sleep(70)
        # accept_button = self.driver.find_element(By.CLASS_NAME, "close-btn pure-button pure-button-primary")
        # accept_button.click()
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

        print(self.up, self.down)
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(2)
        run = self.driver.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        run.send_keys(EMAIL)
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
        time.sleep(5)
        phone = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        phone.send_keys(PHONE)
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span').click()
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(PASSWORD)
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/svg')
        textbox = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        textbox.send_keys(f"My download and upload speeds/promise speeds are: {self.down}/{DOWNLOAD_SPEED}, {self.up}")
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
