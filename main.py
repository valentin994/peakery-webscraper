from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    driver = webdriver.Firefox(executable_path="/Users/vareskic/Downloads/geckodriver")
    driver.implicitly_wait(30)
    driver.get("https://peakery.com/peaks/")
    WebDriverWait(driver, 60).until(
        EC.visibility_of_all_elements_located((By.ID, "peaks-table-body"))
    )
    text = driver.find_element(By.ID, "peaks-table-body")
    soup = BeautifulSoup(text.get_attribute("innerHTML"), "html.parser")
    table_rows = soup.findAll("td")
    peak = soup.findAll("span", attrs={"class": "peak-elevation-meters"})
    [print(x.text) for x in peak]
