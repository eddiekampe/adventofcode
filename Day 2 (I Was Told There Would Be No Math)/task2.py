presents = [line.rstrip("\n") for line in open("input.txt", "r")]

total_feet_ribbon = 0
for present in presents:
    # Formula 2lw + 2wh + 2hl + min(lw, wh, hl)
    l, w, h = map(lambda _: int(_), present.split("x"))
    dimensions = [l, w, h]
    dimensions.remove(max(dimensions))

    ribbon_needed = sum(map(lambda size: 2 * size, dimensions)) + l*w*h
    total_feet_ribbon += ribbon_needed

print total_feet_ribbon
