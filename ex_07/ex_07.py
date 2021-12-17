fhand = open("mbox-short.txt")

for line in fhand:
    line = line.rstrip()
    print(line.upper())
