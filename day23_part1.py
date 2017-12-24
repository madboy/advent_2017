"""
set X Y sets register X to the value of Y.
sub X Y decreases register X by the value of Y.
mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)

If you run the program (your puzzle input), how many times is the mul instruction invoked?
"""
import fileinput

def get_value(reg, register: dict) -> int:
    try:
        value = int(reg)
        return value
    except ValueError:
        return register.get(reg, 0)


def parse_instruction(instruction: str, register: dict, muls) -> int:
    if instruction.startswith("set"):
        _, reg, val = instruction.split()
        register[reg] = get_value(val, register)
    elif instruction.startswith("sub"):
        _, reg, val = instruction.split()
        register[reg] = get_value(reg, register) - get_value(val, register)
    elif instruction.startswith("mul"):
        _, reg, val = instruction.split()
        register[reg] = get_value(reg, register) * get_value(val, register)
        muls += 1
    elif instruction.startswith("jnz"):
        _, reg, val = instruction.split()
        if get_value(reg, register) != 0:
            return get_value(val, register), muls
    else:
        print("Error error: unknown instruction")
    return 0, muls

inputs = fileinput.input()

program = []
for line in inputs:
    program.append(line.strip())

registers = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
}

counter = 0
muls = 0
while counter < len(program):
    adjust, muls = parse_instruction(program[counter], registers, muls)
    if adjust:
        counter += adjust
    else:
        counter += 1
print(muls)
print(registers)
