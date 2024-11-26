#series_sum.py
#Oba Ozai Nov 2024

'''

Sum of an Arithmetic Series
S(sub n) = n/2 x (a x l) 
'''

def sum_arithmetic_series(a, l, n):
    return (n / 2) * (a + l)

# Usage
print(sum_arithmetic_series(1, 10, 10))  # Output: 55
