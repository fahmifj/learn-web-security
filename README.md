# Web Security Academy by PortSwigger

This repository contains my notes (mostly in raw) about web application security and get familiar with BurpSuite. It also contains a few of exploit-like scripts and a small experiment lab for SQLi. It follows the [Web Security Academy](https://portswigger.net/web-security/learning-path) learning path.

## Learning Path

Below are the topics I've completed

### Server-side
- [x] [SQL injection](01-sql-injection/README.md)
- [x] [Authentication](02-authentication/README.md)
- [x] [Directory traversal](03-directory-traversal/README.md)
- [x] [OS command injection](04-command-injection/README.md)
- [x] [Business logic vulnerability](05-business-logic-vulnerabilities/README.md)
- [x] [Information disclosure vulnerabilities](06-information-disclosure/README.md)
- [x] [Access control vulnerabilities](07-access-control/README.md)
- [x] [Server-side request forgery (SSRF)](08-server-side-request-forgery/README.md)
- [x] [XML external entity (XXE)](09-xxe-injection/README.md)

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

## Side Skills Learned

- BurpSuite
- Python Scripting

## Labs

Currently it only has one lab for sql injection.

### SQL injection test labs

Create lab
```
$ make labs
```

Stop lab
```
$ make clean
```