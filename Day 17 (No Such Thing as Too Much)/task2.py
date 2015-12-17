import itertools

containers = map(int, [line.rstrip("\n") for line in open("input.txt", "r")])
eggnog_liters = 150
result = list()

for i in xrange(1, len(containers) + 1):
    result.append(len([c for c in itertools.combinations(containers, i) if sum(c) == eggnog_liters]))

print [r for r in result if r > 0][0]
