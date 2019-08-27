#!/usr/bin/env python3

##(m**e)**d = m (% n)
# n and e are part of the public key
# have two distinct primes

from Crypto.util.number import inverse

p = 
q = 

# n is released as part of the public key
# n, c and e are often given, you can try and use factordb to find p and q
n = p*q



c = 

#   e having a short bit-length and small Hamming weight results in more efficient encryption  – the most commonly chosen value for e is 216 + 1 = 65,537. The smallest (and fastest) possible value for e is 3, but such a small value for e has been shown to be less secure in some settings.[14]
#   e is released as part of the public key.
e = 



#compute λ(n)
# Since n = pq, λ(n) = lcm(λ(p),λ(q)), and since p and q are prime, λ(p) = φ(p) = p − 1 and likewise λ(q) = q − 1. Hence λ(n) = lcm(p − 1, q − 1). 
phi = (p - 1)*(q - 1)


# Determine d as d ≡ e−1 (mod λ(n)); that is, d is the modular multiplicative inverse of e modulo λ(n).
d = inverse(e,phi)

m = pow (c, d, n) 

##for a ctf, you can use hex2string for the flag.
print(hex(m).decode('hex'))

