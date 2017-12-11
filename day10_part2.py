"""
Treating your puzzle input as a string of ASCII characters, what is the Knot Hash of your puzzle input? Ignore any leading or trailing whitespace you might encounter.
"""


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


circular_list = list(range(0,256))
lengths = "70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41"

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

print(create_dense_hash(circular_list))
