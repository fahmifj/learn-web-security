05. Horizontal to vertical privilege escalation  

# Horizontal to vertical privilege escalation

## Lab #9: User ID controlled by request parameter with password disclosure

> This lab has user account page that contains the current user's existing password, prefilled in a masked input.
> 
> To solve the lab, retrieve the administrator's password, then use it to delete `carlos`.
> 
> You can log in to your own account using the following credentials: `wiener:peter `

'My Account' page allows password update.

![b289e145ff764abeffea24675c583516.png](_resources/b2aefe0ec57449478cab90f3842d1f4f.png)

Intercepting the update password request could capture `wiener`'s unmasked password 

![d261404f780ef1d035609a33b3caa348.png](_resources/574aa2150048421985c31e3b372628e9.png)

Same goes to the administrator account.

![58d8056cf050242390f25d39eac2301f.png](_resources/f401b22308e84c1385d5e872fdabaa34.png)
