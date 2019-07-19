from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


def test_google_search():
    driver = Firefox(executable_path='/home/udtech3574/user/geckodriver')
    driver.get('https://google.com')
    search_input = driver.find_element_by_name('q')
    search_input.send_keys('Selenium')
    search_input.send_keys(Keys.ENTER)
    result = driver.find_elements_by_xpath('//div[@class="g"]')
    def check_result_count(driver):
        inner_search_result = driver.find_elements_by_xpath('//div[@class="g"]')
        return len(inner_search_result) >= 9

    WebDriverWait(driver, 2, 0.5).until(check_result_count, "Количество результатов не равно 10")
    for r in result:
        title_list = r.find_element_by_tag_name('h3').text
        assert 'Selenium' in title_list
    driver.quit()

