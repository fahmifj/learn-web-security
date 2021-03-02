from urllib.parse import urlparse
import requests

url = "http://localhost#@stock.weliketoshop.net:8080/"

test = urlparse(url)

url_scheme = test.scheme
print(url_scheme)

url_user = test.username
print(url_user)

url_pass = test.password
print(url_pass)

url_host = test.hostname
print(url_host)

url_port = test.port
print(url_port)

url_frag = test.fragment
print(url_frag)

r = requests.Session()

proxies = {
	"http": "http://127.0.0.1:8080",
	"https": "https://127.0.0.1:8080"
}

r.get(url, proxies=proxies)
