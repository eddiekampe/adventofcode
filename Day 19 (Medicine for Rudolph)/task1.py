import re

molecule = open("molecule.txt", "r").readline()
replacements = [line.rstrip("\n") for line in open("input.txt", "r")]
distinct_molecules = set()

for replacement in replacements:
    before, after = replacement.split(" => ")
    for match in re.finditer(before, molecule):
        new_molecule = molecule[0: match.start()] + after + molecule[match.end():]
        distinct_molecules.add(new_molecule)

print len(distinct_molecules)
