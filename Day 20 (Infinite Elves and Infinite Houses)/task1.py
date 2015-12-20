from collections import defaultdict


puzzle_input = 34000000
houses = defaultdict(lambda: 0)

for elf_power in xrange(1, puzzle_input):
    for house in xrange(elf_power, puzzle_input / 10, elf_power):  # Step fast than 1 by 1
        houses[house] += 10 * elf_power

    if houses[elf_power] >= puzzle_input:
        print elf_power
        break
