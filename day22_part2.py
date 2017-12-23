"""
Clean nodes become weakened.
Weakened nodes become infected.
Infected nodes become flagged.
Flagged nodes become clean.

Decide which way to turn based on the current node:
If it is clean, it turns left.
If it is weakened, it does not turn, and will continue moving in the same direction.
If it is infected, it turns right.
If it is flagged, it reverses direction, and will go back the way it came.
Modify the state of the current node, as described above.
The virus carrier moves forward one node in the direction it is facing.

Given your actual map, after 10000000 bursts of activity, how many bursts cause a node to become infected? (Do not count nodes that begin infected.)
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
for i in range(0, 10000000):
    if grid.get((vc.x, vc.y), ".") == ".":
        grid[(vc.x, vc.y)] = "w"
        vc = vc._replace(d= (vc.d-1)%4)
    elif grid.get((vc.x, vc.y), ".") == "w":
        grid[(vc.x, vc.y)] = "#"
        cause_infection += 1
    elif grid.get((vc.x, vc.y), ".") == "#":
        grid[(vc.x, vc.y)] = "f"
        vc = vc._replace(d= (vc.d+1)%4)
    else:
        grid.pop((vc.x, vc.y))
        # reverse direction
        vc = vc._replace(d= (vc.d+2)%4)
    vc = move(vc)

print(cause_infection)
