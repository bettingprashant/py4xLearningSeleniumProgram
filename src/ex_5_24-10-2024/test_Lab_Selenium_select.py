import allure
from selenium import webdriver
import time
import pytest


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Select")
@allure.description("Verify Select")
def test_alerts_select():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    driver.maximize_window()

    select_html_tag = driver.find_element(By.ID, "dropdown")
    select = Select(select_html_tag)

    # select.select_by_visible_text("Option 2")
    select.select_by_index(1)


    time.sleep(5)