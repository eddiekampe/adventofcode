from collections import defaultdict

commands = open("input.txt", "r").readline()

santa_pos = robot_pos = (0, 0)
result = defaultdict(int)
result[santa_pos] += 1  # Make sure to count start spot


def update_pos(command, pos):

    if command == "^":
        pos = (pos[0], pos[1] + 1)
    elif command == "v":
        pos = (pos[0], pos[1] - 1)
    elif command == ">":
        pos = (pos[0] + 1, pos[1])
    elif command == "<":
        pos = (pos[0] - 1, pos[1])

    return pos


for index, c in enumerate(commands):

    if index % 2 == 0:
        santa_pos = position = update_pos(c, santa_pos)
    else:
        robot_pos = position = update_pos(c, robot_pos)

    result[position] += 1

print len(result)
