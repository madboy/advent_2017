import fileinput

def checksum(row):
    numbers = row.split("\t")
    low, high = 1000000000, 0
    for number in numbers:
        n = int(number)
        if low > n:
            low = n
        if high < n:
            high = n
    return high - low

total = 0
for line in fileinput.input():
    row = line.strip()
    total += checksum(row)

print(total)
