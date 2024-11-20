import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

@allure.title ("FInd all the buttons by TagName")
@allure.description("Verify the Free Trrial button is clicked, Navigated to next page")
def test_4():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    first_name_input_box = driver.find_element(By.CSS_SELECTOR,"input[placeholder='First Name']")
    first_name_input_box.send_keys("Hello")
    time.sleep(5)
    driver.quit()