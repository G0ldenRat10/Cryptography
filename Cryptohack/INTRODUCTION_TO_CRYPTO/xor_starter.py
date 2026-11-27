"""
XOR is a bitwise operator which returns 0 if the bits are the same, 
and 1 otherwise. In textbooks the XOR operator is denoted by ⊕, 
but in most challenges and programming languages you will see the caret ^ used instead.

A	B	Output
0	0	  0
0	1	  1
1	0	  1
1	1	  0

For longer binary numbers we XOR bit by bit: 0110 ^ 1010 = 1100. 
We can XOR integers by first converting the integer from decimal to binary. 
We can XOR strings by first converting each character to the integer representing the Unicode character.

Given the string label, XOR each character with the integer 13. 
Convert these integers back to a string and submit the flag as crypto{new_string}.

The Python pwntools library has a convenient xor() function that can XOR together data of different types and lengths. 
But first, you may want to implement your own function to solve this. 

"""
# Prvi kod:
"""
s = "label"
n = 13 

def challenge(s,n):
    unicode_s = []
    for l in s:
        unicode_s.append(ord(l))
    print(f"Before XOR with 13: {unicode_s}")

    xored_13_unicode_s = []
    for n in unicode_s:
        xored_13_unicode_s.append(n ^ 13)
    print(f"After XOR with 13: {xored_13_unicode_s}")

    flag = ""
    for n in xored_13_unicode_s:
        flag += chr(n)

    return flag

print(f"The flag is crypto/{challenge(s,n)}/")
"""

# Drugi kod:

text = "label"
key = 13

def challenge(text, key):
    return ''.join(chr(ord(char) ^ key) for char in text)
print(f"The flag is: crypto/{challenge(text,key)}/")

