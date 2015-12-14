import re
import itertools
from collections import defaultdict

opinions = [line.rstrip("\n") for line in open("input.txt", "r")]
affections = defaultdict(int)
seating_alternatives = list()
persons = set()
persons.add("random_dude")

# Generate affection dict
for opinion in opinions:
    person_a, operation, happiness, person_b = re.findall(r"[A-Z][a-z]+|gain|lose|\d+", opinion)
    persons.update([person_a, person_b])

    affections[(person_a, person_b)] = int(happiness) if operation == "gain" else -int(happiness)

# Go through all possible placements
for seating in list(itertools.permutations(persons)):

    pairs = [(person_a, seating[i + 1]) for i, person_a in enumerate(seating) if i < len(seating) - 1]
    pairs_reversed = [(seating[i + 1], person_a) for i, person_a in enumerate(seating) if i < len(seating) - 1]
    pairs.extend(pairs_reversed)

    first, last = seating[0], seating[-1]

    happiness = sum(affections[pair] for pair in pairs)
    happiness += affections[(first, last)] + affections[(last, first)]  # Fake circular table

    seating_alternatives.append(happiness)

print max(seating_alternatives)
