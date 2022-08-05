import time

from selenium import webdriver



driver = webdriver.Chrome(executable_path="C:\\Users\\Omar Hassan\\Downloads\\chromedriver_win32\\chromedriver.exe")  # Optional argument, if not specified will search path.

driver.get('https://elearning.zuj.edu.jo/');

time.sleep(5) # Let the user actually see something!

#search_box = driver.find_element_by_name('q')
#search_box.send_keys('ChromeDriver')
    #search_box.submit()
while True:
    inputElement = driver.find_element_by_id("username")
    inputElement.send_keys('201911176@std-zuj.edu.jo')

    inputElement = driver.find_element_by_id("password")
    inputElement.send_keys('nan2001')

    inputElement.submit()
    # username
    # password

time.sleep(5) # Let the user actually see something!

#driver.quit()




'''from selenium import webdriver

driver = webdriver.Chrome('/Users/iyadmajid/Desktop/chromedriver')
driver.set_page_load_timeout(30)
driver.get('https://www.typing.com/student/login')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



inputElement = driver.find_element_by_id("a1")
inputElement.send_keys('1')

inputElement.submit()

driver.implicitly_wait(20)
driver.find_element_by_id('username').send_keys('the_username')
driver.find_element_by_name('password').send_keys('the_password')
driver.find_element_by_class_name('submit-login').click()
driver.find_element_by_xpath("//a[@href='/student/lessons/380/numeric-keypad']").click()
driver.find_element_by_xpath("//a[@class='button begin-button tooltip-trigger']").click()'''