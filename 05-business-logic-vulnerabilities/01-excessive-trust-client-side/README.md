Table of contents
---
[toc]
# Excessive trust in client-side controls


## Lab #1: Excessive trust in client-side controls

Example case on e-commerce web apps:


Intercept request and manipulate product price before it enters the shopping cart

![72aa258ccc396ca77f623eac3b1ddcef.png](_resources/0900d5ec85ed42da88ca525436a2d7ac.png)

Later, in the shopping cart it's shown as only $0.10 in price.

![faa5e5db0c699cd47b6f72c77d1d2a7c.png](_resources/ac848c4ac8c342619837a68b863ce848.png)

When the original price is $1337

![ed78d4a4a770b16667885896572aa182.png](_resources/0a99ed36d14c444fa4e1a1a4348fb677.png)

## Lab #2: 2FA broken logic

Your credentials: `wiener:peter`
Victim's username: `carlos`

![11cf898d58da9d5a5766faf07ab3e5e9.png](_resources/0984752330e0408f9229483dbac5cf24.png)

Intercept login request as well as the request responses.

![5065850ed2d619bdc0ac3404c27f671d.png](_resources/8f240dca20684d4db28009ef77077ba2.png)

We could change the `verify` value to carlos for both request and response

![c256a8359a9cc14c4b1f5072cb7352eb.png](_resources/36bb681a856b4cf6bde21c81c0d15d41.png)

Now it'll send a 4 digit verification into the carlos e-mail

![fbb07ba8d46a508051b43ab872bc6153.png](_resources/e525c10d181646fbb8e23022390c0940.png)

With this attackers could brute force to guess the correct pin
(10.000 tries for all possible combination)

![3573ef1a12e6c01be5a8d2f857cc9263.png](_resources/9ddbbc4760654a92ba47759b041eae1d.png)


![a16ef3b91fa90e2d772138f5a9c5df05.png](_resources/589d3205ad714502bec1d8f6d88627f5.png)

When we have the correct one, we'll logged in as carlos 