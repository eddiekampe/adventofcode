import re
from collections import defaultdict

result_dict = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5,
               "trees": 3, "cars": 2, "perfumes": 1}
result_names = result_dict.keys()
sues = [line.rstrip("\n") for line in open("input.txt", "r")]

results = list()

for i, sue in enumerate(sues):

    stats = [prop.split(": ") for prop in re.findall(r"[a-z]*: \d+", sue)]
    stats = {k: int(v) for k, v in stats}
    sue_data = defaultdict(int, stats)

    matches = list()
    for name in result_names:
        if name in ["cats", "trees"]:  # Check if greater
            matches.append(sue_data[name] > result_dict[name])
        elif name in ["pomeranians", "goldfish"]:  # Check if fewer
            matches.append(sue_data[name] < result_dict[name])
        else:
            matches.append(sue_data[name] == result_dict[name])

    matching_len = len([x for x in matches if x])
    print ("Sue {}".format(i + 1), matching_len)
    results.append(("Sue {}".format(i + 1), matching_len))

_, best_score = max(results, key=lambda s: s[1])
print [sue for sue, score in results if score >= best_score]  # Got multiple results today
