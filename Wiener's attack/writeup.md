# Wiener's attack
Wiener's attack is a cryptographic attack on RSA that targets scenarios where the private key d is unusually small. Specifically, it exploits the mathematical properties of RSA when the private key 
d is small relative to the modulus N. This attack was introduced by Michael J. Wiener in 1990.

## When Does Wiener's Attack Work?
Wiener's attack is effective when the private key d is small enough such that:

![image](https://github.com/user-attachments/assets/86d5d465-6b0d-4dc7-a3d0-c70688934371)

We know that e.d congruent to 1(mod(phi(N)) 
We can rewrite it as e.d=k*phi(N)+1
After rearranging:

![image](https://github.com/user-attachments/assets/826dd0d5-8b34-4302-91b3-0228339ad33a)

d/phi(N) approx. = k/e

d/phi(N) can be represented by a continued fraction

### But what are continued fractions?
continued fractions are a way to represent real numbers as an expression involving a sequence of integer divisions. A continued fraction is expressed as a sum, where each term after the first is the reciprocal of an integer plus the next term in the sequence. This representation is particularly useful for approximating irrational numbers and finding the best rational approximations for real numbers.

Basic Form of a Continued Fraction
A simple continued fraction has the form:

![image](https://github.com/user-attachments/assets/5a7710da-235a-4f52-92d2-d417a8b8253a)
 
Where:
a0 is the integer part of x.

a1,a2,a3,… are the coefficients that form the continued fraction.

## Continued fractions and convergents
d/phi(N) can be represented by a continued fraction of e/n.
Further, e/n can be represented as a continued fraction of k/d
The continued fraction will produce a series of convergents 
k1/d1,k2/d2 and so on that approximate e/N
### Find Convergents:

These convergents are candidate values for k/d
For each convergent ki/di test if the di value works in the equation e.di convergent with 1(phi(N))
Once we get d, we can easily decrypt.
