"""
Task:

Have the program "think" of a secret number (you can hardcode this number for now).
Ask the user to guess the number.
Give the user a hint if their guess is too high or too low.
Let the user keep guessing until they get it right.
Once they guess correctly, congratulate them!

Explanation: This exercise combines concepts like variables, user input, comparison operators, and conditional logic.
"""

from random import randint

number_to_find = randint(1, 10)

guess = int(input("Guess a number from 1 to 10: "))

while guess != number_to_find:
    if guess > number_to_find:
        print(f"Number is lower then {guess}")
    else:
        print(f"Number is higher than {guess}")

    guess = int(input("Guess a number from 1 to 10: "))

print("You got it, congratulation!")
