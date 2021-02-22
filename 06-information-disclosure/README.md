Information Disclosure

# Information Disclosure

When a website unintentionally reveals sensitive information to its user, it referred as Information disclosure/information leakage

Websites may leak these things:
- Data about other users, such as usernames or financial information
- Sensitive commercial or business data
- Technical details about the website and its infrastructure

## Examples of information disclosure

- Backup data or git repository
- Debug info
- Hidden directories found in robots.txt
- Application unintentionally reveals database column/table name in error messages
- Hardcoded API key, credentials, IP address, and database in source code

## Impact

Attacker may able to craft exploits according to the leaked technical information, or use sensitive users data to do phishing attack.

## Prevention

- Double check debugging mode/verbose mode are disabled in production environment.
- Remove any potential information disclosure in code review or QA.
- Use generic error messages.

# Labs

### How to find and exploit information disclosure vulnerabilities
All labs: [How to find and exploit information disclosure vulnerabilities](01-exploit-information-disclosure-vulnerabilities.md) 

- [x] Information disclosure in error messages
- [x] Information disclosure on debug page
- [x] Source code disclosure via backup files
- [x] Authentication bypass via information disclosure
- [x] Information disclosure in version control history