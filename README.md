# Web Security Academy by PortSwigger
## Learning Path

### Server-side
- [x] SQL injection 
    - [x] Login bypass
    - [x] UNION attacks
    - [x] Database examination
    - [x] Blind SQL injection 
- [ ] Authentication
    - [x] Vulnerabilities in password-based login
    - [x] Vulnerabilities in multi-factor authentication
    - [ ] Vulnerabilities in other authentication mechanism
- [x] OS command injection
    - [x] Executing arbitrary commands
    - [x] Blind OS command injection 
- [x] Directory traversal
    - [x] Arbitrary file read
    - [x] Exploiting file path traversal vulnerabilities
- [x] Business logic vulnerability
- [x] Information disclosure vulnerabilities
    - [x] Exploit information disclosure vulnerabilities
- [ ] Access control vulnerabilities
- [ ] Server-side request forgery (SSRF)
- [ ] XML external entity (XXE)

### Client-side
- [ ] Cross-site scripting (XSS)
- [ ] Cross-origin resource sharing (CORS)
- [ ] Cross-site request forgery (CSRF)
- [ ] DOM-based vulnerabilities
- [ ] Clickjacking (UI addressing)
- [ ] WebSockets

### Advanced
- [ ] Insecure deserialization
- [ ] Server-side template injection
- [ ] Web cache poisoning
- [ ] HTTP host header attacks
- [ ] HTTP request smuggling
- [ ] OAuth authentication

## SQL injection test labs

Create lab
```
$ make labs
```

Stop lab
```
$ make clean
```

## Side Skills Learned

- BurpSuite
- Python Scripting
