"""
What is the fewest number of picoseconds that you need to delay the packet to pass through the firewall without being caught?
"""
from collections import namedtuple
import fileinput
import copy

inputs = fileinput.input()

# inputs = [
#     "0: 3",
#     "1: 2",
#     "4: 4",
#     "6: 4",
# ]

Layer = namedtuple('Layer', ['depth', 'range'])
firewall = {}

for line in inputs:
    line = line.strip()
    depth, r = list(map(int, line.split(": ")))
    firewall[depth] = Layer(depth, r)

trapped = True
delay = 0
while trapped:
    delay += 1
    for i in range(0, depth+1):
        l = firewall.get(i)
        if l and (delay+l.depth)%((l.range-1)*2) == 0:
            trapped = True
            break
        else:
            trapped = False
print(delay)
