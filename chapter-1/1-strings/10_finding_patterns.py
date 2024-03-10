"""
Task:

- Check if your 'sentence' variable starts with the word "Welcome".
- Check if your 'sentence' variable ends with the word "Pyrana".
- Print "True" for each match and "False" otherwise.

Explanation: We'll use methods to find patterns at the beginning and end of strings.
"""

sentence = "Welcome to the beginning of learning Python by Pyrana"

if sentence.startswith("Welcome"):
    print("True")
else:
    print("False")


if sentence.endswith("Pyrana"):
    print("True")
else:
    print("False")
