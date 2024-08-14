import gmpy2

def small_exponent_decrypt(c, e, n):
    # Try to compute the e-th root of c
    # In this case, c = m^e, so we need to compute the e-th root
    m = gmpy2.iroot(c, e)[0]  # Extract the e-th root of c
    if pow(m, e) == c:  # Verify if m^e == c to ensure it's the correct root
        return m
    else:
        return None  # If not, decryption failed (not a simple e-th root case)

def main():
    # Example RSA parameters with small e
    e = 3
    n = 2773  # Example modulus
    c = 1728  # Example ciphertext (c = m^3)

    # Decrypt the ciphertext
    plaintext = small_exponent_decrypt(c, e, n)

    if plaintext:
        print(f"Decrypted plaintext: {plaintext}")
    else:
        print("Decryption failed.")

if __name__ == "__main__":
    main()
