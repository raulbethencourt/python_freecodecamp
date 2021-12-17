str = "X-DSPAM-Confidence: 0.8475 "

ipos = str.find(" : ")
# print(ipos)
piece = str[ipos + 1:]
# print(piece)
# print(piece+42) # will fail
value = float(piece)
print(value)
# print(value + 42.0)
