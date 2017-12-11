"""
However, you should instead use the standard list size of 256 (with values 0 to 255) and the sequence of lengths in your puzzle input. Once this process is complete, what is the result of multiplying the first two numbers in the list?
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

lengths = [70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41]
circular_list = list(range(0,256))

# lengths = [3, 4, 1, 5,]
# circular_list = [0, 1, 2, 3, 4,]

skip = 0
position = 0
list_length = len(circular_list)
for length in lengths:
    circular_list = reverse_section(circular_list, position, length)
    position = (position + length + skip)%list_length
    skip += 1
print(circular_list[0]*circular_list[1])
