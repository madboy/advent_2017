"""
To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).
"""
from collections import defaultdict
import fileinput
inputs = fileinput.input()

# inputs = [
#     "b inc 5 if a > 1",
#     "a inc 1 if b < 5",
#     "c dec -10 if a >= 1",
#     "c inc -20 if c == 10",
# ]



def inc_or_dec(register, iod, value, maximum):
    if iod == "dec":
        value = registers.get(register, 0) - int(value)
    else:
        value = registers.get(register, 0) + int(value)

    if value > maximum:
        maximum = value
    registers[register] = value
    return maximum

MAXIMUM = 0
registers = defaultdict(int)

for line in inputs:
    instruction = line.strip()
    register, iod, value, _, cond1, cond2, cond3 = instruction.split()
    if cond2 == ">":
        if registers.get(cond1, 0) > int(cond3):
            MAXIMUM = inc_or_dec(register, iod, value, MAXIMUM)
    elif cond2 == "<":
        if registers.get(cond1, 0) < int(cond3):
            MAXIMUM = inc_or_dec(register, iod, value, MAXIMUM)
    elif cond2 == ">=":
        if registers.get(cond1, 0) >= int(cond3):
            MAXIMUM = inc_or_dec(register, iod, value, MAXIMUM)
    elif cond2 == "==":
        if registers.get(cond1, 0) == int(cond3):
            MAXIMUM = inc_or_dec(register, iod, value, MAXIMUM)
    elif cond2 == "<=":
        if registers.get(cond1, 0) <= int(cond3):
            MAXIMUM = inc_or_dec(register, iod, value, MAXIMUM)
    elif cond2 == "!=":
        if registers.get(cond1, 0) != int(cond3):
            MAXIMUM = inc_or_dec(register, iod, value, MAXIMUM)


print(MAXIMUM)
