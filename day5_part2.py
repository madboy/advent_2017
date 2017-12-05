"""
How many steps does it take to reach the exit?

Follow the instructions until you exit the array
Normal action when having used a move is to increment it,
in this version we instead decrement it when the move is over 3 steps.
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
        if move >= 3:
            instructions[current] -= 1
        else:
            instructions[current] += 1        
        current = current + move
        moves += 1
    return moves

INSTRUCTIONS = get_instructions()
print(follow_instructions(INSTRUCTIONS))
