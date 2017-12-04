"""
How many steps is the data carried?

Spiral layout

37 36  35  34  33  32 31
38 17  16  15  14  13 30
39 18   5   4   3  12 29
40 19   6   1   2  11 28
41 20   7   8   9  10 27
42 21  22  23  24  25 26
43 44  45  46  47  48 49

Valid moves are U, D, L, R
"""
from collections import namedtuple
import math

Coord = namedtuple('Coord', ['x', 'y'])


def distance(coord):
    """manhattan distance between origo and coord"""
    return abs(coord.x) + abs(coord.y)


def move_counter_clockwise(start, value, num):
    """Move from lower right corner until we reach desired value

    When moving counter clockwise we know that each number we go to
    is lower than the one before.
    """
    current = start
    side_length = int(math.sqrt(value)) - 1
    for step in range(0, side_length*4):
        if step < side_length:
            # print("move left")
            current = current._replace(x=current.x - 1)
        elif step < side_length*2:
            # print("move up")            
            current = current._replace(y=current.y + 1)
        elif step < side_length*3:
            # print("move right")
            current = current._replace(x=current.x + 1)
        else:
            # print("move down")
            current = current._replace(y=current.y - 1)            
        value -= 1
        if value == num:
            return current
    return None

def get_coordinate1(num):
    """Find where in the memory our number is located
    """
    if num == 1:
        return Coord(x=0, y=0)
    corner = Coord(x=0, y=0)
    value = 1
    layer = 3
    while True:
        corner = corner._replace(x=corner.x + 1, y=corner.y - 1)
        value = layer**2
        if value > num:
            return move_counter_clockwise(corner, value, num)
        layer += 2

def get_coordinate(num):
    """
    >>> [1**2, 3**2, 7**2, 9**2]
    [1, 9, 49, 81]
    >>> [1**2, 3**2, 5**2, 7**2, 9**2]
    [1, 9, 25, 49, 81]"""
    if num == 1:
        return Coord(0, 0)

    # corner bases are odd numbers
    corner_base = math.ceil(math.sqrt(num))
    if corner_base%2 == 0:
        corner_base += 1
    
    # we start at layer 0
    layer = math.ceil(corner_base / 2) - 1
    corner_value = corner_base ** 2
    return move_counter_clockwise(Coord(x=layer, y=-layer), corner_value, num)

# movement is getting to the right coordinate for 1

TESTS = [
    (1, 0, Coord(0, 0)),
    (12, 3, Coord(2, 1)),
    (23, 2, Coord(0, -2)),
    (3, 2, Coord(1, 1)),
    (28, 3, Coord(3, 0)),
    (37, 6, Coord(-3, 3)),
    (1024, 31, Coord(-15, 16)),
    (368078, 371, Coord(-68, -303)),
]

for number, want, c in TESTS:
    nc = get_coordinate(number)
    got = distance(nc)
    assert  got == want, "{} -> {} gave {} wanted {}".format(number, nc, got, want)
    assert  c == nc, "{} -> gave {} wanted {}".format(number, nc, c)
