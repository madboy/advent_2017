"""
The strength of a bridge is the sum of the port types in each component. 

(Note how, as shown by 10/1, order of ports within a component doesn't matter. However, you may only use each port on a component once.)


What is the strength of the strongest bridge you can make with the components you have available?
"""
from collections import namedtuple, deque, defaultdict
import fileinput

inputs = [
    "0/2",    
    "2/2",
    "2/3",
    "3/4",
    "3/5",
    "0/1",
    "10/1",
    "9/10",
]

inputs = fileinput.input()

# key the components on ports like so:
# 0/1 => {0: [0/1,], 1: [0/1]}
# 0/2 => {0: [0/1, 0/2], 1: [0/1,], 2: [0/2]}

# create valid bridges,
# start with the components that have a 0 port and then continue
# creating valid bridges based on all the candidates that we have

# bridges queue
# ([chain], tail)
# for each variation
# pick up tail
# check if there's anything we can connect to tail
# we need to know which of the ports that we can use
# if
# multiple components fork the variation and add all to queue
# one attach it and make it tail and add back to queue
# none, mark variation as done and move to completed list

# choose the one with the highest sum
# and choose the one which is the longest and has the highest sum of those

Bridge = namedtuple('Bridge', ['chain', 'tail'])
Component = namedtuple('Component', ['used', 'unused'])
Ports = namedtuple('Ports', ['p1', 'p2'])

components = defaultdict(set)

for line in inputs:
    component = line.strip()
    port1, port2 = map(int, component.split("/"))
    ports = Ports(port1, port2)
    components[port1].add(ports)
    components[port2].add(ports)

bridgeq = deque()

# we know that the bridge can only start with a zero pin
for zero_pin in components[0]:
    if zero_pin.p1 == 0:
        bridgeq.append(Bridge([zero_pin], Component(zero_pin.p1, zero_pin.p2)))
    else:
        bridgeq.append(Bridge([zero_pin], Component(zero_pin.p2, zero_pin.p1)))

completed = []
while bridgeq:
    bridge = bridgeq.popleft()
    candiates = components[bridge.tail.unused]
    if candiates:
        for candidate in candiates:
            if candidate not in bridge.chain:
                if candidate.p1 == bridge.tail.unused:
                    tail = Component(candidate.p1, candidate.p2)
                else:
                    tail = Component(candidate.p2, candidate.p1)
                bridgeq.append(Bridge(bridge.chain + [candidate], tail))
            else:
                # if we cannot find any more components to add to the bridge we'll
                # add it to the completed bridges
                completed.append(bridge)
    else:
        # never seem to get here
        completed.append(bridge)

maxes = defaultdict(int)
for c in completed:
    total = 0
    for v in c.chain:
        total += v.p1 + v.p2
    if total > maxes[len(c.chain)]:
        maxes[len(c.chain)] = total

print(max(maxes.values()))
print(maxes[max(maxes.keys())])
