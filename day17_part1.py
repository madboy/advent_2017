"""
Perhaps, if you can identify the value that will ultimately be after the last value written (2017), you can short-circuit the spinlock. In this example, that would be 638.

What is the value after 2017 in your completed circular buffer?
"""

inputs = 359
# inputs = 3

state = [0]
pos = 0
value = 1

for i in range(0,2017):
    pos = (inputs + pos) % value + 1
    state.insert(pos, value)
    value += 1

yidx = state.index(2017)
print(yidx)
print(state[yidx+1])
