from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


def test_ya_search():
    driver = Firefox(executable_path='/home/udtech3574/user/geckodriver')
    driver.get('http://google.com')
    search = driver.find_element_by_name("q")
    search.send_keys('play market')
    search.send_keys(Keys.ENTER)

    def chech_results_count(driver):
        inner_search_results = driver.find_elements_by_xpath('//div[@class="g"]')
        return len(inner_search_results) > 2

    WebDriverWait(driver, 2, 0.5).until(chech_results_count)
    link = driver.find_elements_by_xpath('//div[@class="g"]')[0].find_element_by_xpath('.//div/a')
    link.click()
    search_play = driver.find_element_by_xpath('//input[@name="q"]')
    search_play.send_keys('Selenium')
    search_play.send_keys(Keys.ENTER)
