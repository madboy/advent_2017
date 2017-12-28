"""
It sounds like the goal is to find the only two numbers in each row 
where one evenly divides the other - that is, where the result of the 
division operation is a whole number.

They would like you to find those numbers on each line, divide them, and add up each line's result.
"""
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
