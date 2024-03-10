"""
Task:

- Ask the user to enter their age.
- Convert their input into an integer.
- Check if the user's age is 18 or older.
Print a message indicating whether they are old enough to vote:
- If they are old enough: "You are eligible to vote."
- If they are not old enough: "You are not yet eligible to vote."

Explanation:  This exercise combines user input, type conversion, comparison operators, and Boolean logic.
"""

age_str = input("Please enter you age: ")
age = int(age_str)

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not yet eligible to vote.")
