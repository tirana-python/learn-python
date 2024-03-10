"""
Task:

- Ask the user to enter a number (this input will be a string).
- Convert the user's input into an integer and a floating-point number.
- Print both the converted integer and the converted float.

Explanation:  This exercise will test your understanding of type conversion in Python.
"""

number = input("Enter a number: ")

number_in_float = float(number)
number_in_int = int(number_in_float)

print(f"Number in integer: {number_in_int}")
print(f"Number in float: {number_in_float}")
