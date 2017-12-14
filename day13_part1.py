"""
The severity of getting caught on a layer is equal to its depth multiplied by its range. (Ignore layers in which you do not get caught.) The severity of the whole trip is the sum of these values. In the example above, the trip severity is 0*3 + 6*4 = 24.

Given the details of the firewall you've recorded, if you leave immediately, what is the severity of your whole trip?
"""
from collections import namedtuple
import fileinput

inputs = fileinput.input()

Layer = namedtuple('Layer', ['depth', 'range'])
firewall = {}

for line in inputs:
    line = line.strip()
    depth, r = list(map(int, line.split(": ")))
    firewall[depth] = Layer(depth, r)

severity = 0

for i in range(0, depth+1):
    l = firewall.get(i)
    if l and l.depth%((l.range-1)*2) == 0:
        severity += (l.depth * l.range)

print(severity)
