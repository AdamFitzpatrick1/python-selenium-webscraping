import selenium
from selenium import webdriver
import pandas 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


DRIVER_PATH = Service("chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=DRIVER_PATH, options=options)

driver.get("https://www.nasdaq.com")
cookie_accept = driver.find_element(By.ID, "onetrust-accept-btn-handler")
cookie_accept.click()
