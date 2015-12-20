import re
from collections import OrderedDict

molecule = open("molecule.txt", "r").readline()
replacements = [line.rstrip("\n") for line in open("input.txt", "r")]
translations = OrderedDict()

# Read input
for replacement in replacements:
    before, after = replacement.split(" => ")
    translations[after] = before


def explore(current_molecule, depth=0):

    if current_molecule == "e":
        yield depth

    depth += 1

    for t in translations.iterkeys():
        for match in re.finditer(t, current_molecule):

            new_molecule = current_molecule[0: match.start()] + translations[t] + current_molecule[match.end():]
            for m in explore(new_molecule, depth):
                yield m


print next(explore(molecule))
