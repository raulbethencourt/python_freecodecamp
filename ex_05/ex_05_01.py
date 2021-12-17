sum = 0
count = 0

while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    try:
        sum += float(number)
        count += 1
except:
        print("Invalid input")
        continue

print(sum, count, sum / count)
