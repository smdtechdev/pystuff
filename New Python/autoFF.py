from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Firefox()
time.sleep(5)
browser.get('http://www.smd.tech')
elem = browser.find_element_by_css_selector('.fa-question-circle-o')
time.sleep(5)
elem.click()
elem = browser.find_element_by_class_name('comingSoon')
time.sleep(5)
elem.click()

# elem = browser.find_element_by_css_selector('#contact > div > div > p:nth-child(1) > a')
# time.sleep(5)
# elem.click()
# try:
#     element = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "#contact > div > div > p:nth-child(1) > a"))
#     )
#     element.click()
# finally:
#     browser.quit()
        