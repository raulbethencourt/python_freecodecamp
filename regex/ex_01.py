import re

fhand = open("mbox-short.txt")

hosts = []
for lines in fhand:
    hosts.append(re.findall("^From .*@([^ ]*)", lines))

for host in hosts:
    if host:
        print(host)
