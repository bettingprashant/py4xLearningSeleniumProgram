import allure
from selenium import webdriver
import time
import pytest


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("SVG")
@allure.description("Verify SVG")
def test_alerts_SVG():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()

    search_box = driver.find_element(By.NAME,"q")
    search_box.send_keys("macmini")

    list_svg_elements = driver.find_elements(By.XPATH,"//*[name( )='svg']")

    list_svg_elements[0].click()



    time.sleep(5)