"""
How many programs are in the group that contains program ID 0?
""" 
from collections import namedtuple, deque
import fileinput

# inputs = [
#     "0 <-> 2",
#     "1 <-> 1",
#     "2 <-> 0, 3, 4",
#     "3 <-> 2, 4",
#     "4 <-> 2, 3, 6",
#     "5 <-> 6",
#     "6 <-> 4, 5",
# ]

inputs = fileinput.input()

Program = namedtuple('Program', ['name', 'connections'])

programs = {}
for line in inputs:
    name, connections = list(map(str.strip , line.split("<->")))
    connections = list(map(str.strip, connections.split(",")))
    programs[name] = Program(name, connections)

stack = deque(programs['0'].connections)
connections = set({})
while stack:
    current = stack.popleft()
    connections.add(current)
    for c in programs[current].connections:
        if c not in connections:
            stack.append(c)

print(len(connections))
