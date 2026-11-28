"""
The Chinese Remainder Theorem gives a unique solution to a set of linear congruences if their moduli are coprime.

This means, that given a set of arbitrary integers aiai, and pairwise coprime integers nini, such that the following linear congruences hold:

Note "pairwise coprime integers" means that if we have a set of integers {n1,n2,...,ni}{n1,n2,...,ni}, all pairs of integers selected from the set are coprime: gcd⁡(ni,nj)=1gcd(ni,nj)=1.

x≡a1mod  n1x≡a1modn1
x≡a2mod  n2x≡a2modn2
……
x≡anmod  nnx≡anmodnn

There is a unique solution x≡amod  Nx≡amodN where N=n1⋅n2⋅...⋅nnN=n1⋅n2⋅...⋅nn.

In cryptography, we commonly use the Chinese Remainder Theorem to help us reduce a problem of very large integers into a set of several, easier problems.

Given the following set of linear congruences:

x≡2mod  5x≡2mod5
x≡3mod  11x≡3mod11
x≡5mod  17x≡5mod17

Find the integer aa such that x≡amod  935x≡amod935

Starting with the congruence with the largest modulus, use that for x≡amod  px≡amodp we can write x=a+k⋅px=a+k⋅p for arbitrary integer kk.
"""
range_lenght = 5 * 11 * 17  # mod 5 , mod 11, mod 17 # mora da prodje kroz sve brojeve koji spadaju u skup mogucih iz ta tri modula
# range_lenght == 935

for x in range(range_lenght):
    if x % 5 == 2 and x % 11 == 3 and x % 17 == 5:
        print(f"Sva tri uslova ispinjava integer a: {x}")
