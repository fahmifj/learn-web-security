# Broken access control resulting from platform misconfiguration

Example of broken access control from platform misconfiguration is when a non-standard HTTP headers such as `X-Original-URL` and `X-Rewrite-URL` can be used to bypass restricted acccess of application URL/functions that has specific rules enforced to it.


## Lab #4: URL-based access control can be circumvented

> This website has an unauthenticated admin panel at `/admin`, but a front-end system has been configured to block external access to that path. However, the back-end application is built on a framework that supports the `X-Original-URL` header.
>
> To solve the lab, access the admin panel and delete the user carlos. 

Normal request to `/admin`

![eccd3cf40deba4a2304de824b6d9c01a.png](_resources/7d9f1f98b68941bea76fb32f4cea8187.png)

![4282b3c557562f7a95a22af32ce3c834.png](_resources/1f1347e3533645a0b6fb41047241bdf4.png)

Testing custom HTTP header 

![f4ebb2e46cfc627cc06c144cef250d2c.png](_resources/430453b2e8da444f975258d7dab0486c.png)

Override original request URL `GET / HTTP/1.1` with `X-Original-URL: /admin`

![c49ecdb88a9d40ad4f946f575241703f.png](_resources/425a6f6e057f4ec5bd073c1f1ac408b1.png)

Sent delete request for user `carlos`

![1a6e7a982918a9c50a1d4dcbb34eb9b4.png](_resources/a14bbba1855e4350bd98a8520ba87ac0.png)

user `carlos` deleted successfully

![1f7b2d317cc617af43ad65141bc99fcf.png](_resources/6fc8f5ed45b74eab9e9a92d76a68640b.png)

## Lab #5: Method-based access control can be circumvented
>This lab implements access controls based partly on the HTTP method of requests. You can familiarize yourself with the admin panel by logging in using the credentials `administrator:admin`.
>
> To solve the lab, log in using the credentials `wiener:peter` and exploit the flawed access controls to promote yourself to become an administrator. 

Observing the application request as admin

Request action: promote user to admin

![2cf5aae180ff3237197766486c7ab442.png](_resources/a63b439ffeef47ac90c5efaf2689595e.png)

Request action: demote user from admin

![92a25d938c35c4ab474343a0b1fb9ae7.png](_resources/ddbcd8d09fa84b9084fcd88d8e7e9c95.png)

Trying `PUT` as it's the proper method to update things in REST way

![2443f016aa3f17ae25d142bcf27954f4.png](_resources/b20ac38f4c9d41cb9fc409d7bd18e9a1.png)

Now user `wiener` has admin panel

![82c14632bc9e75395d8bfc7ced275c53.png](_resources/c7982b4a32a04be4a79b1e277526b6d5.png)
