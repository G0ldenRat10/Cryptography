import hashlib
import hmac
import secrets


def mask(n: int) -> int:
    return (1 << n) - 1;


print(mask(4))