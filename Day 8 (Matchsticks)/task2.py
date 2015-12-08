import re

words = [line.rstrip("\n") for line in open("input.txt", "r")]

escaped = 0
unescaped = 0

for word in words:

    unescaped += len(word)
    escaped_word = "\"" + re.escape(word) + "\""  # Escape word and add quotes
    escaped += len(escaped_word)

print escaped - unescaped
