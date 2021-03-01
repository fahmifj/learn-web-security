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
- [ ] User ID controlled by request parameter with password disclosure

### Insecure direct object references (IDOR)
- [ ] Insecure direct object references

### Access control vulnerabilities in multi-step processes
- [ ] Multi-step process with no access control on one step 

### Referer-based access control
- [ ] Referer-based access control