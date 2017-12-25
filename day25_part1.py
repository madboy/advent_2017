"""
Recreate the Turing machine and save the computer!
What is the diagnostic checksum it produces once it's working again?

Once the specified number of steps have been executed,
the Turing machine should pause; once it does, count the number
of times 1 appears on the tape.

Begin in state A.
Perform a diagnostic checksum after 12208951 steps.
"""
from collections import defaultdict, namedtuple, Counter

Action = namedtuple('Action', ['write', 'next', 'move'])
State = namedtuple('State', ['name', 'action_if_0', 'action_if_1'])

a = State('A', action_if_0=Action(1, 'B', 1), action_if_1=Action(0, 'E', -1))
b = State('B', action_if_0=Action(1, 'C', -1), action_if_1=Action(0, 'A', 1))
c = State('C', action_if_0=Action(1, 'D', -1), action_if_1=Action(0, 'C', 1))
d = State('D', action_if_0=Action(1, 'E', -1), action_if_1=Action(0, 'F', -1))
e = State('E', action_if_0=Action(1, 'A', -1), action_if_1=Action(1, 'C', -1))
f = State('F', action_if_0=Action(1, 'E', -1), action_if_1=Action(1, 'A', 1))

states = {
    a.name: a,
    b.name: b,
    c.name: c,
    d.name: d,
    e.name: e,
    f.name: f,
}

tape = defaultdict(int)
current_state = a
cursor = 0
for i in range(0,12208951):
    cursor_value = tape.get(cursor, 0)
    if cursor_value == 0:
        w, n, m = current_state.action_if_0
    else:
        w, n, m = current_state.action_if_1
    if w == 0:
        del tape[cursor]
    else:
        tape[cursor] = w
    cursor += m
    current_state = states[n]

c = Counter(tape.values())
print(c[1])
