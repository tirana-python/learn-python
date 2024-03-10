"""
Task:

- Ask the user if they like ice cream (input of "yes" or "no").
Store their answer in a variable.
Use an if/else statement to print a message based on their answer:
- If they like ice cream, print "Great choice! Ice cream is delicious."
- If they don't like ice cream, print "That's okay, there are other tasty treats."

Explanation: Conditional statements (if/else) allow your code to make decisions based on Boolean values.
"""

likes_ice_cream = input("Do you like ice cream? (yes/no): ")

if likes_ice_cream.lower() == "yes":
    print("Great choice! Ice cream is delicious.")
else:
    print("That's okay, there are other tasty treats.")

