# SQL injection
## What is SQL injection ?
PortSwigger Web Security Academy defines SQL injection as:

>"A web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database"

## Impact of a successful SQL injection attack?
There are many harmful things that attackers could do with SQL injection attacks, to keep it short, see how it compared to the CIA triad.

- **Confidentiality**: SQLi can be used to view sensitive data/information (usernames, passwords, emails)
- **Integrity**: SQli can be used to alter data in database.
- **Availability**: SQLi can be used to delete data or even the tables in database.

SQLi could also lead to Remote Code Execution (RCE)

## Type of SQL injection

### In-band SQL injection
An in-band SQL injection uses the same communication channel to attack and gather the result of the attack. The result of the attack are presented in the web application page.  

An in-band SQLi divided into two:
- **Error-based SQLi**, is a technique that forces the database to generate an error. This can gives the attackers information about the back-end process of the vulnerable application and then refine their payload.
- **Union-based SQLi**, is a technique that leverages the SQL UNION operator to combine the result of the original query of the application with the malicious query by the attackers.

### Blind SQL injection
A blind SQL injection occurs when the application is vulnerable to SQL injection attack but the result of the attack are not displayed directly in the web page.

Even if the attackers couldn't see the result directly from the web page, they can observe the behaviour of application response to construct the information.

Because of that, a blind SQL injection could takes longer to exploit and mostly require a certain skill set to automate the exploit.

Blind SQL injection also can be divided into two:
- **Boolean-based**, is a technique where a set of Boolean condition is sent to the application to expect different result which will then be compared based on TRUE or FALSE result.
- **Time-based**, is a technique that uses a SQL query to delay the application proccess.

### Out-of-Band (OAST) SQL injection 
An out-of-band SQLi uses the ability of the application to interact with external network or system that you control.

This type of SQLi is not common and require certain features being enabled in the database.

## Finding SQL injection
Based on perspective of testing

### Black Box Testing
Black Box tester has limited to no information about the system. Usually it only has access to:
- Application URL
- The scope of the engagement

Methodology:
- Map the application
    - Explore the accessible part of the application (both visible and not visible)
    - List all of the input vectors and note it
    - Observing the application behaviour (function, request, response)
- Fuzzing the application input vectors and observe the application response or the time taken to respond.
    - Submit SQL-specific characters (`'`, `"`, `#`, `--`, `;`)
    - Submit Boolean conditions (`AND 1=1`, `AND 1=2`, `OR 1=1`)
    - Submit OAST SQLi payload to trigger an out-of-band network interaction and monitor it.

### White Box Testing
White Box tester has access to the complete system and source code of the application

Methodology:
- Enable web server logging
- Enable database logging
- Map the application
    - Regex search all functions in code that interact with the database.
    - Code review
        - Follow code path for all input vectors
- Fuzz the application input vectors

## Prevent SQL injection

- Don't put direct input to the database query, evaluate the user input before placed into thsde query.

## Exploiting SQL injection

### Labs 

Examples of exploiting SQL injection and way to detect it are included in the hands-on labs:

#### Retrieving hidden data
- [x] [SQL injection vulnerability in WHERE clause allowing retrieval of hidden data](01-retrieving-hidden-data/README.md)

#### Subverting application logic
- [x] [SQL injection vulnerability allowing login bypass](02-subverting-app-logic/README.md)

#### UNION attack
All labs: [UNION attack](03-union-attacks/README.md)
- [x] SQL injection UNION attack, determining the number of columns returned by the query
- [x] SQL injection UNION attack, finding a column containing text
- [x] SQL injection UNION attack, retrieving data from other tables
- [x] SQL injection UNION attack, retrieving multiple values in a single column

#### Examining the database
All labs: [Examining the database](04-examining-the-database-type/README.md)
- [x] SQL injection attack, querying the database type and version on Oracle
- [x] SQL injection attack, querying the database type and version on MySQL and Microsoft
- [x] SQL injection attack, listing the database contents on non-Oracle databases
- [x] SQL injection attack, listing the database contents on Oracle

#### Blind SQL injection
All labs: [Blind SQL injection](05-blind-sql-injection/README.md)
- [x] Blind SQL injection with conditional responses
- [x] Blind SQL injection with conditional errors
    - Script: https://gist.github.com/fahmifj/13d055117f729a233a8f4ccbefdb1680
- [x] Blind SQL injection with time delays
- [ ] Blind SQL injection with time delays and information retrieval
- [ ] Blind SQL injection with out-of-band interaction
- [ ] Blind SQL injection with out-of-band data exfiltration


## Cheatsheet
Different database type has different SQL injection techniques, but it works identically.

- [PortSwiggerSQLi Cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- [PayloadAllTheThings SQL Injection Cheatsheet](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection)

## References
- Web Security Academy - SQL injection
    - https://portswigger.net/web-security/sql-injection
- SQL Injection Complete Guide by Rana Khalil
    - https://www.youtube.com/watch?v=1nJgupaUPEQ