from selenium import webdriver

def test_open_vwo_login():
    driver = webdriver.Chrome()
    #  POST  request to create a New FRESH copy of Chrome

    driver.get("https://app.Vwo.com")

    print(driver.title)
    assert driver. title == "Login - VWO"