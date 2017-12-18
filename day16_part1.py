"""
You watch the dance for a while and record their dance moves (your puzzle input). In what order are the programs standing after their dance?
"""
import fileinput 
programs = list("abcdefghijklmnop")
# programs = list("abcde")

# inputs = [
#     "s1,x3/4,pe/b"
# ]

inputs = fileinput.input()

instructions = []
for line in inputs:
    line = line.strip()
    instructions.extend(line.split(","))

# instructions = [
#     "s3", # spin section from back to front
#     "x3/4", # swap these positions
#     "pe/b", # swap these programs
# ]

for instruction in instructions:
    if instruction.startswith("s"):
        section = int(instruction[1:])
        programs = programs[-section:] + programs[:-section]
        # assert programs == list("eabcd"), programs
    elif instruction.startswith("x"):
        f, t = list(map(int, instruction[1:].split("/")))
        tmp = programs[t]
        programs[t] = programs[f]
        programs[f] = tmp
        # assert programs == list("eabdc"), programs
    elif instruction.startswith("p"):
        f, t = instruction[1:].split("/")
        fi = programs.index(f)
        ti = programs.index(t)
        programs[ti] = f
        programs[fi] = t
        # assert programs == list("baedc"), programs
    else:
        print("invalid instruction")

print("".join(programs))
