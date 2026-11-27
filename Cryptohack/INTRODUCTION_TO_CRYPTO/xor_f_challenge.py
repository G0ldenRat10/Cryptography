"""
I've encrypted the flag with my secret key, you'll never be able to guess it.

Remember the flag format and how it might help you in this challenge!

0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104 

"""

from Crypto.Util.strxor import strxor

cipher = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
print(f"Lenght of cipher in bytes: {len(cipher)}")

# cipher = flag XOR key => key = cipher XOR flag (ja imam jedan deo flag-a)

known = b"crypto{"

# mora ZIP jer CIPHER i deo flag-a nisu iste duzine pa nije moguc XOR sa strxor
key_part = bytes(c ^ k for c, k in zip(cipher,known))  # kad istekne known i ostane ostatak cipher-a ne uparuje ga dalje nisacim
key = key_part + b'y'
print(f"Current key: {key}")

# flag = cipher XOR key (asocijativnost)
flag_part = bytes(c ^ k for c, k in zip(cipher, key))
print(flag_part)


