from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

def test_google():
    driver = webdriver.Firefox(executable_path = '/home/udtech3574/user/geckodriver')

    driver.get('https://www.google.com')
    search_input = driver.find_element_by_class_name("gLFyf")

    search_input.send_keys("google translate")
    search_input.send_keys(Keys.ENTER)

    def check_result_count(driver):
        inner_search_result = driver.find_elements_by_xpath('//div[@class="g"]')
        return len(inner_search_result) >= 10

    WebDriverWait(driver, 2, 0.5).until(check_result_count, "Количество результатов не равно 10")

    search_result = driver.find_elements_by_xpath('//div[@class="g"]')
    link = search_result[0].find_element_by_xpath('.//a/h3').click()
    # link.click()
    driver.find_element_by_xpath('//div[@id="sugg-item-en"]').click()
    driver.find_element_by_xpath('.//div[@class="tl-sugg"]/div[2]/div[2]').click()


    enter_text = driver.find_element_by_xpath('//textarea[@id="source"]')
    enter_text.send_keys("Hi all, i'm test script")


