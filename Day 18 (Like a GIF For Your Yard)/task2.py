from collections import defaultdict


def generate_initial_grid(grid_data):

    grid = defaultdict(bool)
    for y in xrange(len(grid_data)):  # Construction of grid
        for index, x in enumerate(grid_data[y]):
            grid[(y, index)] = x == "#"
    return grid


def neighbors_on(x, y, grid):
    statuses = [grid[a, b] for a in xrange(x - 1, x + 2) for b in xrange(y - 1, y + 2) if (a, b) != (x, y)]
    return len([s for s in statuses if s])


def run(grid):

    grid[0, 0] = grid[0, 99] = grid[99, 0] = grid[99, 99] = True
    new_grid = defaultdict(bool)
    for y in xrange(0, 100):
        for x in xrange(0, 100):

            nr_neighbors_on = neighbors_on(x, y, grid)
            if grid[(x, y)] and (nr_neighbors_on in [2, 3]):  # On and 2 or 3 neighbors are on
                new_grid[(x, y)] = grid[(x, y)]
            elif not grid[(x, y)] and nr_neighbors_on == 3:  # Off and 3 neighbors are on
                new_grid[(x, y)] = True
            else:
                new_grid[(x, y)] = False

    new_grid[0, 0] = new_grid[0, 99] = new_grid[99, 0] = new_grid[99, 99] = True
    return new_grid


if __name__ == "__main__":

    grid_input = [line.rstrip("\n") for line in open("input.txt", "r")]
    light_grid = generate_initial_grid(grid_input)

    for _ in xrange(0, 100):
        light_grid = run(light_grid)

    print len([status for status in light_grid.values() if status])
