"""
The captcha requires you to review a sequence of digits (your puzzle input) and
find the sum of all digits that match the next digit in the list. Now, instead of
considering the next digit, it wants you to consider the digit halfway around the circular list
The list is circular, so the digit after the last digit is the first digit in the list.

What is the solution to your captcha?
"""
import fileinput


def filter_captcha(seq, step):
    for i, d in enumerate(seq):
        if d == seq[i-step]:
            yield int(d)


def get_captcha() -> str:
    captcha = ""
    for line in fileinput.input():
        line = line.strip()
        captcha += line
    return captcha

captcha = get_captcha()
step = int(len(captcha)/2)
print(sum(list(filter_captcha(captcha, step))))
