#lcm.py
#Oba Ozai Nov 2024


'''
Least Common Multiple (LCM)
Formula:
lcm(a,b)= gcd(a,b) ∣a×b∣
'''

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    from math import gcd
    return abs(a * b) // gcd(a, b)

# Usage
print("LCM = ",lcm(12, 15))  # Output: 60

​	
 
