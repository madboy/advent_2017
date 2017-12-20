"""
The little packet looks up at you, hoping you can help it find the way. What letters will it see (in the order it would see them) if it follows the path? (The routing diagram is very wide; make sure you view it without line wrapping.)
"""
from collections import namedtuple
import fileinput
import string

Point = namedtuple('Point', ['row', 'col'])
Program = namedtuple('Program', ['pos', 'd'])


def _valid(row: int, col: int) -> bool:
    try:
        return diagram[row][col] != " "
    except Exception:
        return False


def get_valid_directions(pos: Point, diagram: list) -> list:
    """
    determine which directions that's possible to move in
    
    returns [up, down, left, right]
    """
    return [
        _valid(pos.row-1, pos.col),
        _valid(pos.row+1, pos.col),
        _valid(pos.row, pos.col-1),
        _valid(pos.row, pos.col+1)
    ]


def move(p: Program, digram: list, letter: list) -> Program:
    opposite_directions = {
        Point(-1, 0): 1,
        Point(1, 0): 0,
        Point(0, -1): 3,
        Point(0, 1): 2,
    }

    directions = {
        0: Point(-1, 0), # up
        1: Point(1, 0), # down
        2: Point(0, -1), # left
        3: Point(0, 1), # right
    }

    instruction = diagram[p.pos.row][p.pos.col]

    if instruction in string.ascii_uppercase:
        letters.append(instruction)
        return Program(Point(p.pos.row + p.d.row, p.pos.col + p.d.col), p.d)
    if instruction in ["|", "-"]:
        d = p.d
    elif instruction == "+":
        # determine which direction we should change too
        # this should be the only case when we change direction
        # use current direction to help us continue on the correct path
        valid = get_valid_directions(p.pos, diagram)
        opposite = opposite_directions[p.d]
        valid[opposite] = False
        d = directions[valid.index(True)]
    else:
        # end of the line
        return None
    return Program(Point(p.pos.row + d.row, p.pos.col + d.col), d)


inputs = [
    "     |          ",
    "     |  +--+    ",
    "     A  |  C    ",
    " F---|----E|--+ ",
    "     |  |  |  D ",
    "     +B-+  +--+ ",
]

inputs = fileinput.input()

diagram = []
letters = []
for line in inputs:
    diagram.append(line.strip("\n"))

# look at the top row for where entry to maze is
start = diagram[0].index("|")
p = Program(Point(0, start), Point(1, 0))
current = p

found_exit = False
count = 0
while not found_exit:
    current = move(current, diagram, letters)
    if not current:
        found_exit = True
        print("".join(letters), count)
    count += 1
