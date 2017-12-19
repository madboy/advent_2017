"""
What is the value of the recovered frequency (the value of the most recently played sound) the first time a rcv instruction is executed with a non-zero value?
"""
import fileinput

def get_value(reg, register: dict) -> int:
    try:
        value = int(reg)
        return value
    except ValueError:
        return register.get(reg, 0)


def parse_instruction(instruction: str, register: dict) -> int:
    if instruction.startswith("snd"):
        _, reg = instruction.split()
        register["freq"] = get_value(reg, register)
        # print("play sound:", get_value(reg, register))
    elif instruction.startswith("set"):
        _, reg, val = instruction.split()
        register[reg] = get_value(val, register)
        # print("set {} to {}".format(reg, get_value(val, register)))
    elif instruction.startswith("add"):
        _, reg, val = instruction.split()
        register[reg] = get_value(reg, register) + get_value(val, register)
        # print("incr {} by {}".format(reg, get_value(val, register)))
    elif instruction.startswith("mul"):
        _, reg, val = instruction.split()
        register[reg] = get_value(reg, register) * get_value(val, register)
        # print("set {} to {}*{}".format(reg, reg, get_value(val, register)))
    elif instruction.startswith("mod"):
        _, reg, val = instruction.split()
        register[reg] = get_value(reg, register)%get_value(val, register)
        # print("set {} to {}%{}".format(reg, reg, get_value(val, register)))
    elif instruction.startswith("rcv"):
        _, reg = instruction.split()
        if get_value(reg, register) > 0:
            print(register["freq"])
            return 0, True
        # print("recover last freq played if {} > 0".format(reg))
    elif instruction.startswith("jgz"):
        _, reg, val = instruction.split()
        if get_value(reg, register) > 0:
            return get_value(val, register), False
        # print("jump {} if {} > 0".format(get_value(val, register), reg))
    else:
        print("Error error: unknown instruction")
    return 0, False

inputs = [
    "set a 1",
    "add a 2",
    "mul a a",
    "mod a 5",
    "snd a",
    "set a 0",
    "rcv a",
    "jgz a -1",
    "set a 1",
    "jgz a -2",
]

inputs = fileinput.input()

register = dict()
instructions = []
for line in inputs:
    instruction = line.strip()
    instructions.append(instruction)

counter = 0
recovered = False
while not recovered:
    adjust, recovered = parse_instruction(instructions[counter], register)
    if adjust:
        counter += adjust
    else:
        counter += 1
