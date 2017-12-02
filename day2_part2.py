import fileinput

def checksum(row):
    numbers = row.split("\t")
    numbers = list(map(int, numbers))
    numbers.sort()
    for i, number in enumerate(numbers):
        n = int(number)
        for nn in numbers[i+1:]:
            if int(nn)%n == 0:
                return int(nn)/n
    return 0

total = 0
for line in fileinput.input():
    row = line.strip()
    cs = checksum(row)
    assert cs != 0, row
    total += cs

print(total)
