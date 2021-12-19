import re

fhand = open("mbox-short.txt")

costs = []
for line in fhand:
    costs.append(re.findall("\$[0-9.]+", line))

for cost in costs:
    if cost:
        print(cost)
