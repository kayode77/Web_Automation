import unittest
import HtmlTestRunner
import re
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Demoselect(unittest.TestCase):
        # Selection of States
    def test_INECFORM(self):
        driver=webdriver.Chrome()
        driver.get('https://cvr.inecnigeria.org/pu')
        driver.implicitly_wait(10)
        driver.maximize_window()
        Parent_handle=driver.current_window_handle
        print(Parent_handle)
        print(driver.title)
        driver.save_screenshot('my.png')
        def clean_text(a):
          a=str(a)
          a=re.sub('/','-',a)
          a=re.sub(' {1,}',' ',a)
          return a.split()[2]


        INEC_STATE = driver.find_element(By.XPATH, "//*[@value='30']")
        INEC_STATE.click()
        print('The state selected is:', INEC_STATE.text)

        INEC_LOCAL_GOVERNMENT = driver.find_element(By.XPATH, "//*[@value='622']")
        INEC_LOCAL_GOVERNMENT.click()
        print('The Local Government selected is:',clean_text(INEC_LOCAL_GOVERNMENT.text))


        INEC_REGISTRATION_AREA = driver.find_element(By.XPATH, "//*[@value='7137']")
        INEC_REGISTRATION_AREA.click()
        print('The Registration area selected is:',clean_text(INEC_REGISTRATION_AREA.text))

        INEC_POLLING_UNIT = driver.find_element(By.XPATH, "//*[@value='98347']")
        INEC_POLLING_UNIT.click()
        print('The Polling unit selected is:',INEC_POLLING_UNIT.text)
        driver.save_screenshot('my1.png')


        wait = WebDriverWait(driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@class='btn block btn-success btn-block']")))
        element.click()
        All_handles=driver.window_handles
        print(All_handles)
        for handle in All_handles:
            if handle != Parent_handle:
                driver.switch_to.window(handle) 

        driver.save_screenshot('my2.png')

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False,testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Victoria\\Desktop\\inec\\REPORT'))
    