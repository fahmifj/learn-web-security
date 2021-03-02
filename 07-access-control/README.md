# Access Control

Access controls is application of constrains on what (or who) is allowed to perform attempted actions or access resources that they have requested.

Access control is depent on `Authentication` and `Session Management`

- **Authentication** validates the identity of users.
- **Session Management** determine which http request are being made by the same users.

# Labs

Example of broken access control with hands on lab

### Vertical privilege escalation

#### Unprotected functionality  
All labs: [Unprotected functionality](01-unprotected-functionality/README.md)
- [x] Unprotected admin functionality
- [x] Unprotected admin functionality with unpredictable URL

#### Parameter-based access control methods 
All labs: [Parameter-based access control methods](02-parameter-based-access-control-methods/README.md)
- [x] User role controlled by request parameter
- [x] User role can be modified in user profile

#### Broken access control resulting from platform misconfiguration
All labs: [Broken access control resulting from platform misconfiguration](03-platform-misconfiguration/README.md)
- [x] URL-based access control can be circumvented
- [x] Method-based access control can be circumvented

### Horizontal privilege escalation
All labs: [Horizontal privilege escalation](04-horizontal-privilege-escalation/README.md)
- [x] User ID controlled by request parameter 
- [x] User ID controlled by request parameter, with unpredictable user IDs 
- [x] User ID controlled by request parameter with data leakage in redirect

### Horizontal to vertical privilege escalation
- [x] [User ID controlled by request parameter with password disclosure](05-horizontal-to-vertical-privilege-escalation/README.md)

### Insecure direct object references (IDOR)
- [x] [Insecure direct object references](06-insecure-direct-object-references/README.md)

### Access control vulnerabilities in multi-step processes
- [x] [Multi-step process with no access control on one step](08-referer-based-access-control/README.md)

### Referer-based access control
- [x] [Referer-based access control](08-referer-based-access-control/README.md)