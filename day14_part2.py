"""
Treating your puzzle input as a string of ASCII characters, what is the Knot Hash of your puzzle input? Ignore any leading or trailing whitespace you might encounter.
"""
from collections import namedtuple, deque
from day10_part2 import create_dense_hash

Square = namedtuple('Square', ['r', 'c'])

def check_region(sq, squares, alls):
    neighbours = [
        Square(sq.r + 1, sq.c),
        Square(sq.r - 1, sq.c),
        Square(sq.r, sq.c + 1),
        Square(sq.r, sq.c - 1),
    ]

    region = []
    for n in neighbours:
        if squares.get(n, 0) == "1":
            try:
                alls.remove(n)
                region.append(n)
            except:
                pass
    return region

b = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111",
}


squares = dict()
for row in range(0, 128):
    # salt = "flqrgnkx-" + str(row)
    salt = "hfdlxzhv-" + str(row)

    h = create_dense_hash(salt)
    col = []
    for c in h:
        col.extend(list(b[c]))
    for i in range(0, 128):
        squares[Square(row, i)] = col[i]

all_squares = deque(list(squares.keys()))
nbr_of_regions = 1 # start at one so we can use that as the critteria for if we've marked a square as part of a region already
while all_squares:
    candidate =  all_squares.popleft()
    if squares[candidate] == "1":
        stack = deque([candidate])
        nbr_of_regions += 1
        while stack:
            current = stack.popleft()
            regions = check_region(current, squares, all_squares)
            if regions:
                squares[current] = nbr_of_regions
                stack.extend(regions)

print(nbr_of_regions-1)
