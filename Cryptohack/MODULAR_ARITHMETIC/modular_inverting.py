"""
As we've seen, we can work within a finite field FpFp​, adding and multiplying elements, 
and always obtain another element of the field.

For all elements gg in the field, there exists a unique integer dd such that g⋅d≡1mod  pg⋅d≡1modp.

This is the multiplicative inverse of gg.

Example: 7⋅8=56≡1mod  117⋅8=56≡1mod11

What is the inverse element: d=3−1d=3−1 such that 3⋅d≡1mod  133⋅d≡1mod13?

Think about the little theorem we just worked with. How does this help you find the inverse of an element?

"""
print(pow(3,-1,13)) # 9