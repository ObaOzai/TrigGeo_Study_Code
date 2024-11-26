#quadratic.py
#Oba Ozai Nov 2024

'''
basic quadratic formula 
x = 1/2a(-b +/- square_root(b^2 - 4ac) 
'''

import math

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No Real Roots"
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1, root2

# Usage
print(quadratic_formula(1, -3, 2))  # Output: (2.0, 1.0)
