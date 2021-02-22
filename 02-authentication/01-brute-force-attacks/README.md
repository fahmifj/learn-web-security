Table of contents
---
[toc]
# Brute-force attacks

Payloads:
- [Username]( https://portswigger.net/web-security/authentication/auth-lab-usernames)
- [Password](https://portswigger.net/web-security/authentication/auth-lab-passwords)


## Brute force usernames
Easy to guess by naming convention like,

- `firstname.lastname@corporation.com`
- `firstinitialname.lastname@corporation.com`

Notes for auditing:

- Is the website discloses a potential username publicly?
- Is a profile accessible without logging in?
- Contact email = potential IT support/sysadmin with high privileges.

## Brute-forcing passwords
Predictable password can improves success rate in brute force especially dictionary attack, therefore attackers may have an up to date wordlist.

## Username enumeration
Attackers may observe changes in the website before brute-forcing.

For examples, when attackers enter one username and a random password, the application might reply that the given username is valid but the password is incorrect.
Therefore, attackers can enumerate the valid usernames which then reduce the time cost required to do brute-force.

# Labs
## Lab #1: Username enumeration via different responses

Steps:

**BurpSuite Intruder - Sniper Attack**

Brute force username

![924f807bdccd9356d18e156216e5eccd.png](./_resources/d9b21c3af6344604a489344f03228b89.png)

Brute force password

![94d047c56efc8e419781b42496c6a4e4.png](./_resources/1486b1f245304ad1979cbbd4e3e27534.png)

Valid credential is `afiliados:123456789`

![e6f8b281ec59482009359b70ec5ed3ac.png](./_resources/60c2d3392c954c02ac97bfb688239285.png)

**Sniper Attack in Python**

Pseudo w/o threading:
Username enumeration
```
valid_users = []
for user in usernames:
	data = {
			"username": {user},
			"password": "test"}
	login = requests.post(url, data)
	
	if "Incorrect password" in login.text:
		valid_user.append(user)
		print(valid_user[-1]) 
```


## Lab #2: Username enumeration via subtly different responses

Steps:

Username enumeration

![e9c2038f15ba8bcd0b82c35bca116de1.png](./_resources/e1a858fde1f041339dacf28b829479c0.png)

username `alerts` returns a response without full stop.

Brute force passwords

![25ee793a75ccd94ec7555f75e8c0db68.png](./_resources/537b3e17bd684971a5b44430ae84d8a4.png)

![390b5a7e9cbb7a565aaae7122e86bccb.png](./_resources/c0fba60c2433429e83c141778d3486f2.png)

## Lab #3: Username enumeration via response timing

> My scripting skill is not strong enough to complete this lab, so I followed the solution.

Steps:

**Determine response time**

Invalid or valid username with valid password = around 1000ms

![801769426138400abc3ace92c25dbf9b.png](./_resources/4fcad5923ea14f7a814c1f7e132b2e0b.png)

Valid username, invalid password = 4,900ms 

![9c5dcb4ac8ca07c4a7e902fae4f12139.png](./_resources/d2adcf3ba74449709010970b16866d75.png)


Brute-force with BurpSuite Intruder - Pitchfork attack

> By adding `X-Forwarded-For` header, the server will think our request was sent from proxy
>
> Example our client ip: 1.2.3.4 and `X-Forwarded-For` set to 127.0.0.1, then the server thinks the client ip, which is 1.2.3.4 was the proxy and believe the original request comming from 127.0.0.1, thus we can manipulate `X-Forwarded-For` to bypass brute-force ip blocking protection

![c66d22730c305e0141388595d1e99468.png](./_resources/8bca45f6aaac4fd9b87963c7a8b0258b.png)

Payload `X-Forwarded-For`

![65da1b205da4ec9e4d1592647adf3c08.png](./_resources/a80983e6d8384ab6928455a86fa26f0b.png)

Payload `username`

![2854a49e6b920d2dda6b85162b5645e3.png](./_resources/959a2da8507e4f98a5a949289fce0619.png)

User enumeration, select some user with high response time, and repeat the request using repeater
- arizona ~0,5s
- arkansas ~0,6s
- al ~0,5s
- ads ~0,5s
- appserver ~ 1s
- accounting ~ 0,5s

![567a5e9f17938ef95a39e349fb8a2fc3.png](./_resources/c95f2486ab4b4b3a82d30034b5620241.png)

Brute force password
![9b29bd09d84b998031d35cd0f16ce904.png](./_resources/134f05a80a874e18bbfe1953804f27e7.png)

Done.

![d3e9fc911a763528f4d47d7d54fd79a3.png](./_resources/898f9bb73592432397386868000fece0.png)