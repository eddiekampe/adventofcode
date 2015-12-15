import re
from copy import copy


def read_ingredients(filename):

    ingredient_data = dict()
    ingredients = [line.rstrip("\n") for line in open(filename, "r")]

    for ingredient in ingredients:
        name, capacity, durability, flavor, texture, _ = re.findall(r"[A-Z][a-z]+|[-]?\d+", ingredient)
        ingredient_data[name] = (int(capacity), int(durability), int(flavor), int(texture))

    return ingredient_data


def test_bake(mix, ingredient, stats):

    test_mix = copy(mix)
    test_mix[ingredient] += 1
    return calculate_score(test_mix, stats)


def calculate_score(mix, stats):

    c, d, f, t = (0, 0, 0, 0)
    for ingredient, scoops in mix.items():
        c1, d1, f1, t1 = stats[ingredient]
        c, d, f, t = c + c1 * scoops, d + d1 * scoops, f + f1 * scoops, t + t1 * scoops

    return max(0, c) * max(0, d) * max(0, f) * max(0, t)


def optimize_recipe(stats, max_spoons):

    mixture = dict()
    current_teaspoons = 4
    # Lets start with one of each ingredient
    for ingredient in stats.keys():
        mixture[ingredient] = 1

    while current_teaspoons < max_spoons:

        mixes = ((ingredient, test_bake(mixture, ingredient, stats)) for ingredient in stats.keys())
        ingredient, score = max(mixes, key=lambda m: m[1])  # m[1] = score
        mixture[ingredient] += 1
        current_teaspoons += 1

    return mixture


if __name__ == "__main__":

    ingredient_stats = read_ingredients("input.txt")
    optimal_recipe = optimize_recipe(stats=ingredient_stats, max_spoons=100)
    print optimal_recipe, "yields", calculate_score(optimal_recipe, ingredient_stats)
