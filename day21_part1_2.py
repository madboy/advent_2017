"""
How many pixels stay on after 5 iterations?

A bit slow for the second part, so there should be a way to do this without storing all of it.
"""
import fileinput

def rotate(pattern: list) -> list:
    size = len(pattern[0])
    npattern = []
    for row in range(size): npattern += [[0]*size]
    for r in range(0, size):
        for c in range(0, size):
            npattern[r][c] = pattern[size - c - 1][r]
    return npattern


def transpose(pattern: list) -> list:
    return [list(i) for i in zip(*pattern)]


def find_transformation(square: list, transformations: list) -> list:
    c = compact_form(square)
    return transformations[c]


# this could probably be cleaned up a bit
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

def merge_transformations(transformations, new_size) -> list:
    ssize = len(transformations[0])
    sside = int(new_size/ssize)
    # create list to hold all the merged transformed squares
    merged = []
    for row in range(new_size): merged += [[0]*new_size] 

    # go through each square and add all the items from that square to the merged pattern
    # as we change square we need to change which part of the merged pattern we are filling
    for sq, square in enumerate(transformations):
        for s, square_row in enumerate(square):
            for ss, row in enumerate(square_row):
                r  = s + int(sq/sside)*ssize
                c = ss + (sq%sside)*ssize
                merged[r][c] = row                
    return merged

inputs = fileinput.input()
transformations = dict()

# as we read the input go through possible variations of the pattern
# and store those as well
for line in inputs:
    before, after = line.strip().split(" => ")
    epattern = expanded_form(before)
    for i in range(0, 4):
        npattern = rotate(epattern)
        transformations[compact_form(npattern)] = after
        transformations[compact_form(transpose(npattern))] = after
        epattern = npattern

start_pattern = [
    [".", "#", "."],
    [".", ".", "#"],
    ["#", "#", "#"],
]

pattern = start_pattern
# for i in range(0, 18): # part 2
for i in range(0, 5):
    size = len(pattern[0])
    trans = []
    if size%2 == 0: # break into 2x2 squares
        square_size = 2
        transformed_size = 3
    elif size%3 == 0: # break into 3x3 squares
        square_size  = 3        
        transformed_size = 4        
    else:
        print("error, invalid pattern size")

    new_size = transformed_size * int(size/square_size)
    squares = break_into_squares(square_size, pattern, size)
    for square in squares:
        trans.append(expanded_form(find_transformation(square, transformations)))
    pattern = merge_transformations(trans, new_size)

count = 0
for p in pattern:
    count += p.count("#") # check which pixels are still on
print(count)
