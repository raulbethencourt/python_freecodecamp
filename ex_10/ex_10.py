fhand = open("mbox-short.txt")

dict = {}
for lines in fhand:
    words = lines.split()
    for word in words:
        if word.isalpha():
            dict[word] = dict.get(word, 0) + 1

sorted_list = sorted([(val, key) for key, val in dict.items()], reverse=True)

for val, key in sorted_list[:10]:
    print(key, val)
