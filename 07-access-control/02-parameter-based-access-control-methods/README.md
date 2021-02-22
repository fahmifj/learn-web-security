# Parameter-based access control methods

Some applications determine the user's access rights or role at login, and then store this information in a user-controllable location, such as a hidden field, cookie, or preset query string parameter

In some applications, user's access are stored in a user-controllable location:
- URL Parameter
- Cookie
- Hiddenfield

## Lab #3: User role controlled by request parameter

>  This lab has an admin panel at `/admin`, which identifies administrators using a forgeable cookie.
>
>Solve the lab by accessing the admin panel and using it to delete the user carlos.
>
>You have an account on the application that you can use to help design your attack. The credentials are: `wiener:peter`. 

`/admin` says:

![68fd4516afb97799b536adcce3a17ab6.png](_resources/0bb4714e68d446da8352fabd9909b68a.png)

However, there's a potential privilege escalation via cookie.

![6d10a0fc33335221efcb1b9a8160e1d1.png](_resources/2e3f19c85ad3436c8083e268e74012f1.png)


When the `admin` value is set to `True`, it gained admin functionality.

![f507d64c8cc102bdd30804aa49dcce85.png](_resources/a5660e4341d4411781adddde7483674a.png)

## Lab #4: User role can be modified in user profile
> This lab has an admin panel at /admin. It's only accessible to logged-in users with a roleid of 2.
>   
> Solve the lab by accessing the admin panel and using it to delete the user carlos.  
>  
> You can log in to your own account using wiener:peter. 

Simply visit the admin panel on `/admin`

![2903a820ad5468cbd9e6912b1c6f72a4.png](_resources/d69ee49eebae4868a3a6d0577426369a.png)

Parameter id is available when visiting my-account, but the labs need a `roleid` in integer, not an `id` in string type.

![b9b60f64ab24dc473b19c395f6fc352c.png](_resources/7c585b70b3c44bf59b9ebd75f5cf5f20.png)

When a request to update an email is sent, the returned response contains user roleid.

![1f562c64ef0ec221eadfaf74e3d332fc.png](_resources/0b69be5613f34e8cb6bb9477cb1866b3.png)

Now, we could sent a new request and add a 
`{"roleid": 2}`

![225d19b53ce27211661e2dc2facc5f72.png](_resources/34c4ff5d1afe4a2785cb96491d780203.png)

The homepage displays the menu for accessing admin panel.

![56bf02cc10482530cc15aded3d60709a.png](_resources/91151bfe44f74afd9100bfd40fdb24c8.png)