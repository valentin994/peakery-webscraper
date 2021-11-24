from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

if __name__ == "__main__":
    data = {}
    driver = webdriver.Firefox(executable_path="/Users/vareskic/Downloads/geckodriver")
    driver.implicitly_wait(30)
    driver.get("https://peakery.com/peaks/")
    WebDriverWait(driver, 60).until(
        EC.visibility_of_all_elements_located((By.ID, "peaks-table-body"))
    )
    text = driver.find_element(By.ID, "peaks-table-body")
    soup = BeautifulSoup(text.get_attribute("innerHTML"), "html.parser")
    table_rows = soup.findAll("tr")
    peak_name_list = [
        el.findAll("td", attrs={"class": "table-hover-cell peak_avatar peak-row"})[
            1
        ].text
        for el in table_rows
    ]
    peak_height = (
        table_rows[0]
        .find("td", attrs={"class": "table-hover-cell peak-row"})
        .find("div")
        .find("span", attrs={"class": "peak-elevation-meters"})
        .text.split()[0]
    )
    peak_height_list = [
        el.find("td", attrs={"class": "table-hover-cell peak-row"})
        .find("div")
        .find("span", attrs={"class": "peak-elevation-meters"})
        .text.split()[0]
        for el in table_rows
    ]
