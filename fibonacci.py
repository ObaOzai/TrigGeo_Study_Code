#fibonacci.py
#Oba Ozai Nov. 2024

'''
Fibonacci Sequence
Formula:
F(n)=F(n−1)+F(n−2),F(0)=0,F(1)=1
'''
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Usage
print(fibonacci(10))  # Output: 55


