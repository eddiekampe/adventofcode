commands = open("input.txt", "r").readline()
total, up = len(commands), commands.count("(")
result = up - (total - up)

print result
