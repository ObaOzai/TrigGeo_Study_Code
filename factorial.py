#factorial.py
#Oba Ozai Nov 2024
'''
n!=n×(n−1)×⋯×1,for n≥1,0!=1
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Usage
print(factorial(5))  # Output: 120

