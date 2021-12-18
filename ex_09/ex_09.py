fname = input("Enter file name: ")

while True:
    if 1 > len(fname):
        fname = "mbox-short.txt"
        break
    elif "mbox-short.txt" != fname:
        fname = input("Wrong file, try again :")
    else:
        break
fhand = open(fname)

count = {}
for lines in fhand:
    lines = lines.rstrip()
    words = lines.split()
    for word in words:
        # idiom: retrieve/create/update counter
        count[word] = count.get(word, 0) + 1

largest_word = None
nb_times = -1
for key, val in count.items():
    if nb_times < val:
        nb_times = val
        largest_word = key  # capture/remember largest key

print("The word reptaly the most is : ", largest_word, " ", nb_times, " times")
