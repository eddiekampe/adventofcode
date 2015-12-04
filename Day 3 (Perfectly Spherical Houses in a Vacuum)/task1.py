from collections import defaultdict

commands = open("input.txt", "r").readline()

cur_pos = (0, 0)
result = defaultdict(int)
result[cur_pos] += 1  # Make sure to count start spot

for command in commands:

    if command == "^":
        cur_pos = (cur_pos[0], cur_pos[1] + 1)
    elif command == "v":
            cur_pos = (cur_pos[0], cur_pos[1] - 1)
    elif command == ">":
            cur_pos = (cur_pos[0] + 1, cur_pos[1])
    elif command == "<":
            cur_pos = (cur_pos[0] - 1, cur_pos[1])

    result[cur_pos] += 1

print len(result)