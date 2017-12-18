"""
You watch the dance for a while and record their dance moves (your puzzle input).

In what order are the programs standing after their billion dances?
"""
import fileinput
from collections import defaultdict

programs = list("abcdefghijklmnop")
seen = defaultdict(int)
counter = 0
inputs = fileinput.input()

instructions = []
for line in inputs:
    line = line.strip()
    instructions.extend(line.split(","))

# 40 is the remainder of 1_000_000_000 % 60
# 60 is the cycle length before the dance starts repeating
while counter < 40:
    seen["".join(programs)] += 1
    for instruction in instructions:
        if instruction.startswith("s"):
            section = int(instruction[1:])
            programs = programs[-section:] + programs[:-section]
        elif instruction.startswith("x"):
            f, t = list(map(int, instruction[1:].split("/")))
            tmp = programs[t]
            programs[t] = programs[f]
            programs[f] = tmp
        elif instruction.startswith("p"):
            f, t = instruction[1:].split("/")
            fi = programs.index(f)
            ti = programs.index(t)
            programs[ti] = f
            programs[fi] = t
        else:
            print("invalid instruction")
    counter += 1

print("".join(programs), counter)
