"""
I've encrypted the flag with my secret key, you'll never be able to guess it.

Remember the flag format and how it might help you in this challenge!

0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104 

"""

from Crypto.Util.strxor import strxor

cipher = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

for key in range(256):
    result = bytes(byte ^ key for byte in cipher) # svaki bajt pojedinacno u cipher-u i XOR sa kljucem u range (256) vraca rezultat
    print(key,result)