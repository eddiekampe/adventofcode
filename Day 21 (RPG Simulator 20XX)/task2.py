import re

monster_data = "".join(open("input.txt", "r").readlines())

weapons = {"Dagger": (8, 4, 0), "Shortsword": (10, 5, 0), "Warhammer": (25, 6, 0), "Longsword": (40, 7, 0),
           "Greataxe": (74, 8, 0)}
armor = {"Nothing": (0, 0, 0), "Leather": (13, 0, 1), "Chainmail": (31, 0, 2), "Splintmail": (53, 0, 3),
         "Bandedmail": (75, 0, 4), "Platemail": (102, 0, 5)}
rings = {"Nothing 1": (0, 0, 0), "Nothing 2": (0, 0, 0), "Damage +1": (25, 1, 0), "Damage +2": (50, 2, 0),
         "Damage +3": (100, 3, 0), "Defense +1": (20, 0, 1), "Defense +2": (40, 0, 2), "Defense +3": (80, 0, 3)}


def battle(items):

    boss_hp, boss_dmg, boss_armor = map(int, re.findall(r"\d+", monster_data))
    player_hp, player_dmg, player_armor = 100, 0, 0  # Start stats

    for item in items:
        player_dmg += item[1]
        player_armor += item[2]

    turn = 0
    while player_hp > 0 and boss_hp > 0:

        if turn % 2 == 0:  # Player starts
            damage_after_mitigation = boss_armor - player_dmg
            boss_hp -= 1 if damage_after_mitigation > 1 else abs(damage_after_mitigation)
        else:
            damage_after_mitigation = player_armor - boss_dmg
            player_hp -= 1 if damage_after_mitigation > 1 else abs(damage_after_mitigation)

        turn += 1

    return player_hp > boss_hp

ring_values = rings.values()
lose_costs = list()

for weapon_stats in weapons.itervalues():
    for armor_stats in armor.itervalues():

        for ring1, ring2 in [(ring_values[i], ring_values[j]) for i in xrange(len(rings)) for j in xrange(i + 1, len(rings))]:

            player_items = [weapon_stats, armor_stats, ring1, ring2]
            player_won = battle(player_items)
            if not player_won:
                lose_costs.append(sum([c for c, _d, _a in player_items]))

print max(lose_costs)
