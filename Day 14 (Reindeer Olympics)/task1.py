import re

stats = [line.rstrip("\n") for line in open("input.txt", "r")]
distances = list()
time_limit = 2503

for stat in stats:
    reindeer, speed, duration, sleep = re.findall(r"[A-Z][a-z]+|\d+", stat)
    speed, duration, sleep = map(int, [speed, duration, sleep])

    # Number of full bursts + possible mid burst
    distance = speed * (time_limit / (duration + sleep) * duration + min(duration, time_limit % (duration + sleep)))
    distances.append(distance)

print max(distances)
