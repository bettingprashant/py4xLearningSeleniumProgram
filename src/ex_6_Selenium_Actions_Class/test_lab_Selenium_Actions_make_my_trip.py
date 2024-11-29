import time

import allure
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@allure.title("Actions P2")
@allure.description("Verify Mouseback")
def test_verify_action_make_my_trip():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.makemytrip.com")
    driver.maximize_window()
    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='closeModal']")))
    driver.find_element(By.XPATH, "//span[@data-cy='closeModal']").click()

    time.sleep(2)

    # fromCity = driver.find_element(By.ID,"fromCity")
    fromCity = driver.find_element(By.XPATH, "//input[@id='fromCity']")

    actions = ActionChains(driver)
    (actions.move_to_element(fromCity).click().send_keys("DEL").perform())
    time.sleep(5)

    actions.move_to_element(fromCity).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

    time.sleep(10)

    time.sleep(5)
    driver.quit()
