import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

@allure.title ("Print the title of ebay after searching")
@allure.description("Verify the Free Trrial button is clicked, Navigated to next page")
def test_4():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    search_box_input = driver.find_element(By.XPATH,"//input[@placeholder='Search for anything']")
    search_box_input.send_keys("macmini")

    search_box_button = driver.find_element(By.CSS_SELECTOR,"input[value='Search']")
    search_box_button.click()

    list_of_items =driver.find_elements(By.CSS_SELECTOR,".s-item__title")
    for i in list_of_items:
        print(i.text)
    list_of_item_price = driver.find_elements(By.CSS_SELECTOR,".s-item__price")
    for j in list_of_item_price:
        print(j.text)
        print(max(j.text))

    assert (len(list_of_items)) == 62


    time.sleep(5)
    driver.quit()

