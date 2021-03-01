04. Horizontal privilege escalation

# Horizontal privilege escalation

A horizontal privilege escalation occurs when a user is able to gain/access another user resources.

## Lab #6: User ID controlled by request parameter 
> This lab has a horizontal privilege escalation vulnerability on the My Account page.
> 
> To solve the lab, obtain the API key for the user carlos and submit it as the solution.
>
> You can log in to your own account using the following credentials: `wiener:peter` 

Observe 'My account' URL

![6ce7083d1e8b72df41a767ca44753f5c.png](_resources/725e830ce743409f8d81318a0c010279.png)

Change the request parameter to `id=carlos`
![eb44fce98061fd65f92c8ef819fd6fa9.png](_resources/8730c93033ec4a9dbb874e26e21f365d.png)

## Lab #7: User ID controlled by request parameter, with unpredictable user IDs 

>This lab has a horizontal privilege escalation vulnerability on the My Account page, but identifies users with GUIDs.
>
>To solve the lab, find the GUID for carlos, then submit his API key as the solution.
>
>You can log in to your own account using the following credentials: wiener:peter 

The post author's name is displayed in each post along with its GUID in the URL.

![482bdc025bc8f8d2a475ba1b949b09f8.png](_resources/c013f8953fe14f79ae5abf64de11d2e3.png)

Carlos GUID found!

![65ba3215f3ace79dcf5dba551c116fa5.png](_resources/cf539dec4ae845bb9efc90f71aad7f37.png)


## Lab #8: User ID controlled by request parameter with data leakage in redirect 

> This lab contains an access control vulnerability where sensitive information is leaked in the body of a redirect response.
>
> To solve the lab, obtain the API key for the user carlos and submit it as the solution.
>
> You can log in to your own account using the following credentials: `wiener:peter `
  

The application is rendering its content before doing page redirection.

![6db3850044e55d33e3983a8e498c4712.png](_resources/ed75ac43df9e4fe7936a0552713e9d46.png)

In this case, I could easily make a match/replace rule in Burp to automatically rewrite the HTTP status to `200` instead of `302`.

![f2814355fcedb1cd532f3c4831463fc2.png](_resources/b972fa4abf854cf19ca58dc188ad5db2.png)

Now it won't follow 302 redirection.

![95717f3c630fbe75f5d68b12943b3484.png](_resources/862f57c4989c4b0e93586144254cc06a.png)
