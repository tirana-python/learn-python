"""
Task:

Ask the user to enter a number.
Check the following conditions:
Is the number positive?
Is the number even?
Print a message describing the number:
"The number is positive and even."
"The number is positive and odd."
"The number is neither positive nor even." (this would be for 0)
"The number is negative and even."
"The number is negative and odd."
Explanation: This exercise introduces combining multiple Boolean conditions using logical operators (and, or).
"""

number_str = input("Enter a number: ")
number = int(number_str)

is_positive = number > 0
is_even = number % 2 == 0

if is_positive and is_even:
    print("The number is positive and even.")
elif is_positive and not is_even:
    print("The number is positive and odd.")
elif not is_positive and not is_even:
    print("The number is neither positive nor even.")
elif not is_positive and is_even:
    print("The number is negative and even.")
else:
    print("The number is negative and odd.")
