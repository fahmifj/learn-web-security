# SQL injection
## What is SQL injection ?

PortSwigger Web Security Academy defines SQL injection as:

>"A web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database"


## What is the impact of a successful SQL injection attack?

- Accessing sensitive data
- Data exfiltration/database dump
- System take over

## SQL injection examples techniques (hands-on labs)

Examples of SQL injection and way to detect it are included in the hands-on labs:
- [Retrieving hidden data](01-retrieving-hidden-data/README.md)
- [Subverting application logic](02-subverting-app-logic/README.md)
- [UNION attack](03-union-attacks/README.md)
- [Examining the database](04-examining-the-database-type/README.md)
- [Blind SQL injection](05-blind-sql-injection/README.md)

Different database type has different SQL injection techniques, but it works identically.

- [PortSwiggerSQLi Cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)


## Prevent SQL injection

- Don't put direct input to the database query, evaluate the user input before placed into the query.