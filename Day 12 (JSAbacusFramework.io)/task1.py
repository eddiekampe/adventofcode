import re

text_object = open("input.txt", "r").readline()
print sum(map(int, re.findall(r"[-]?\d+", text_object)))
