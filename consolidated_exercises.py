# consolidated_exercises.py
# Oba Ozai 2024
# Description: A collection of Python exercises for arithmetic, geometry, temperature conversions, and more.

# ----------------------------------------------
# 1. Temperature Conversion Functions
# ----------------------------------------------

def fahrenheit_to_celsius(f):
    """
    Convert Fahrenheit to Celsius.
    Formula: (F - 32) * 5/9
    """
    return (f - 32) * 5 / 9

def celsius_to_fahrenheit(c):
    """
    Convert Celsius to Fahrenheit.
    Formula: (C * 9/5) + 32
    """
    return (c * 9 / 5) + 32

def celsius_to_kelvin(c):
    """
    Convert Celsius to Kelvin.
    Formula: C + 273.15
    """
    return c + 273.15

def kelvin_to_celsius(k):
    """
    Convert Kelvin to Celsius.
    Formula: K - 273.15
    """
    return k - 273.15

# Example usage:
# print(fahrenheit_to_celsius(98.6))  # Output: 37.0

# ----------------------------------------------
# 2. Determine Type of Triangle
# ----------------------------------------------

def triangle_type(a, b, c):
    """
    Determine the type of triangle based on its sides.
    Equilateral: All sides equal.
    Isosceles: Two sides equal.
    Scalene: No sides equal.
    """
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# Example usage:
# print(triangle_type(3, 3, 3))  # Output: Equilateral

# ----------------------------------------------
# 3. Calculate the Sum of Numbers from 0 to N
# ----------------------------------------------

def sum_up_to_n(n):
    """
    Calculate the sum of all numbers from 0 to n using a for loop.
    Formula: n * (n + 1) / 2
    """
    return sum(range(n + 1))

# Example usage:
# print(sum_up_to_n(10))  # Output: 55

# ----------------------------------------------
# 4. Print Even Numbers from 0 to N
# ----------------------------------------------

def print_even_numbers(n):
    """
    Print all even numbers from 0 to n using a while loop.
    """
    i = 0
    while i <= n:
        if i % 2 == 0:
            print(i)
        i += 1

# Example usage:
# print_even_numbers(10)

# ----------------------------------------------
# 5. Area of Common Shapes
# ----------------------------------------------

import math

def area_of_circle(radius):
    """
    Calculate the area of a circle.
    Formula: π * r^2
    """
    return math.pi * radius ** 2

def area_of_triangle(base, height):
    """
    Calculate the area of a triangle.
    Formula: 0.5 * base * height
    """
    return 0.5 * base * height

def area_of_polygon(sides, side_length):
    """
    Calculate the area of a regular polygon.
    Formula: (n * s^2) / (4 * tan(π / n))
    """
    return (sides * side_length ** 2) / (4 * math.tan(math.pi / sides))

# Example usage:
# print(area_of_circle(5))  # Output: 78.54
# print(area_of_triangle(10, 5))  # Output: 25.0
# print(area_of_polygon(6, 4))  # Output: 41.57 (Regular Hexagon)

# ----------------------------------------------
# 6. Character Printing from a String
# ----------------------------------------------

def print_characters(s):
    """
    Print each character of a string on a new line using a loop.
    """
    for char in s:
        print(char)

# Example usage:
# print_characters("Hello")

# ----------------------------------------------
# 7. Numpy Array from a List
# ----------------------------------------------

import numpy as np

def list_to_numpy_array(sample_list):
    """
    Convert a Python list to a Numpy array.
    """
    return np.array(sample_list)

# Example usage:
# sample_list = [101, 102, 103, 104]
# print(list_to_numpy_array(sample_list))

# ----------------------------------------------
# 8. Print Multiplication Table for N
# ----------------------------------------------

def print_multiplication_table(n):
    """
    Print the multiplication table for a given number n.
    """
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Example usage:
# print_multiplication_table(5)

# ----------------------------------------------
# End of File
# ----------------------------------------------

#EOF
