"""
What is the largest value in any register after completing the instructions in your puzzle input?
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


def inc_or_dec(register, iod, value):
    if iod == "dec":
        registers[register] = registers.get(register, 0) - int(value)
    else:
        registers[register] = registers.get(register, 0) + int(value)

registers = defaultdict(int)

for line in inputs:
    instruction = line.strip()
    register, iod, value, _, cond1, cond2, cond3 = instruction.split()
    if cond2 == ">":
        if registers.get(cond1, 0) > int(cond3):
            inc_or_dec(register, iod, value)
    elif cond2 == "<":
        if registers.get(cond1, 0) < int(cond3):
            inc_or_dec(register, iod, value)
    elif cond2 == ">=":
        if registers.get(cond1, 0) >= int(cond3):
            inc_or_dec(register, iod, value)
    elif cond2 == "==":
        if registers.get(cond1, 0) == int(cond3):
            inc_or_dec(register, iod, value)
    elif cond2 == "<=":
        if registers.get(cond1, 0) <= int(cond3):
            inc_or_dec(register, iod, value)
    elif cond2 == "!=":
        if registers.get(cond1, 0) != int(cond3):
            inc_or_dec(register, iod, value)

maximum = 0
for k, v in registers.items():
    if v > maximum:
        maximum = v

print(maximum)
