commands = open("input.txt", "r").readline()

current_floor = 0
for index, command in enumerate(commands):

    if command == "(":
        current_floor += 1
    else:
        current_floor -= 1

    if current_floor == -1:
        print index + 1
        break
