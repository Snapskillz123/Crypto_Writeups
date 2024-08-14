import gmpy2
from gmpy2 import mpz
from functools import reduce

# Function to calculate the Chinese Remainder Theorem (CRT)
def chinese_remainder_theorem(n, a):
    sum = 0
    prod = reduce(lambda x, y: x * y, n)
    
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

# Function to calculate the modular inverse
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# Function to perform Håstad's Broadcast Attack
def hastads_broadcast_attack(ciphertexts, moduli, e):
    # Apply CRT to get the combined result
    combined_c = chinese_remainder_theorem(moduli, ciphertexts)
    
    # Compute the e-th root of the combined ciphertext
    m = gmpy2.iroot(mpz(combined_c), e)[0]  # e-th root
    return m

def main():
    # Example RSA parameters (ciphertexts and moduli from different recipients)
    e = 3
    
    # Three recipients with different moduli and ciphertexts
    moduli = [
        mpz(784313),  # n1
        mpz(1043993),  # n2
        mpz(1256871)  # n3
    ]
    
    ciphertexts = [
        mpz(157321),  # c1
        mpz(886919),  # c2
        mpz(1052191)  # c3
    ]
    
    # Perform Håstad's Broadcast Attack
    plaintext = hastads_broadcast_attack(ciphertexts, moduli, e)
    
    # Output the decrypted plaintext
    print(f"Decrypted plaintext: {plaintext}")

if __name__ == "__main__":
    main()
