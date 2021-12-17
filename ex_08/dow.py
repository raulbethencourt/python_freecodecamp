fhand = open("mbox-short.txt")

for line in fhand:
    line = line.rstrip()
    wds = line.split()
    print('Words')
    if wds[0] != "From":
        continue
    print(wds[2])
