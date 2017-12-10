"""
Your goal is to find the total score for all groups in your input. Each group is assigned a score which is one more than the score of the group that immediately contains it. (The outermost group gets a score of 1.)

What is the total score for all groups in your input?
"""
from collections import namedtuple
import random
import fileinput

Group = namedtuple('Group', ['name', 'score', 'parent', 'child'])

# inputs = [
#     ("{}", 1),
#     ("{{},{}}", 5),
#     ("{{{}}}", 6),
#     ("{{{},{},{{}}}}", 16),
#     ("{<a>,<a>,<a>,<a>}", 1),
#     ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
#     ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
#     ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3),
# ]

inputs = fileinput.input()

def name() -> str:
    nbr = random.randint(0, 200)
    return '{:04X}'.format(nbr)

def score(groups: list) -> int:
    total = 0
    for group in groups:
        total += group.score
    return total

def groups_str(groups: list) -> str:
    s = ""
    for group in groups:
        s += "{}\n".format(group)
    return s

for line in inputs:
    group = line.strip()
    current_group = None
    garbage = False
    ignore = False
    groups = []
    for c in group:
        if ignore:
            ignore = False
        else:
            if c == "!":
                ignore = True
            elif c == "<" and not garbage:
                garbage = True
            elif c == ">":
                garbage = False
            elif c == "{" and not garbage:
                # this should only happen for the most outer group
                if not current_group:
                    current_group = Group(
                        score=1,
                        parent=None,
                        child=None,
                        name=name())
                else:
                    parent_group = current_group
                    current_group = Group(
                        score=current_group.score+1,
                        parent=current_group,
                        child=None,
                        name=name())
                    parent_group._replace(child=current_group)
                groups.append(current_group)
            elif c == "}" and not garbage:
                current_group = current_group.parent
    print(score(groups))
