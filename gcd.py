#gcd.py
#Oba Ozai Nov 2024
'''
Greatest Common Divisor (GCD)
Formula:
gcd(a,b)=gcd(b,amodb),where gcd(a,0)=a
'''

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Usage
print(gcd(48, 18))  # Output: 6
