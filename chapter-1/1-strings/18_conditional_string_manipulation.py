"""
Task:

- Ask the user to enter a word.
- If the length of the word is even, print the word in uppercase.
- If the length of the word is odd, print the word in lowercase.

Explanation: We'll use if/else statements to control how the string is modified based on its properties.
"""

word = input("Please enter e word: ")

if len(word) % 2 == 0:
    print(word.upper())
else:
    print(word.lower())

# Another way of solving it is with the Ternary Operator
# [result_if_true] if [condition] else [result_if_false]

print(word.upper()) if len(word) % 2 == 0 else print(word.lower())
