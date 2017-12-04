"""How many valid passphrases?

To ensure security, a valid passphrase must contain no duplicate words.
"""
import fileinput

# INPUT = [
#     "aa bb cc dd ee",
#     "aa bb cc dd aa",
#     "aa bb cc dd aaa"
# ]

INPUT = fileinput.input()
invalid: bool = False
VALID = 0

for line in INPUT:
    passphrase = line.strip()
    words = passphrase.split()
    used_words: dict = {}
    invalid = False
    for word in words:
        if used_words.get(word):
            invalid = True
            break
        else:
            used_words[word] = 1
    if not invalid:
        VALID += 1

print(VALID)
