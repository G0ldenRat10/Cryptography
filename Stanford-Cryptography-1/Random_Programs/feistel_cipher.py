import hashlib
import hmac
import secrets

# bitvajs funkcije za osnovni rad 

def mask(n: int) -> int:
    return (1 << n) - 1;

def split(block: int, n: int) -> tuple[int,int]:
    L = block >> n
    R = block & mask(n) 
    return [L, R]

def join(L: int, R: int, n: int) -> int:
        return (L << n) | R