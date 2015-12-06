from collections import defaultdict

commands = [line.rstrip("\n") for line in open("input.txt", "r")]
light_grid = defaultdict(int)

for command in commands:

    if command.startswith("toggle"):
        _, start, _, end = command.split(" ")
        increase = 2
    else:
        _, switch, start, _, end = command.split(" ")
        if switch == "on":
            increase = 1
        else:
            increase = -1

    start_x, start_y = [int(val) for val in start.split(",")]
    end_x, end_y = [int(val) for val in end.split(",")]

    for x_index in xrange(start_x, end_x + 1):
        for y_index in xrange(start_y, end_y + 1):
            light_grid[(x_index, y_index)] += increase
            if light_grid[(x_index, y_index)] < 0:
                light_grid[(x_index, y_index)] = 0

print sum(light_grid.values())
