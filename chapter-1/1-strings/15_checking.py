"""
Task:

- Create a variable called website and assign it a website address (e.g., "www.google.com").
- Check if the website address starts with "http://". Print "True" if it does, "False" otherwise.
- Check if the website address ends with ".com". Print "True" if it does, "False" otherwise.

Explanation: We'll practice checking for specific conditions within strings.
"""

website = "https://pyrana.org"

if website.startswith("https://"):
    print("True")
else:
    print("False")

if website.endswith(".org"):
    print("True")
else:
    print("False")
