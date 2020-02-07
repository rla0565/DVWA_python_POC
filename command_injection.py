import requests
import os

a = input("명령어를 입력하시오.")

URL = "http://10.0.2.15:8080/vulnerabilities/exec/"
        
cookie={
        "PHPSESSID":"egeq7ijgbia3dcb111r71197r2",
        "security":"low"
        }

session1 = requests.Session()

req=session1.post(URL,cookies=cookie)


os.system(str(a))
exit()
