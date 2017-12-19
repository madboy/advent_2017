"""
Once both of your programs have terminated (regardless of what caused them to do so), how many times did program 1 send a value?
"""
import fileinput
from collections import namedtuple, deque

Program = namedtuple('Program', ['pid', 'snd', 'rcv', 'active', 'snds'])

def get_value(reg, register: dict, pid: int) -> int:
    try:
        value = int(reg)
        return value
    except ValueError:
        return register.get(reg, pid)


def parse_instruction(instruction: str, gregister: dict, pid: str, register: dict) -> (int, bool):
    if instruction.startswith("snd"):
        _, val = instruction.split()
        val = get_value(val, register, gregister[pid].pid)
        gregister[pid] = gregister[pid]._replace(snds=gregister[pid].snds+1)
        gregister[pid].snd.append(val)
    elif instruction.startswith("set"):
        _, reg, val = instruction.split()
        register[reg] = get_value(val, register, gregister[pid].pid)
    elif instruction.startswith("add"):
        _, reg, val = instruction.split()
        register[reg] = get_value(reg, register, gregister[pid].pid) + get_value(val, register, gregister[pid].pid)
    elif instruction.startswith("mul"):
        _, reg, val = instruction.split()
        register[reg] = get_value(reg, register, gregister[pid].pid) * get_value(val, register, gregister[pid].pid)
    elif instruction.startswith("mod"):
        _, reg, val = instruction.split()
        register[reg] = get_value(reg, register, gregister[pid].pid)%get_value(val, register, gregister[pid].pid)
    elif instruction.startswith("rcv"):
        _, reg = instruction.split()
        # pop value from queue
        # if no value enter waiting mode
        q = gregister.get(gregister[pid].rcv).snd
        try:
            val = q.popleft()
            register[reg] = val
            gregister[pid] = gregister[pid]._replace(active = True)
        except IndexError:
            gregister[pid] = gregister[pid]._replace(active = False)
    elif instruction.startswith("jgz"):
        _, reg, val = instruction.split()
        if get_value(reg, register, pid) > 0:
            return get_value(val, register, gregister[pid].pid), False
    else:
        print("Error error: unknown instruction")
    return 0, False

inputs = fileinput.input()


pid0 = Program(0, deque([]), "one", True, 0)
pid1 = Program(1, deque([]), "zero", True, 0)

register = dict()

register["zero"] = pid0
register["register0"] = dict()
register["one"] = pid1
register["register1"] = dict()

instructions0 = []
instructions1 = []
for line in inputs:
    instruction = line.strip()
    instructions0.append(instruction)
    instructions1.append(instruction)

counter0 = 0
counter1 = 0
recovered = False
while register["zero"].active or register["one"].active:
    adjust0, recovered = parse_instruction(instructions0[counter0], register, "zero", register["register0"])
    
    if register["zero"].active:
        if adjust0:
            counter0 += adjust0
        else:
            counter0 += 1

    adjust1, recovered = parse_instruction(instructions1[counter1], register, "one", register["register1"])
    if register["one"].active:
        if adjust1:
            counter1 += adjust1
        else:
            counter1 += 1

print(register["zero"])
print(register["one"])
