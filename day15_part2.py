"""
After 40 million pairs, what is the judge's final count?
"""

def next_value(prev: int, factor: int, multiple: int) -> int:
    product = factor*prev
    divider = 2147483647
    value = product%divider
    if (value % multiple) == 0:
        return value
    else:
        return next_value(value, factor, multiple)

start_a =  873
factor_a = 16807

start_b =  583
factor_b = 48271

matches = 0
for i in range(0, 5000000):
    next_a = next_value(start_a, factor_a, 4)
    next_b = next_value(start_b, factor_b, 8)

    ba = '{:032b}'.format(next_a)
    bb = '{:032b}'.format(next_b)

    if ba[-16:] == bb[-16:]:
        matches += 1

    start_a = next_a
    start_b = next_b

print(matches)
