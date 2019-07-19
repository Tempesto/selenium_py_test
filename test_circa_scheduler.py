from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

def test_google_search():
    driver = Firefox(executable_path='/home/udtech3574/user/geckodriver')
    driver.get('http://circa.udtech.global/en/')

    driver.find_element_by_xpath('.//div/div/a[@class="big Button-sc-1g20tyc-0 dxdNr"]').click()
    driver.find_element_by_xpath('.//div/div/a[@class="ClosestLocationBlock__SchedulerButton-c1i0bd-6 gwLpBX '
                                 'small Button-sc-1g20tyc-0 dxdNr"]').click()
    # def check_result_count(driver):

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    a = driver.find_elements_by_xpath("//label[contains(text(), '0')]")
    if len(a)== 0:
        print('A=0')
    a[1].click()
        # return len(time)

    # WebDriverWait(driver, 2, 0.5).until(check_result_count, "Количество результатов не равно 2")
    # time = driver.find_elements_by_xpath('.//div[@class="choose-date choose-date-times"]/div/div/div/label[1]')

