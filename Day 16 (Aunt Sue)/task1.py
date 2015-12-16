import re

result_set = frozenset([("children", 3), ("cats", 7), ("samoyeds", 2), ("pomeranians", 3), ("akitas", 0),
                        ("vizslas", 0), ("goldfish", 5), ("trees", 3), ("cars", 2), ("perfumes", 1)])
result_names = [k for k, v in result_set]
sues = [line.rstrip("\n") for line in open("input.txt", "r")]

results = list()

for i, sue in enumerate(sues):

    stats = [prop.split(": ") for prop in re.findall(r"[a-z]*: \d+", sue)]
    stats_names = (n for n, _ in stats)
    stats.extend([(n, 0) for n in result_names if n not in stats_names])  # Add missing properties, with value 0

    sue_data = frozenset([(k, int(v)) for k, v in stats])
    matching_len = len(result_set.intersection(sue_data))
    results.append(("Sue {}".format(i + 1), matching_len))

print max(results, key=lambda s: s[1])
