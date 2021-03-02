# Referer-based access control 
A referer-based access control is an access control that relies on HTTP `Referer` header. The application then decide whether the specific request/action is allowed or not based on that header.


## Lab #11: Referer-based access control 
> This lab controls access to certain admin functionality based on the Referer header. You can familiarize yourself with the admin panel by logging in using the credentials `administrator:admin`.
> 
> To solve the lab, log in using the credentials `wiener:peter` and exploit the flawed access controls to promote yourself to become an administrator. 

Observing the HTTP request to promote a user to admin from administrator account.

![6c417ed4d28805a571df05be70058047.png](_resources/6c621303e38e4fa78ec795a42c0c92c8.png)
Got unauthorized response after the following header is removed.
```
Referer: https://ac9e1fa91f3dbbde8002391700e700ce.web-security-academy.net/admin
```
![a2ddd324c5c84d85cc07fb65cd92dc4a.png](_resources/52ac01bcc7e34221a070fabf473dd1cc.png)

Repeating the URL request from `wiener` session also returns unauthorized.

![2d0f29ee455de61222e9188db6915908.png](_resources/7217bb4ccd4c49118b5167dc79a70126.png)

But adding the same referer from admin request resulting a status 302 Found.
![0aaf482979dc8237a10094b537b1531e.png](_resources/93eb21b4b120401a9c7cd4730236f378.png)

Wiener now has admin panel

![b03bbecd6062ba98ed3b6295da0353ba.png](_resources/2edabb0c01bd418d901c6336dfd3d577.png)