from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

URL = "https://www.instagram.com/"
USERNAME = "Adrian_Kohan_"
PASSWORD = "mbmnaak1997"
s = Service(r"C:/Users/Adrian/Downloads/Compressed/chromedriver-win64/chromedriver-win64/chromedriver.exe")




class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=s)

    def login(self):
        self.driver.get(URL)
        time.sleep(5)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(15)



    def find_follower(self):
        self.driver.get("https://www.instagram.com/nobody_minds/")
        time.sleep(15)
        time.sleep(2)
        followers = self.driver.find_element(By.XPATH,'//*[@id="mount_0_0_Xx"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(5)
        element_inside_popup = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div')
        for i in range(5):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element_inside_popup)
            time.sleep(2)


    def follow(self):
            all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
            for button in all_buttons:
                try:
                    button.click()
                    time.sleep(1)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                    cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_follower()
bot.follow()

