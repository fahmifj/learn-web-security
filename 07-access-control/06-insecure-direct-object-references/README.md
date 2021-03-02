# Insecure direct object references

IDOR arises when an application uses user-supplied input to access objects directly and an attacker can modify the input to obtain unauthorized access

## Lab #10: Insecure direct object references

> This lab stores user chat logs directly on the server's file system, and retrieves them using static URLs.
>
> Solve the lab by finding the password for the user carlos, and logging into their account. 

Requesting chat transcript

![2eb5446de8cb94e50eb7ed864f37f5da.png](_resources/1e7de69dbec64ff591d34990a19ae166.png)

It returns 302 Found redirection to a new location of text file.
![1f85d353e1f0723b1a65f50b86308971.png](_resources/c9be1a7f0bd34744b64440b32615ce43.png)

By modifying the text file name from 2 to 1,

![bf68c78d5e382c65418590e89d26e5fd.png](_resources/bda1f9b85f264cde8c74d01b19ab8755.png)

It follows the redirection with the new file name, `1.txt`, in the request url.
 
![0ce1495128a0f015e45dd483a6f921c8.png](_resources/20122c123e9b4d6eb18763d5cf367f25.png)

Discovered a password from chat log 
![3d3e503ede3e8e331a58ce4d1a27f28e.png](_resources/2b5c2a8618844403a4147fc62713a5b7.png)