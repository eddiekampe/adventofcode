import itertools

containers = map(int, [line.rstrip("\n") for line in open("input.txt", "r")])
eggnog_liters = 150
result = 0

for i in xrange(1, len(containers) + 1):
    result += len([c for c in itertools.combinations(containers, i) if sum(c) == eggnog_liters])

print result
