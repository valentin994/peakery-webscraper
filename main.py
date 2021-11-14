from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

if __name__ == "main":
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get("https://peakery.com/peaks/")
    WebDriverWait(driver, 60).until(EC.visibility_of_all_elements_located((By.ID, "peaks-table-body")))
    text = driver.find_element(By.ID,"peaks-table-body")
    print(text.get_attribute("innerHTML"))
