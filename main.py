from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

if __name__ == "__main__":
    driver = webdriver.Firefox(executable_path="/Users/vareskic/Downloads/geckodriver")
    driver.implicitly_wait(30)
    driver.get("https://peakery.com/peaks/")
    data = {}
    peak_height_list = []
    peak_name_list = []
    for i in range(15748):
        WebDriverWait(driver, 1000000).until(
            EC.visibility_of_all_elements_located((By.ID, "peaks-table-body"))
        )
        text = driver.find_element(By.ID, "peaks-table-body")
        soup = BeautifulSoup(text.get_attribute("innerHTML"), "html.parser")
        table_rows = soup.findAll("tr")
        peak_name = [
            el.findAll("td", attrs={"class": "table-hover-cell peak_avatar peak-row"})[
                1
            ].text
            for el in table_rows
        ]
        peak_name_list.extend(peak_name)
        peak_height = [
            el.find("td", attrs={"class": "table-hover-cell peak-row"})
            .find("div")
            .find("span", attrs={"class": "peak-elevation-meters"})
            .text.split()[0]
            for el in table_rows
        ]
        peak_height_list.extend(peak_height)
        print(peak_name_list)
        if i == 0:
            WebDriverWait(driver, 1000000).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        f"/html/body/main/div[2]/div/div/div/div[2]/div/div[2]/div[3]/div/div/span/div[2]/a",
                    )
                )
            ).click()
        else:
            WebDriverWait(driver, 1000000).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        f"/html/body/main/div[2]/div/div/div/div[2]/div/div[2]/div[3]/div/div/span/div[3]/a",
                    )
                )
            ).click()
    data["peak_names"] = peak_name_list
    data["peak_height"] = peak_height_list
    df = pd.DataFrame(data)
    df.to_csv("peak_data.csv")
