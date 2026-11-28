"""
Let aa and bb be positive integers.

The extended Euclidean algorithm is an efficient way to find integers u,vu,v such that

a⋅u+b⋅v=gcd⁡(a,b)a⋅u+b⋅v=gcd(a,b)

Later, when we learn to decrypt RSA ciphertexts,
 we will need this algorithm to calculate the modular inverse of the public exponent.

Using the two primes p=26513,q=32321p=26513,q=32321, find the integers u,vu,v such that

p⋅u+q⋅v=gcd⁡(p,q)p⋅u+q⋅v=gcd(p,q)

Enter whichever of uu and vv is the lower number as the flag.

Knowing that p,qp,q are prime, what would you expect gcd⁡(p,q)gcd(p,q) to be? 
For more details on the extended Euclidean algorithm, check out this page.
"""

# ax + by = gcd(a,b)  - Bezautov identitet

def extended_gcd(a,b):

    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


a = 26513 
b = 32321

gcd, x, y = extended_gcd(a,b)

print("GCD:", gcd)
print("x:", x)
print("y:", y)




