"""
For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d 
"""

from Crypto.Util.strxor import strxor

cipher = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
for byte in cipher:
    print(byte)
# Jedan Byte ima 8 bitova, 2 na 8i stepen = 256 => 0 - 255
#for key in range(256):

        
