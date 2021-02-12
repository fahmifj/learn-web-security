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

# Vulnerabilities in password-based login

## Brute-force attacks

### Brute-forcing usernames
Easy to guess by naming convention like,

`firstname.lastname@corporation.com`
`firstinitialname.lastname@corporation.com`

Notes for auditing:

- Is the website discloses a potential username publicly?
- Is a profile accessible without logging in?
- Contact email = potential IT support/sysadmin with high privileges.

### Brute-forcing passwords
Predictable password can improves success rate in brute force especially dictionary attack, therefore attackers may have an up to date wordlist.


### Username enumeration
Attackers may observe changes in the website before brute-forcing.

For examples, when attackers enter one username and a random password, the application might reply that the given username is valid but the password is incorrect.
Therefore, attackers can enumerate the valid usernames which then reduce the time cost required to do brute-force.
