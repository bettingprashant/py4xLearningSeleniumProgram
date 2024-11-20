import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

@allure.title("Positive Testcase - App.vwo.com Signup Button Verification.")
@allure.description("Verify that Free Trial button is clicked, Navigated to next page")
def test_negative_vwo_free_trial_project3():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    # buttons = driver.find_elements(By.TAG_NAME,"button")
    # print(len(buttons))
    # for i in buttons:
    #     print(i.text)

    all_links_page = driver.find_elements(By.TAG_NAME, "a")
    print(len(all_links_page))
    for  i in all_links_page:
        print(i.text)

    time.sleep(5)
    driver.quit()