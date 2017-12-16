"""
Treating your puzzle input as a string of ASCII characters, what is the Knot Hash of your puzzle input? Ignore any leading or trailing whitespace you might encounter.
"""
from collections import Counter

def reverse_section(l, pos, length):
    l_length = len(l)
    end = pos + length
    if end > l_length:
        overflow = (end)%l_length
        selection = list(range(pos, l_length)) + list(range(0, overflow))
    else:
        selection = list(range(pos, end))

    # swap elements in the list
    section = []
    for select in selection:
        section.append(l[select])

    for select in selection:
        l[select] = section.pop()
    return l

def create_dense_hash(l):
    """create a dense hash from a list of length 256
    """
    h = []
    for i in range(0,16):
        s = l.pop(0)
        n = l.pop(0)
        r = s ^ n
        for ii in range(0,14):
            r = r ^ l.pop(0)
        h.append(r)
    dense_hash = ""
    for number in h:
        dense_hash += "{:x}".format(number)
    return dense_hash

b = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111",
}


total = 0
for row in range(0, 128):
    circular_list = list(range(0,256))
    lengths = "hfdlxzhv-" + str(row)

    ascii_lengths = []
    for l in lengths:
        ascii_lengths.append(ord(l))

    ascii_lengths.extend([17, 31, 73, 47, 23])

    # turn circular_list into a spare hash
    skip = 0
    position = 0
    list_length = len(circular_list)
    for turn in range(0, 64):
        for length in ascii_lengths:
            circular_list = reverse_section(circular_list, position, length)
            position = (position + length + skip)%list_length
            skip += 1

    h = create_dense_hash(circular_list)
    col = ""
    for c in h:
        col += b[c]
    cc = Counter(col) # count the different parts of the number
    total += cc["1"] # and total up the number of ones we have

print(total)
