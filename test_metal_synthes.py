from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys

def test_metal():
    driver = Firefox(executable_path='/home/udtech3574/user/geckodriver')
    driver.get('http://metal-synthes.udtech.global/')
    driver.find_element_by_name('email').send_keys("test@test.com")
    driver.find_element_by_id('name').send_keys('test')
    driver.find_element_by_id('phone').send_keys('+306666666666')
    driver.find_element_by_name('message').send_keys('test for test')
    driver.find_element_by_id('phone').clear()
    driver.find_element_by_xpath(".//div/label[contains(text(), 'This field is required.')]")

