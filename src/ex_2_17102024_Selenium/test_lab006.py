from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_chrome_current_url_verification():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(10)
    driver.quit()

def test_edge_current_url_verification():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(10)
    driver.quit()

def test_firefox_current_url_verification():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(10)
    driver.quit()
