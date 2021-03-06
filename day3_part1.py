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


def distance(a, b=Coord(0,0)):
    """manhattan distance between coordinates a and b"""
    return abs(a.x - b.x) + abs(a.y - b.y)


def get_coordinate(num):
    """
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
    side_length = int(corner_base) - 1

    # move counter clockwise towards decreasing values
    lower_right = corner_value
    lower_left = corner_value-side_length    
    upper_left = corner_value-2*side_length
    upper_right = corner_value-3*side_length
    
    if lower_left < num:
        # print("bottom side")
        return Coord(layer - (lower_right - num), -layer)
    elif upper_left < num:
        # print("left side")
        return Coord(-layer, layer - (lower_left - num))
    elif upper_right < num:
        # print("upper side")
        return Coord(-layer + (upper_left - num), layer)
    else:
        # print("right side")
        return Coord(layer, layer - (upper_right - num))


TESTS = [
    (1, 0, Coord(0, 0)),
    (12, 3, Coord(2, 1)),
    (23, 2, Coord(0, -2)),
    (3, 2, Coord(1, 1)),
    (28, 3, Coord(3, 0)),
    (37, 6, Coord(-3, 3)),
    (1024, 31, Coord(-15, 16)),
    (368078, 371, Coord(-68, -303)), # puzzle input
]

for number, want, c in TESTS:
    nc = get_coordinate(number)
    got = distance(nc)
    assert  got == want, "{} -> {} gave {} wanted {}".format(number, nc, got, want)
    assert  c == nc, "{} -> gave {} wanted {}".format(number, nc, c)
