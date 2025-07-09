from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

insta_url = "https://www.instagram.com"

def __openInsta():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("window-size=1920,1080")
    service = Service()

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(insta_url)
    return driver

def login(username, password):
    driver = __openInsta()
    driver.find_element(By.XPATH, '//*[@name="username"]').send_keys(username) # enters username
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password) # enters password
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[contains(@class, 'html-div')]//button[@type='submit']").click()
    time.sleep(5)
    
    return driver

def sendReel(reel_path):
    pass