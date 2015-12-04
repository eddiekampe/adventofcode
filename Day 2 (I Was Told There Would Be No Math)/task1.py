presents = [line.rstrip("\n") for line in open("input.txt", "r")]

total_feet_wrapper = 0
for present in presents:
    # Formula 2lw + 2wh + 2hl + min(lw, wh, hl)
    l, w, h = map(lambda _: int(_), present.split("x"))
    sides = [l*w, w*h, h*l]

    wrapper_needed = sum(map(lambda side: 2 * side, sides)) + min(sides)
    total_feet_wrapper += wrapper_needed

print total_feet_wrapper
