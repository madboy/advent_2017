"""
In the example above, there were 2 groups: one consisting of programs 0,2,3,4,5,6, and the other consisting solely of program 1.

How many groups are there in total?
""" 
from collections import namedtuple, deque
import fileinput

inputs = [
    "0 <-> 2",
    "1 <-> 1",
    "2 <-> 0, 3, 4",
    "3 <-> 2, 4",
    "4 <-> 2, 3, 6",
    "5 <-> 6",
    "6 <-> 4, 5",
]

inputs = fileinput.input()

Program = namedtuple('Program', ['name', 'connections'])

programs = {}
for line in inputs:
    name, connections = list(map(str.strip , line.split("<->")))
    connections = list(map(str.strip, connections.split(",")))
    programs[name] = Program(name, connections)

# in the given example we only need to start with one group and work from there
# but now we need to go through all possible group starting points that we
# haven't seen already as part of another group
groups = 0
seen = set({})
for program in programs.keys():
    if program not in seen:
        seen.add(program)
        stack = deque(programs[program].connections)
        connections = set({})
        while stack:
            current = stack.popleft()
            connections.add(current)
            for c in programs[current].connections:
                if c not in connections:
                    stack.append(c)
        seen.update(connections)
        groups += 1

print(groups)
