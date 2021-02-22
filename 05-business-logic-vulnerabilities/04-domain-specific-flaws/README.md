Table of contents
---
[toc]
# Domain-specific flaws

## Lab #12: Flawed enforcement of business rules

Credentials: `wiener:peter`

Normal order

![6bcf9b6d2a72e766f870236a26178292.png](_resources/5444a9c6a8f44f979dd3896eccaa9389.png)

We could use BurpSuite repeater to repeat the request on applying the coupon code to see if it can be stacked with the same coupon.

![a14ef3e2c9e3a0e9951af32faca9d4f6.png](_resources/c3d9c7576362425988adf3162b334811.png)

Since it cannot be stacked with the same coupon, let's try with another coupon.  

![2f5b12b02c1db667b6853ddd0b2498c2.png](_resources/3e2cd190a64a4309b10a710961f71bab.png)

And repeat the use of different coupon alternately

![0637c56380c54335d1b43c630d0c33cb.png](_resources/dc4d9dd6385b49678e8e6a760d44fe30.png)

It broke the application logic

![39b96b5939a857e0dea44aecf9d0c659.png](_resources/3ced7d55deed42c787823e31a4a388bd.png)

