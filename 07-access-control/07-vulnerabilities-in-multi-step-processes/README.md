# Access control vulnerabilities in multi-step processes

## Lab #10: Multi-step process with no access control on one step 

> This lab has an admin panel with a flawed multi-step process for changing a user's role. You can familiarize yourself with the admin panel by logging in using the credentials `administrator:admin`.
>
> To solve the lab, log in using the credentials `wiener:peter` and exploit the flawed access controls to promote yourself to become an administrator. 

Observing account ugprade proccess

![a82be7eaae64cb17879825326da0651e.png](_resources/4846692aae03427aa878f234694aa468.png)

The initial request:

![6fa01138fbc871beec1ca7beda557e7b.png](_resources/3da4313c739c4ceaadb88932db82fc87.png)

The second step is a confirmation

![27bfd856d7bc5108cc0de3360a320c75.png](_resources/9e6d5373c25e46e5b671cdeb7395d14f.png)

The confirmation page view

![729efa070058c51e5561d97ee28ba415.png](_resources/be01966a82824682959f93132a2e085a.png)

The new request that being sent after upgrade action is confirmed

![c82dca3425cc9d5adb8b2d2b70f3e560.png](_resources/c64d9333975a4d148ebafd9f4ffb39e4.png)

By injecting `wiener`'s session to the request above, I successfully become an administrator.

![3a583ddd4ce61b0df0cc99649d1bdd36.png](_resources/a39edad5ae704084a3925612a6abff5d.png)

![6511b1ab328b2613ff2a2dd0e855eadf.png](_resources/5f590df23eae45dfb2f581e5c283d41c.png)
