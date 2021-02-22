Table of contents
---
[toc]
# Making flawed assumptions about user behavior

## Lab #6: Inconsistent security controls

Complete registration proccess

![28786b34c31cd64e74d6c54e265cc1f4.png](_resources/01c4460f7b6b4a8cae5129ddd5fced2f.png)


![1198a90abb083d6d452649d9895affa8.png](_resources/bc982dcb46ba41aeaef499797420e0da.png)

Discover hidden content/directory with gobuster

```
$ gobuster.exe dir -u http://url -w wordlist
```

![0e75f88ef8aa326db123f27e472ea47a.png](_resources/60a62e9099bb47139cfffc3ff4fa44c3.png)

It states the admin interface is not accessible except for DontWannaCry user

![82ab241e158888beef3b29e9f15f96aa.png](_resources/1b36d846701c4ba6aea2c06dc0c9aec6.png)

An inconsistent security comes from here, where the registration does need an email verification but not for changing/updating email

![93315dfc00a80f2f4b61c77c623115e3.png](_resources/a5fd16e457784907a3dba6ba21691b72.png)


![f37add8cad643fc2fd5e1ae470dbf5a4.png](_resources/c1bd2c60c6884675b22b0cf757f36b3f.png)

## Lab #8: Password reset broken logic

> - Your credentials: wiener:peter
> - Victim's username: carlos

Use forgot password feature

![64f67697de2c25ca842ef2f2bda94cfd.png](_resources/29d70a12a8024f478ce61abe86edaff9.png)

Check the email client, open and intercept the link for password reset

![fb4ea4be9ce9eb4570ebc99b81350ed8.png](_resources/93d1b0d494ec40dd9431d5584aa6ace0.png)

Modify username in body request from `wiener` to `carlos`

![f2a8aa80669c2258b10cb6de7a5ad1cd.png](_resources/a92d17147cc14d39b5c90157f6931f48.png)

Simply login as carlos and input `peter` for the password

![8e73dfa0ecfe29b3a98145376aa7723d.png](_resources/7ed72a5fd81c4b8ab3fe8fdf928c8d24.png)

Authenticated!

![0287600cb8790e25d28c1ce4640755d1.png](_resources/02ae678e54af4ad280c5fa77f3586a17.png)

![d9edec53e9a1f19d05a1b0a1219ba629.png](_resources/58082d59c4fe4aad917319f80d7a18f1.png)

	
## Lab #9: 2FA simple bypass

Expected authentication flow:  
`Login => Send mail verification => Input verification code => Home page`

Unintended authentication flow:  
`Login => Home page`




Intercept the request and the response as well

![91b9514d096e4e46617125f031fe9d09.png](_resources/d9efd0a718204a5a80852cdc3bdce951.png)

By observing the HTTP status request, it might be possible that we're already authenticated before the app ask for verification code

![acec028779439a8a1c4d3d9c405e56e6.png](_resources/601613c7ccfd4ee6904ba3f8b2262a5f.png)

If that's , we could just modify the response location to homepage/account page

![b18f07500116fb2abdd7ec313adddc13.png](_resources/814920e7f5614b1784d3a15269848198.png)


Log in as carlos succeeded

![18ea186cb7ffc4e6deddce67df42040c.png](_resources/abd3785a7de346feba6979be9453f74c.png)

