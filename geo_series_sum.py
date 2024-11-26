#geo_series_sum.py
#Oba Ozai Nov 2024

'''
check series sum formula
'''

def sum_geometric_series(a, r, n):
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)

# Usage
print(sum_geometric_series(1, 2, 4))  # Output: 15.0
