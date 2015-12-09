from itertools import permutations

distances = [line.rstrip("\n") for line in open("input.txt", "r")]
travel_costs = dict()
cities = set()

for distance in distances:

    city_from, _, city_to, _, cost = distance.split(" ")
    travel_costs[(city_from, city_to)] = int(cost)
    travel_costs[(city_to, city_from)] = int(cost)
    cities.update([city_from, city_to])

longest = 0

for permutation in permutations(cities):

    p = list(permutation)
    costs = sum(travel_costs[(p[i - 1], p[i])] for i, _ in enumerate(permutation) if i > 0)

    if costs > longest:
        longest = costs

print longest
