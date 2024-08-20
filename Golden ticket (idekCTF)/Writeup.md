# Golden ticket

So bascially we've been given the equation:

![image](https://github.com/user-attachments/assets/7929c3de-c220-4a0d-8a67-cc5a39006267)

where m is the flag in integer.
Since there is addition and all we can't directly apply discrete log.
In the output, we've been given flag_chocolate which is a variable which stores the value of when golden ticket(flag in integer) is put into the equation given above.
So we have the last element of the loop where numbers for 0 to golden_ticket-1 are put into the equation.
from these two given values, we can get two equations:

![image](https://github.com/user-attachments/assets/07b6cceb-5439-4210-9f61-426ab0acae0c)

Since the outer mod doesn't change the values of the equation we can omit it.
The new equations now looks like this:

![image](https://github.com/user-attachments/assets/93864a7c-f8b7-422f-9d97-c65bed269dd1)

Now we just need to manipulate the euqation to get rid of the -ve and +ve sign coz they're just ruining our equation.

What we can do is ```(6)-13(7)```
We now have:

![image](https://github.com/user-attachments/assets/d718fb61-810e-4eb3-b523-4853e452f482)

We can then calculate the multiplicative inverse of 24 and find the modular inverse of it.

the equation is finally ```(inv(24) * modinv(24, p)) % p= 37^m-1```

We get m-1 from appplying DLP and then +1 get us m.
convert to bytes and voila we have our flag.




