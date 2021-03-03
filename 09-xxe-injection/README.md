# XML External Entity

## What is XML?

XML stands for "extensible markup language". XML is a language designed for storing and transfering data. It's designed to be human and machine readable.   

XML has a tree-like structure like HTML, but unlike HTML, XML doesn't have predefined tags instead we define the tag by ourself.  

Each defined tags can also have attributes.

Below is the example of how xml document structured:

```xml
<?xml version="1.0" encoding="UTF-8"?> 
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note> 
```

1. XML Prolog (not neccessary, but good practice)
`<?xml version="1.0" encoding="UTF-8"?>`
2. XML root element (this is a **must!**)
	```xml
	<note> 
		...
		...
		...
	</note>
	```
3. XML children of root element are 
	```xml
	...
		<to></to>
		<from></from>
		<heading></heading>
		<body> </body>
	...
	```

Without a root element, an XML document would be considered as invalid XML.

## Document Type Definition (DTD)

A DTD defines the stucture and attributes of an XML document. XML document allows validation using DTD.  

DTD can be declared from inside and outside of XML document. 
  
### Internal DTD 
Internal DTD is declared inside the XML document

```xml
<?xml version="1.0"?>
<!DOCTYPE note [
<!ELEMENT note (to,from,heading,body)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT body (#PCDATA)>
]>
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend</body>
</note>
``` 


### External DTD

External declaration uses a reference to a DTD file. The reference are placed/wrapped inside `<!DOCTYPE>`  

filename: note.dtd
```
<!ELEMENT note (to,from,heading,body)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT body (#PCDATA)>
```

filename: note.xml
```xml
<?xml version="1.0"?>
<!DOCTYPE note SYSTEM "note.dtd" > 
<note>
	<to>Tove</to>
	<from>Jani</from>
	<heading>Reminder</heading>
	<body>Don't forget me this weekend</body>
</note>
```

Example above is assuming the `note.xml` file and `note.dtd` are in the same folder.


## XML/DTD entities

Entities are used to define shortcuts to special characters.  

Entities can be declared internal or external.  

Example of internal declaration:
```xml
<?xml version="1.0"?>
<!DOCTYPE note [<!ENTITY name "fahmifj">] >
<note>
	<to>Tove</to>
	<from>&name;</from>
	<heading>Reminder</heading>
	<body>Don't forget this is internal entity</body>
</note>
```

> An entity has three parts: an ampersand (&), an entity name, and a semicolon (;).


Example of external declaration:
```xml
<?xml version="1.0"?>
<!DOCTYPE note [<!ENTITY name SYSTEM "http://somewhere.com/entity.dtd">] >
<note>
	<to>&name;</to>
	<from>You</from>
	<heading>Reminder</heading>
	<body>Don't forget this is external entity</body>
</note>
```

An external entity can use several scheme other than `http://` like `file://` and `ftp://`

# Labs

Example of XXE attacks with hands on lab:

- [ ] Exploiting XXE using external entities to retrieve files
- [ ] Exploiting XXE to perform SSRF attacks

## Blind XXE vulnerabilities

- [ ] Blind XXE with out-of-band interaction
- [ ] Blind XXE with out-of-band interaction via XML parameter entities
- [ ] Exploiting blind XXE to exfiltrate data using a malicious external DTD
- [ ] Exploiting XXE to retrieve data by repurposing a local DTD


## Finding hidden attack surface for XXE injection

- [ ] Exploiting XInclude to retrieve files
- [ ] Exploiting XXE via image file upload
