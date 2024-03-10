"""
Task:

- Ask the user to enter a paragraph of text.
Do the following:
- Count how many sentences are in the paragraph. (You can assume that a sentence ends with a period.)
- Count how many times the word "the" appears (case-insensitive).
- Print the results of your analysis.

Explanation: This combines several string concepts and requires a bit more independent thinking.
"""

paragraph = input("Please enter a paragraph of text: ")

if paragraph.endswith("."):
    num_sentences = paragraph.count(".")
else:
    num_sentences = paragraph.count(".") + 1  # Add 1 for the last sentence not containing a '.'

# Count the word "the" (case-insensitive)
num_the = paragraph.lower().count("the")

# Print the results
print("Analysis of your paragraph:")
print(f"Number of sentences: {num_sentences}")
print(f"Number of occurrences of 'the': {num_the}")
