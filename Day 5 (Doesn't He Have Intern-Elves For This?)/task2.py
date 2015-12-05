words = [line.rstrip("\n") for line in open("input.txt", "r")]

result = 0
for word in words:

    double_occurrence_found = False
    has_letter_between_found = False

    for index, character in enumerate(word):

        if index > 1 and not double_occurrence_found and word.count("{}{}".format(word[index - 1], character)) >= 2:
            double_occurrence_found = True

        if index > 2 and not has_letter_between_found and character == word[index - 2]:
            has_letter_between_found = True

        if double_occurrence_found and has_letter_between_found:
            result += 1
            break

print result
