from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

PROXY = "23.23.23.23:3129" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)



driver = webdriver.Chrome(executable_path="C:\\Users\\omarh\\Downloads\\Compressed\\chromedriver_win32_2\\chromedriver.exe")  # Optional argument, if not specified will search path.

driver.get('https://instagram.com/')
time.sleep(5)
inputElement = driver.find_element_by_name("username")
inputElement.send_keys('3omar.hs_iqtbasat')

inputElement = driver.find_element_by_name("password")
inputElement.send_keys('ibrahee')

inputElement.submit()
time.sleep(7)
try:
    inputElement = driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF").click()
    time.sleep(4)
    inputElement = driver.find_element_by_class_name("aOOlW.HoLwm").click()
    print("Account is opened!!")
except NoSuchElementException:
    pass
    #driver.quit()