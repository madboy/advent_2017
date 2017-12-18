"""
What is the value after 0 the moment 50000000 is inserted?
"""
inputs = 359

state = [0]
pos = 0
value = 1
current = 1

for i in range(0,50000000):
    pos = (inputs + pos) % value + 1
    if pos == 1:
        current = value
    value += 1

print(current)
