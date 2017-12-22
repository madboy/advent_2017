"""
How many pixels stay on after 5 iterations?
"""
import fileinput


def find_transformation(square: list, transformations: list) -> list:
    c = compact_form(square)
    return transformations[c]


def break_into_squares(square_size: int, pattern: list, size: int) -> list:
    nsquares = int(size/square_size)**2
    squares = []
    start_row = 0
    layer = 0
    cols = 0
    for s in range(0, nsquares):
        square = []
        for row in range(square_size): square += [[0]*square_size]
        if cols >= size:
            layer += 1
            cols = 0
        for ridx, r in enumerate(range(0+square_size*layer, square_size*layer+square_size)):
            for cidx, c in enumerate(range(cols, cols+square_size)):
                square[ridx][cidx] = pattern[r][c]
        cols += square_size
        squares.append(square)
    return squares


def compact_form(square: list) -> str:
    rows = []
    for row in square:
        rows.append("".join(row))
    return "/".join(rows)


def expanded_form(square: str) -> list:
    expanded = []
    rows = square.split("/")
    for row in rows:
        expanded.append(list(row))
    return expanded


def apply_transformations(new_size: int, trans: list, transformed_size: int):
    new_pattern = []
    for row in range(new_size): new_pattern += [[0]*new_size]
    layer = 0
    cols = 0
    for i, transformation in enumerate(trans):
        ft = expanded_form(transformation)
        cols += len(ft[0])
        if cols > new_size:
            layer += 1
            cols = 0
            # print("move down one layer")
        for r, row in enumerate(ft):
            for c, col in enumerate(row):
                new_pattern[r+layer][c+i*transformed_size] = col
    return new_pattern


inputs = [
    "../.# => ##./#../...",
    ".#./..#/### => #..#/..../..../#..#",
]

# inputs = fileinput.input()

transformations = {}
for line in inputs:
    before, after = line.strip().split(" => ")
    transformations[before] = after

start_pattern = """
.#.
..#
###"""

start_pattern = [
    [".", "#", "."],
    [".", ".", "#"],
    ["#", "#", "#"],
]

# process
#If the size is evenly divisible by 2, break the pixels up into 2x2 squares, and convert each 2x2 square into a 3x3 square by following the corresponding enhancement rule.
#
# Otherwise, the size is evenly divisible by 3; break the pixels up into 3x3 squares, and convert each 3x3 square into a 4x4 square by following the corresponding enhancement rule.

pattern = start_pattern

for i in range(0, 2):
    size = len(pattern[0])
    trans = []
    if size%2 == 0:
        square_size = 2
        transformed_size = 3
        new_size = int((size+1) * (size/square_size))
        squares = break_into_squares(square_size, pattern, size)
        print("break into 2x2 squares")
        print(squares)
        for square in squares:
            trans.append(find_transformation(square, transformations))
        pattern = apply_transformations(new_size, trans, transformed_size)        
    elif size%3 == 0:
        new_size = int((size+1) * (size/3))
        transformed_size = 4
        print("break into 3x3 squares", new_size)
        squares = break_into_squares(3, pattern, size)
        for square in squares:
            trans.append(find_transformation(square, transformations))
        pattern = apply_transformations(new_size, trans, transformed_size)
    else:
        print("error, invalid pattern size")
    print(pattern)
