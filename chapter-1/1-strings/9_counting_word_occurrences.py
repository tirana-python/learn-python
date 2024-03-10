"""
Task:

- Count how many times the word "the" appears in your 'sentence' variable (case-insensitive).
- Print the count.

Explanation: Sometimes you might want to analyze how often certain words appear in a text.
"""

sentence = "Welcome to the beginning of learning Python by Pyrana"
count = 0
for word in sentence.split(" "):
    if word.lower() == "the":
        count += 1

print(count)

# Another way of doing it with chaining
occurrence_count = sentence.lower().split().count("the")
print(occurrence_count)
