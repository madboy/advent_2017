"""
Given that exactly one program is the wrong weight, what would its weight need to be to balance the entire tower?
"""
from collections import namedtuple, defaultdict
import fileinput

INPUTS = fileinput.input()
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

def read_input(inputs):
    for line in inputs:
        program = line.strip()
        if "->" in program:
            program_info, above = program.split("->")
            children = (list(map(str.strip , above.split(","))))
            name, weight = program_info.split()
            weight = int(weight.strip("()"))
            node = Node(name, weight, children, 0)
            NODES[name] = node
            CHILDREN.extend(children)
        else:
            name, weight = line.split()
            weight = int(weight.strip("()"))
            NODES[name] = Node(name, weight, [], weight)


def total_weight(weight, children):
    total = 0
    for child in children:
        if NODES[child].total_weight == 0:
            return 0
        else:
            total += NODES[child].total_weight
    return total + weight

def calculate_weights():
    unsolved = []
    for name, node in NODES.items():
        if node.total_weight == 0:
            unsolved.append(node)

    while unsolved:
        node = unsolved.pop()
        t = total_weight(node.weight, node.children)
        if t == 0:
            unsolved.insert(0, node)
        else:
            node = node._replace(total_weight=t)
            NODES[node.name] = node

def detect_unbalanced_program(origin, children):
    seen = defaultdict(list)
    for child in children:
        t = NODES[child].total_weight
        seen[t].append(child)

    unbalanced = None
    for s in seen.values():
        if len(s) == 1:
            unbalanced = s[0]

    if unbalanced:
        return(detect_unbalanced_program(children, NODES[unbalanced].children))
    else:
        return origin

def find_adjusted_weight(unbalanced):
    to_adjust = None
    correct = None
    seen = defaultdict(list)

    for unb in unbalanced:
        t = NODES[unb].total_weight
        seen[t].append(unb)

    for s in seen.values():
        if len(s) == 1:
            to_adjust = s[0]
        else:
            correct = s[0]

    return NODES[to_adjust].weight + (NODES[correct].total_weight - NODES[to_adjust].total_weight)

Node = namedtuple('Node', ['name', 'weight', 'children', 'total_weight'])
NODES = {}
CHILDREN = []

read_input(INPUTS)
calculate_weights()

root = NODES[list(set(NODES.keys()) - set(CHILDREN)).pop()]
unbalanced = detect_unbalanced_program([root.name], root.children)
print(find_adjusted_weight(unbalanced))
