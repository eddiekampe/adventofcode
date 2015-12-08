import re

words = [line.rstrip("\n") for line in open("input.txt", "r")]

parsed = 0
unparsed = 0

for word in words:

    unparsed += len(word)

    word = word[1:-1]  # Remove quotes from string
    word = re.sub(r"\\\"", " ", word)  # Replace \" with 1 character
    word = re.sub(r"\\\\", " ", word)  # Replace \\ with 1 character
    word = re.sub(r"\\x.{2}", " ", word)  # Replace hex representations from

    parsed += len(word)

print unparsed - parsed
