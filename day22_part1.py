"""
If the current node is infected, it turns to its right. 
Otherwise, it turns to its left. (Turning is done in-place; the current node does not change.)

If the current node is clean, it becomes infected. Otherwise, it becomes cleaned. (This is done after the node is considered for the purposes of changing direction.)

The virus carrier moves forward one node in the direction it is facing.

Given your actual map, after 10000 bursts of activity, how many bursts cause a node to become infected? (Do not count nodes that begin infected.)
"""
from collections import namedtuple

directions: list = [(0,1), (1,0), (0,-1), (-1, 0)]

def move(vc):
    return Virus(
        x=vc.x + directions[vc.d][0],
        y=vc.y + directions[vc.d][1],
        d=vc.d        
    )

Virus = namedtuple('Virus', ['x', 'y', 'd'])

vc = Virus(0, 0, 0)
grid: dict = dict()

inputs = [
    "###.#######...#####.#..##",
    ".####...###.##...#..#....",
    ".#.#...####.###..##..##.#",
    "########.#.#...##.#.##.#.",
    "..#.#...##..#.#.##..####.",
    "..#.#.....#....#####..#..",
    "#.#..##...#....#.##...###",
    ".#.##########...#......#.",
    ".#...#..##...#...###.#...",
    "......#.###.#..#...#.####",
    ".#.###.##...###.###.###.#",
    ".##..##...#.#.#####.#...#",
    "#...#..###....#.##.......",
    "####.....######.#.##..#..",
    "..#...#..##.####.#####.##",
    "#...#.#.#.#.#...##..##.#.",
    "#####.#...#.#.#.#.##.####",
    "....###...#.##.#.##.####.",
    ".#....###.#####...#.....#",
    "#.....#....#####.#..#....",
    ".#####.#....#..##.#.#.###",
    "####.#..#..##..#.#..#.###",
    ".##.##.#.#.#.#.#..####.#.",
    "#####..##.#.#..#..#...#..",
    "#.#..#.###...##....###.##",
]

# inputs = [
#     "..#",
#     "#..",
#     "...",
# ]
length = int(len(inputs[0])/2)
height = int(len(inputs)/2)

for r, row in enumerate(inputs):
    for c, ch in enumerate(row):
        coord = (c-height, length-r)
        grid[coord] = ch

cause_infection = 0
for i in range(0, 10000):
    if grid.get((vc.x, vc.y), ".") == "#":
        grid[(vc.x, vc.y)] = "."        
        vc = vc._replace(d= (vc.d+1)%4)
    else:
        grid[(vc.x, vc.y)] = "#"
        vc = vc._replace(d = (vc.d-1)%4)
        cause_infection += 1
    vc = move(vc)

print(cause_infection)
