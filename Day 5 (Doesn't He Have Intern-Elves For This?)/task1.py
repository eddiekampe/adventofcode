words = [line.rstrip("\n") for line in open("input.txt", "r")]

vowels = "aeiou"
bad_words = ["ab", "cd", "pq", "xy"]
result = 0

for word in words:

    vowels_found = 0
    has_double_letter = False

    if any(bad_word in word for bad_word in bad_words):
        continue  # Process next word

    for index, character in enumerate(word):

        if character in vowels:
            vowels_found += 1
        if index > 0 and character == word[index - 1]:
            has_double_letter = True

    if has_double_letter and vowels_found >= 3:
        result += 1

print result
