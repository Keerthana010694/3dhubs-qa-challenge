import os
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture(scope='module')
def test_driver():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    """get the url"""
    driver.get("https://www.3dhubs.com/manufacture/")
    driver.maximize_window()
    yield
    """close the browser"""
    driver.quit()


def test_UrlCheck(test_driver):
    current_url = driver.current_url
    assert current_url == 'https://www.hubs.com/manufacture/'
    """upload the file from the path"""
    driver.find_element_by_id("file-btn").send_keys(os.getcwd() + "\\SampleStepFile.step")
    driver.find_element_by_id("email").send_keys("keerthu16mit@gmail.com")
    driver.find_element_by_xpath("//button[@type='submit']").click()
    driver.implicitly_wait(60)


def test_TotalPrice(test_driver):
    """check the total price"""
    Total = driver.find_element_by_css_selector("div h3d-quote-total-price span")
    assert driver.find_element_by_css_selector("div h3d-quote-total-price span").is_displayed()
    print("Total price is " + Total.text)


