# Common SSRF attacks

## Lab #1: Basic SSRF against the local server

> This lab has a stock check feature which fetches data from an internal system.
> 
> To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos. 

Observing a product request.

![0333df3aed12212e69717f7d8ad593ad.png](../_resources/e6f84adb9fe542f182e064ff07b63812.png)

Found an url endpoint to fetch the product stock.

![2318dac0a6acce719e038324ec229b99.png](../_resources/8baad8277a924c3fb2a7f48e36f7f188.png)

SSRF to `http://localhost`.

![e99fd29ba3b72f598b25c1e21a0ae840.png](../_resources/f7cf7e305af64c19a2a2580924bb7443.png)

SSRF to `http://localhost/admin`
![ce8de9dc83584ee7b7b55fc82502c6b8.png](../_resources/b43109132b8149339ed4df45d8e14263.png)

I could make a ssrf to delete user carlos by inserting `http://localhost/admin/delete?username=carlos` as stockApi parameter value.


![95e051bd81c3c2c1891acf3ecbb51f27.png](../_resources/dba1f4d19b614e77a89f0e831fd10f91.png)

Applications that behave like this have several reason:
1. Access control restriction is ignored since the server connects to itself.
2. Disaster recovery purpose, make it easier to recover even if the administrator lose their credential.

## Lab #2: Basic SSRF against another back-end system

> This lab has a stock check feature which fetches data from an internal system.
> 
> To solve the lab, use the stock check functionality to scan the internal 192.168.0.X range for an admin interface on port 8080, then use it to delete the user carlos. 


![df6f3928a471148949ff2d8254175b68.png](../_resources/4056515e2ac446b99d899d8aa8f75e8a.png)

URL encoded
```
http%3A%2F%2F192.168.0.1%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D1%26storeId%3D1
```

Decoded URL

```
http://192.168.0.1:8080/product/stock/check?productId=1&storeId=1
```

Sending `http://192.168.0.1:8080/admin` returns missing parameter.

![d39c53069f78d64b8efd48cbb359ce48.png](../_resources/910ee75fb9df4979838adc651c060ca7.png)


Searching the correct internal IP.

![be29e9fe85caf20b9b56e08efb57c5b0.png](../_resources/b3896fe64ccc419ea604c9e36c72b249.png)

Payload range from 1-255

![51392080a71ef72d3675a957e216eb64.png](../_resources/7c2526e5c43843c7beaeaf3a60754fdf.png)


Observe the requests

![11e4ea3217d82e21e6c8b164c92b9836.png](../_resources/909cda3902f94c72b29185e427094fff.png)

The correct location was `192.168.0.4/admin`

![22ec78149f2dfaf01157aab473b86164.png](../_resources/a7cc1340e6644ac89aea67bd25d6a8fa.png)

Deleted user `carlos`
![0158c4146a6b283d67fd0f05b1915050.png](../_resources/75bf0cd3bb8d4a999cfead66a0797818.png)