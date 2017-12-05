"""
How many steps does it take to reach the exit?

Follow the instructions until you exit the array
"""
import fileinput


def get_instructions():
    # inputs = ["0", "3", "0", "1", "-3",]
    inputs = fileinput.input()
    instructions = []

    for line in inputs:
        instruction = int(line.strip())
        instructions.append(instruction)
    return instructions


def follow_instructions(instructions):
    current = 0
    moves = 0
    while current < len(instructions):
        move = instructions[current]
        instructions[current] += 1
        current = current + move
        moves += 1
    return moves

INSTRUCTIONS = get_instructions()
print(follow_instructions(INSTRUCTIONS))
