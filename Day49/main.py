from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

urls = [

    'https://www.linkedin.com/jobs/search/?currentJobId=3692522261&f_AL=true&f_E=1%2C2&f_WT=2&geoId=103644278&keywords=python%20developer&location=United%20States&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'

]

s = Service(r"C:/Users/Adrian/Downloads/Compressed/chromedriver-win64/chromedriver-win64/chromedriver.exe")

for url in urls:
    driver = webdriver.Chrome(service=s)
    driver.get(url)
    time.sleep(5)
    sign_in = driver.find_element(By.CLASS_NAME, "job-alert-redirect-section__cta")
    sign_in.click()
    username = driver.find_element(By.ID, "username")
    username.send_keys("f.kohansal.fk@gmail.com")
    password = driver.find_element(By.ID, "password")
    password.send_keys("Mbmnaak1997")
    enter = driver.find_element(By.LINK_TEXT, "Sign in")
    enter.click()
    time.sleep(5)
    save = driver.find_element(By.LINK_TEXT, "Save")
