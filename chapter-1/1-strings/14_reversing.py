"""
Task:

- Reverse the order of the characters in your full_name string (from previous exercises).
- Print the reversed name.

Explanation: Strings can be manipulated to rearrange their characters.
"""

first_name = "Max"
last_name = "Mara"

full_name = f"{first_name} {last_name}"

reversed_name = ''.join(reversed(full_name))
print(reversed_name)

# Another way of doing it
print(full_name[::-1])
