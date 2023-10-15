#pythogarean triplet

import math
def pythagorean_triplet():
    for a in range(1, 1000):
        for b in range(a, 1000):  # Start b from a to avoid duplicate triples
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a, b, c

triplet = pythagorean_triplet()
if triplet is not None:
    a, b, c = triplet
    product = a * b * c
    print(f"The Pythagorean triplet is ({a}, {b}, {c}), and the product is {product}")
else:
    print("No Pythagorean triplet found for a + b + c = 1000.")


