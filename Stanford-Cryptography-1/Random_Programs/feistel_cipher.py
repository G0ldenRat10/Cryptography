import hashlib
import hmac
import secrets

# master key za testiranje

master_key = secrets.token_bytes(16) # == 128 bitova
# print(master_key.hex())

# bitvajs funkcije za osnovni rad 

def mask(n: int) -> int:
    return (1 << n) - 1;

def split(block: int, n: int) -> tuple[int,int]:
    L = block >> n
    R = block & mask(n) 
    return [L, R]

def join(L: int, R: int, n: int) -> int:
        return (L << n) | R


# funkcije rundi i kljucevi rundi

def F(key: bytes, x: int, n: int) -> int:   # key = master_key; x = L -> x; n = broj bajtova (8)
    nbytes = (n+7) // 8                     # zbog +7 (najveci ostatak pri deljenju sa 8), svaki n koji nije deljiv sa 8 predje na sledeci ceo kolicnik, a deljiv ne
    xb = x.to_bytes(nbytes, "big")
    h = hmac.new(key, xb, hashlib.sha256)
    digest = h.digest()