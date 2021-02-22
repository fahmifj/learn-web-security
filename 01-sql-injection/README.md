# SQL injection
## What is SQL injection ?

PortSwigger Web Security Academy defines SQL injection as:

>"A web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database"

## What is the impact of a successful SQL injection attack?

- Accessing sensitive data
- Data exfiltration/database dump
- System take over

# Labs 

Examples of SQL injection and way to detect it are included in the hands-on labs:

### Retrieving hidden data

- [x] [SQL injection vulnerability in WHERE clause allowing retrieval of hidden data](01-retrieving-hidden-data/README.md)
### Subverting application logic
- [x] [SQL injection vulnerability allowing login bypass](02-subverting-app-logic/README.md)

### UNION attack
All labs: [UNION attack](03-union-attacks/README.md)
- [x] SQL injection UNION attack, determining the number of columns returned by the query
- [x] SQL injection UNION attack, finding a column containing text
- [x] SQL injection UNION attack, retrieving data from other tables
- [x] SQL injection UNION attack, retrieving multiple values in a single column

### Examining the database
All labs: [Examining the database](04-examining-the-database-type/README.md)

- [x] SQL injection attack, querying the database type and version on Oracle
- [x] SQL injection attack, querying the database type and version on MySQL and Microsoft
- [x] SQL injection attack, listing the database contents on non-Oracle databases
- [x] SQL injection attack, listing the database contents on Oracle

## Blind SQL injection

All labs: [Blind SQL injection](05-blind-sql-injection/README.md)


- [x] Blind SQL injection with conditional responses
- [x] Blind SQL injection with conditional errors
    - Script: https://gist.github.com/fahmifj/13d055117f729a233a8f4ccbefdb1680
- [x] Blind SQL injection with time delays


## Cheatsheet
Different database type has different SQL injection techniques, but it works identically.

- [PortSwiggerSQLi Cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- [PayloadAllTheThings SQL Injection Cheatsheet](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection)


## Prevent SQL injection

- Don't put direct input to the database query, evaluate the user input before placed into the query.