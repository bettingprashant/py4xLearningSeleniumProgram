from selenium import webdriver

def test_task2():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    page_source_data = driver.page_source
    assert "CURA Healthcare Service" in page_source_data
    driver.quit()