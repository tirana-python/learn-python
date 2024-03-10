"""
Task:

- Create variables to store the following numbers: 10, 5, and 2.5.
- Perform the following calculations and print the result for each:
- Addition (10 + 5)
- Subtraction (10 - 2.5)
- Multiplication (5 * 2.5)
- Division (10 / 5)

Explanation: This introduces fundamental arithmetic operations in Python.
"""

x = 10
y = 5
z = 2.5

addition = x + y
print(addition)

subtraction = x - z
print(subtraction)

multiplication = y * z
print(multiplication)

division = x / y
print(division)

"""
***Additional***

Understanding Integer vs. Float Behavior

 - Addition: When you add an integer (x) and a float (z), the result is automatically converted to a float (15.0) to 
    accommodate the decimal portion.
 - Subtraction: Similarly, subtracting a float from an integer results in a float (7.5).
 - Multiplication: Multiplying an integer and a float also produces a float (12.5).
 - Division: Division in Python generally produces a float, even if the result would otherwise seem like a 
    whole number (2.0).

Important Note: If you want integer division (which discards the remainder), you'll need to use the // operator.
Let's try that!
"""