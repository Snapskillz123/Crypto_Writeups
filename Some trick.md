# Some trick

This is the script:
```
import random
from secrets import randbelow, randbits
from flag import FLAG

CIPHER_SUITE = randbelow(2**256)
print(f"oPUN_SASS_SASS_l version 4.0.{CIPHER_SUITE}")
random.seed(CIPHER_SUITE)

GSIZE = 8209
GNUM = 79

LIM = GSIZE**GNUM


def gen(n):
    p, i = [0] * n, 0
    for j in random.sample(range(1, n), n - 1):
        p[i], i = j, j
    return tuple(p)


def gexp(g, e):
    res = tuple(g)
    while e:
        if e & 1:
            res = tuple(res[i] for i in g)
        e >>= 1
        g = tuple(g[i] for i in g)
    return res


def enc(k, m, G):
    if not G:
        return m
    mod = len(G[0])
    return gexp(G[0], k % mod)[m % mod] + enc(k // mod, m // mod, G[1:]) * mod


def inverse(perm):
    res = list(perm)
    for i, v in enumerate(perm):
        res[v] = i
    return res


G = [gen(GSIZE) for i in range(GNUM)]


FLAG = int.from_bytes(FLAG, 'big')
left_pad = randbits(randbelow(LIM.bit_length() - FLAG.bit_length()))
FLAG = (FLAG << left_pad.bit_length()) + left_pad
FLAG = (randbits(randbelow(LIM.bit_length() - FLAG.bit_length()))
        << FLAG.bit_length()) + FLAG

bob_key = randbelow(LIM)
bob_encr = enc(FLAG, bob_key, G)
print("bob says", bob_encr)
alice_key = randbelow(LIM)
alice_encr = enc(bob_encr, alice_key, G)
print("alice says", alice_encr)
bob_decr = enc(alice_encr, bob_key, [inverse(i) for i in G])
print("bob says", bob_decr)

```
Basically G is a 2D matrix 8209*79. It's then randomized in the gen function and altered in the gexp function and the encrypted.
We have been given alice's encrypted message, bob's encrypted message and bob's  decrypted message using alice's encrypted message and then inverse of the G matrix.
Since we have the seed, we can obtain the original G matrix
Now we need to bruteforce using this matrix that we have.
```
GSIZE = 8209
flag = []
b_k = bob_key
b_e = bob_encr
for g in G:
    mm = b_k % GSIZE
    for k in range(GSIZE):
        if mm == b_e % GSIZE:
            flag.append(k - 1)
            break
        mm = g[mm]
    b_k //= GSIZE
    b_e //= GSIZE

flag_rec = sum(x * GSIZE**i for i, x in enumerate(flag_rec))
```
(Thanks madhav 😁)
But yeah so basically it takes the key and encrypted message and reduces it to a field of 8208.
if ```key % 8209 == encrypted % 8209``` then k is a part of the padded flag. k-1 because of index position.
with mm=g[mm], we are basically tracking back the permutations. We then integer divide by 8209 to deconstruct the key and the encrypted message.
We now add all the elements of the flag list to construct the padded flag.
now we just search through the padded flag for SEKAI{<flag content>} and we're done

## Flag
SEKAI{7c124c1b2aebfd9e439ca1c742d26b9577924b5a1823378028c3ed59d7ad92d1}
