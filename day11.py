"""
  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

--- Part One ---

You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

--- Part Two ---

How many steps away is the furthest he ever got from his starting position?

Excellent resource: https://www.redblobgames.com/grids/hexagons/
"""
from collections import namedtuple
import fileinput

Hexagon = namedtuple('Hexagon', ['col', 'row'])

def hex_distance(hex1, hex2):
    """this converts the axial coordinates into cube coordinates 
    and returns half manhattan/taxi cab distance for a cube coordinate system"""
    return (abs(hex1.col - hex2.col) 
          + abs(hex1.col + hex1.row - hex2.col - hex2.row)
          + abs(hex1.row - hex2.row)) / 2

start = Hexagon(0, 0)
pos = start

moves = []
distances = []

for line in fileinput.input():
    line = line.strip()
    moves = line.split(",")

for move in moves:
    if move == "n":
        pos = pos._replace(row=pos.row-1)
    elif move == "ne":
        pos = pos._replace(col=pos.col+1, row=pos.row-1)
    elif move == "se":
        pos = pos._replace(col=pos.col+1)
    elif move == "s":
        pos = pos._replace(row=pos.row+1)
    elif move == "sw":
        pos = pos._replace(col=pos.col-1, row=pos.row+1)
    elif move == "nw":
        pos = pos._replace(col=pos.col-1)
    else:
        print("invalid direction")
    distances.append(hex_distance(start,pos))

print(hex_distance(start, pos))
print(max(distances))

