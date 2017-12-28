"""
The spreadsheet consists of rows of apparently-random numbers.
To make sure the recovery process is on the right track, they need you 
to calculate the spreadsheet's checksum. 
For each row, determine the difference between the largest value 
and the smallest value; the checksum is the sum of all of these differences.

What is the checksum for the spreadsheet in your puzzle input?
"""
import fileinput


def checksum(rows):
    check = []
    for row in rows:
        numbers = list(map(int, row.split("\t")))
        check.append(max(numbers) - min(numbers))
    return sum(check)


rows = []
for line in fileinput.input():
    row = line.strip()
    rows.append(row)

print(checksum(rows))
