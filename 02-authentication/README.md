# Authentication vulnerabilities

## What is authentication?

Authentication is a process of verifying a someone or something identity. It's making sure that the identity is valid or genuine.

Therefore, the authentication mechanism must be robust.

Three authentication factors:
- Knowledge -> Something you **know** (Password, PIN)
- Possession -> Something you **have** (Devices, token)
- Inherence -> Something you **are** (Biometric)

## Authentication vs Authorization

Authentication only **verify** who you are, it doesn't care about what you can do after, what permission you have, it only **validates**.

Authorization does care about what you can do or what thing you are **allowed** to do.

## Authentication vulnerabilities factors

- Weak mechanism
Bruteforce, weak session cookie, default/hardcoded credentials.

- Logic flaws
Poor coding in the implementation, allows an attacker to bypass authentication/validation.
This is reffered as Broken Authentication in OWASP TOP 10.

## Impact

- Attackers may take full control over the entire application/system.
- Sensitive data 
- Possibly opening a broader attack surface (pivoting)

# Labs
## Vulnerabilities in password-based login

### Brute-force attacks
All labs: [Brute-force attacks](01-brute-force-attacks/README.md)  

#### Username enumeration
- [x] Username enumeration via different responses
- [x] Username enumeration via subtly different responses
- [x] Username enumeration via response timing

