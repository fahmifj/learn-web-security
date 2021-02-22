Table of contents
---
[toc]
# Failing to handle unconventional input

Example case:
```
$transferAmount = $_POST['amount'];
$currentBalance = $user->getBalance();

if ($transferAmount <= $currentBalance) {
    // Complete the transfer
} else {
    // Block the transfer: insufficient funds
}
``` 

Initial balance  
attackers : $1000
victim : $2000

attacker sent $1000  
$-1000 => victim balance's

victim's balance after receiving the transfer  
`$2000 + (-$1000) = $1000`

recalculate attacker's balance after transfer  
`$1000 - (-$1000) = $2000`

## Lab #3: High-level logic vulnerability

Credentials: `wiener:peter`  


![1b21b47fa5f4b29d6da727d2a9df313d.png](_resources/f8ce9de00c2b48fa885b90ae4fd694aa.png)

![9e985c3a916c35835988e979c94084b5.png](_resources/ddb7d23acf0f4ec08f5a49c89574f755.png)

Modify request body

```
productId=1&redir=PRODUCT&quantity=-10
```

Resulting the product quantity turn to `-10` in the shopping cart.

![9c442f3516bfbf0aa962957f0834be18.png](_resources/513c6a0657ab48f5ae4e24c99aa37363.png)

At this time, it states total price cannot be less than zero

![71f3aeab935f54729526588e4ef79a32.png](_resources/e0e4663dc851404aa58bb348d4ab3373.png)

Now, what if we add another items with normal price to cover the minus of the total price?

![a5e27a4eae71a4ae5d76b42c4886e9bf.png](_resources/0a46c659db3c4e028a9e2136596f4b1f.png)

We can do the opposite as well.

![80b7af48c352f0262a2b8093ff4c8dc0.png](_resources/034a8098ca4f442bbad2a59bbcbd54a6.png)