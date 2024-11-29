import allure
from selenium import webdriver
import time
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Smartcare")
@allure.description("Verify Smartcare Login")
def test_smartcare():
    driver = webdriver.Chrome()
    driver.get("https://www.smartcare.health/login")
    driver.maximize_window()

    login = driver.find_element(By.XPATH, "//*[@placeholder='Mobile/Email/User Id']")
    login.click()
    login.send_keys("surendra@konsultsoft.com")
    enter_button = driver.find_element(By.XPATH,"//*[@class='svg-inline--fa fa-arrow-right icon-bg wcolor br-50 p-2 cursor-pointer']")
    enter_button.click()

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@placeholder='Password']"))
    )
    password_input.click()
    password_input.send_keys("Test@123")
    login_button = driver.find_element(By.XPATH, "//*[@class='bg-blue br-20px px-4 py-2 cursor-pointer wcolor']")
    login_button.click()
    doctor_role = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@class ='role-manage-list-card doctor-color']"))
    )
    doctor_role.click()

    # WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "XPATH_OF_OVERLAY")))  #- Don't know the code

    time.sleep(20)
    # Ensure overlay disappears


    # Click consultation element
    doctor_consultation = WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='col-lg-51 p-0 desk-show']//li[3]//a[1]//div[1]//span[1]//img[1]"))
    )
    doctor_consultation.click()
    time.sleep(20)



    # assert driver.current_url == "https://doctor.smartcare.health/doctors/my-patient"
    time.sleep(10)
