"""
Recreate the Turing machine and save the computer!
What is the diagnostic checksum it produces once it's working again?

Once the specified number of steps have been executed,
the Turing machine should pause; once it does, count the number
of times 1 appears on the tape.

Begin in state A.
Perform a diagnostic checksum after 12208951 steps.
"""
from collections import defaultdict

L, R = -1, 1

states = {
    'A': ((1, 'B', R), (0, 'E', L)),
    'B': ((1, 'C', L), (0, 'A', R)),
    'C': ((1, 'D', L), (0, 'C', R)),
    'D': ((1, 'E', L), (0, 'F', L)),
    'E': ((1, 'A', L), (1, 'C', L)),
    'F': ((1, 'E', L), (1, 'A', R)),
}

def machine(states, current_state):
    tape = defaultdict(int)
    cursor = 0
    for i in range(0,12208951):
        cursor_value = tape.get(cursor, 0)
        tape[cursor], n, m = states[current_state][cursor_value]
        cursor += m
        current_state = n
    return tape

print(sum(machine(states, 'A').values()))
