from seleniumwire import webdriver
from bs4 import BeautifulSoup as bs 

driver = webdriver.Firefox()

driver.get("http://10.0.2.15:8080/login.php")

URL = "http://10.0.2.15:8080/vulnerabilities/weak_id/"

delay = 2

driver.implicitly_wait(delay)

driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('1234')
driver.find_element_by_xpath('/html/body/div/div[2]/form/fieldset/p/input').click()

driver.get(URL)

driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/form/input').click()
for request in driver.requests:
    if(str(request) == URL):
            try:
                print(request.response.headers['Set-Cookie'])
            except KeyError:
                print('skip')

driver.close()
