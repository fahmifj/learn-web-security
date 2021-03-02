# Server-Side Request Forgery 

From [PortSwigger](https://portswigger.net/web-security/ssrf):

> Server-side request forgery (also known as SSRF) is a web security vulnerability that allows an attacker to induce the server-side application to make HTTP requests to an arbitrary domain of the attacker's choosing.


## Impact of SSRF

- Broke trust relationship, allowing attacker to access internal assets
- Attackers could forge request that originate from the organization that hosting the vulnerable application


## Example of SSRF attacks

### Common SSRF attacks
All labs: [Common SSRF attacks](01-common-ssrf-attacks/README.md)
- [x] SSRF attacks against the server itself
- [x] SSRF attacks against other back-end systems

### Circumventing common SSRF defenses
All labs: [Circumventing common SSRF defenses](02-circumventing-common-ssrf-defenses/README.md)
- [x] SSRF with blacklist-based input filters
- [x] SSRF with whitelist-based input filters

### Blind SSRF
All labs: [Blind SSRF](03-blind-ssrf/README.md)
- [x] Blind SSRF with out-of-band detection
- [ ] Blind SSRF with Shellshock exploitation