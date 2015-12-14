import re
from collections import defaultdict

reindeer_stats = [line.rstrip("\n") for line in open("input.txt", "r")]
reindeer_data = dict()
time_limit = 2503

for stats in reindeer_stats:
    reindeer, speed, duration, sleep = re.findall(r"[A-Z][a-z]+|\d+", stats)
    reindeer_data[reindeer] = map(int, [speed, duration, sleep])  # Save stats for later

distances, scores = defaultdict(int), defaultdict(int)

for second in xrange(0, time_limit):

    for reindeer, stats in reindeer_data.items():
        speed, duration, sleep = stats

        if second % (duration + sleep) < duration:  # Update distance if active
            distances[reindeer] += speed

    leader_distance = max(distances.values())
    leaders = (reindeer for reindeer, distance in distances.items() if distance >= leader_distance)
    for reindeer in leaders:
        scores[reindeer] += 1

print max(scores.values())
