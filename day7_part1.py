"""
Before you're ready to help them, you need to make sure your information is correct. What is the name of the bottom program?
"""
from collections import namedtuple
import fileinput

inputs = fileinput.input()
# inputs = [
#     "pbga (66)",
#     "xhth (57)",
#     "ebii (61)",
#     "havc (66)",
#     "ktlj (57)",
#     "fwft (72) -> ktlj, cntj, xhth",
#     "qoyq (66)",
#     "padx (45) -> pbga, havc, qoyq",
#     "tknk (41) -> ugml, padx, fwft",
#     "jptl (61)",
#     "ugml (68) -> gyxo, ebii, jptl",
#     "gyxo (61)",
#     "cntj (57)",
# ]

NODES = []
ABOVE = []
for line in inputs:
    program = line.strip()
    if "->" in program:
        program_info, above = program.split("->")
        ABOVE.extend(list(map(str.strip , above.split(","))))

        name, weight = program_info.split()
        NODES.append(name)

print(set(NODES) - set(ABOVE))
