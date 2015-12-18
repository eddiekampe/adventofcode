commands = [line.rstrip("\n") for line in open("input.txt", "r")]

for command in commands:
    print command
