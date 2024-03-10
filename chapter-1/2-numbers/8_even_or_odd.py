"""
Task:

- Ask the user to enter a number.
- Use the modulo operator to determine if the number is even or odd.
- Print the result (e.g., "The number is even" or "The number is odd").

Explanation: An even number is always divisible by 2, leaving a remainder of 0. We can use the modulo operator to check for this.
"""

user_input = input("Please enter a number: ")
number = int(user_input)

if number % 2 == 0:
    print(f"The number: {number} is even")
else:
    print(f"The number: {number} is odd")
