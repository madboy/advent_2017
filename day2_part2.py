import fileinput


def checksum(row):
    numbers = list(map(int, row.split("\t")))
    for n in numbers:
        for nn in numbers:
            if n> nn and n%nn == 0:
                return n/nn


rows = []
for line in fileinput.input():
    row = line.strip()
    rows.append(row)

print(sum(map(checksum, rows)))
