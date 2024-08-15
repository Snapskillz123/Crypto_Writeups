# Coppersmith attack

The Coppersmith attack is a method used in cryptanalysis, specifically targeting the RSA (Rivest-Shamir-Adleman) encryption algorithm. Named after Don Coppersmith, the attack focuses on finding small roots of polynomial equations modulo an integer, which is particularly relevant in RSA when certain conditions are met.
## 1. Small Exponent Attack:
Suppose the public exponent (e) in RSA is small (like 3 or 65537), and the ciphertext is also small (for example, the message is shorter than the modulus n). In that case, the Coppersmith attack can  recover the plaintext directly from the ciphertext without needing to factorize n.
The small exponent attack in RSA exploits the weakness that arises when the public exponent e is small, typically e=3 or e=5.

### a.Direct Decryption 
If m^e <n, then:
c=m^e 
In this case, the attacker can directly compute the e-th root of c to recover m
This works because there's no need for modular arithmetic when  e is smaller than n

### b. Håstad's Broadcast Attack
This attack applies when the same message m is encrypted with the same small public exponent e but sent to multiple recipients with different moduli 𝑛1,𝑛2...𝑛𝑘.
The attack exploits the Chinese Remainder Theorem (CRT) to combine these different ciphertexts into one, allowing the attacker to solve for 𝑚




## 3. Small Private Exponent Attack:
If the private exponent (d) is small, the attack can be used to find d efficiently. This is dangerous because d is the key to decrypting messages in RSA; if it is small, it makes RSA vulnerable.
## 4. Lattice-Based Methods:
The attack utilizes lattice reduction techniques (such as the LLL algorithm) to find small roots of polynomials, which allows the recovery of plaintext in certain scenarios.
