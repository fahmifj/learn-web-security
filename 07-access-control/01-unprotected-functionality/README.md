# Unprotected functionality 

Example of unprotected functionality:

## Lab #1: Unprotected admin functionality
> This lab has an unprotected admin panel. 

Leaked admin panel directory in `robots.txt` file  

![e7e04793d764e13eebf6ce9d6faf12be.png](_resources/5b26839f61ff4f40ae6c5333defc8575.png)

Admin panel could be accessed without authentication, this leads to a vertical privilege escalation where an unauthorized user gain admin functionality.  

![869c4a5e65757be3ee2492527bce7e68.png](_resources/f3fdc51a48894a328774a69c2d112719.png)

## Lab #2: Unprotected admin functionality with unpredictable URL

> This lab has an unprotected admin panel. It's located at an unpredictable location, but the location is disclosed somewhere in the application. 

![1fb1998796161a349086e55a2acacee7.png](_resources/181af65b8c1a479fb73ec9dab69e0d2d.png)

Code:
 
```javascript
var isAdmin = false;
if (isAdmin) {
   var topLinksTag = document.getElementsByClassName("top-links")[0];
   var adminPanelTag = document.createElement('a');
   adminPanelTag.setAttribute('href', '/admin-rm57qa');
   adminPanelTag.innerText = 'Admin panel';
   topLinksTag.append(adminPanelTag);
   var pTag = document.createElement('p');
   pTag.innerText = '|';
   topLinksTag.appendChild(pTag);
}
```

Gained admin functionality

![f52cf0c5cf523ed27d7aca6eaabb170f.png](_resources/18ef5b2886604bf8b2b6d94b0639b882.png)
