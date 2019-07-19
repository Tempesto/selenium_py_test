from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


def test_link():
    driver = webdriver.Firefox(executable_path='/home/udtech3574/user/geckodriver')
    driver.get('https://sb.udtech.global/#/admin/users/all')

    if driver.current_url == 'https://sb.udtech.global/#/':
        login = driver.find_element_by_xpath('//input[@class="Input__FormController__2-xDV"]')
        login.send_keys("krainik.m@udtech.co")

        passw = driver.find_element_by_xpath('.//form/div[2]/div/div/input')
        passw.send_keys("123456")
        driver.find_element_by_xpath('//div[@class="Button__Wrapper__38QdY"]').click()

        def check_li(driver):
            li_in_ul = driver.find_elements_by_xpath('.//nav/ul/li')
            return len(li_in_ul) == 8

        WebDriverWait(driver, 2, 0.5).until(check_li)
        driver.find_element_by_xpath('.//nav/ul/li[1]').click()
        li_in_ul = driver.find_elements_by_xpath('.//nav/ul/li')
        # k = 1
        for i in range(1, len(li_in_ul)+1):
            driver.find_element_by_xpath('.//nav/ul/li[{}]'.format(i)).click()
            # print(driver.find_element_by_xpath('.//nav/ul/li[{}]/button[@class="Sidebar__Current__O7CLO"]'.format(i)))
            # if driver.find_element_by_xpath('.//nav/ul/li[{}]/ul/li[2]'.format(i)):
            #     driver.find_element_by_xpath('.//nav/ul/li[3]/ul/li[2]').click()


#


