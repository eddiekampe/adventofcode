import re


def read_ingredients(filename):

    ingredient_data = dict()
    ingredients = [line.rstrip("\n") for line in open(filename, "r")]

    for ingredient in ingredients:
        name, capacity, durability, flavor, texture, calories = re.findall(r"[A-Z][a-z]+|[-]?\d+", ingredient)
        ingredient_data[name] = (int(capacity), int(durability), int(flavor), int(texture), int(calories))

    return ingredient_data


def calculate_score(mix, stats):

    c, d, f, t, cal = (0, 0, 0, 0, 0)
    for ingredient, scoops in mix.items():
        c1, d1, f1, t1, cal1 = stats[ingredient]
        c, d, f, t, cal = c + c1 * scoops, d + d1 * scoops, f + f1 * scoops, t + t1 * scoops, cal + cal1 * scoops

    if cal != 500:
        return -1  # Too unhealthy (but mom it's christmas...)

    return max(0, c) * max(0, d) * max(0, f) * max(0, t)


if __name__ == "__main__":

    ingredient_stats = read_ingredients("input.txt")
    names = ingredient_stats.keys()
    options = (
        # Assume we work with exactly 4 ingredients
        {names[0]: i1, names[1]: i2, names[2]: i3, names[3]: i4}
        for i1 in xrange(101)
        for i2 in xrange(101 - i1)
        for i3 in xrange(101 - i1 - i2)
        for i4 in xrange(101 - i1 - i2 - i3)
        if i1 + i2 + i3 + i4 == 100
    )
    # Brute force for now...
    print max(calculate_score(option, ingredient_stats) for option in options)
