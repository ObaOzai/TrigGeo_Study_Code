#prime.py
#Oba Ozai Nov 2024

'''
Prime Checking
Algorithm:
A number 
n is prime if it is greater than 1 and divisible only by 1 and itself.
'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Usage
print(is_prime(29))  # Output: True
