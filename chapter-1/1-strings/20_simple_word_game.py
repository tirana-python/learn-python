"""
Task:

- Ask the user to enter a word.
- Check if the word reads the same backward as forward (i.e., if it's a palindrome).
- Print "Yes, it's a palindrome" if it is, and "No, it's not a palindrome" if it isn't.

Explanation: We'll use string slicing and comparisons.
"""

word = input("Please enter a word: ")

if word == word[::-1]:
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome")
