"""How many valid passphrases?

To ensure security, a valid passphrase must contain no duplicate words,
or anagrams that can formed from other words.
"""
import fileinput

# INPUT = [
#     "abcde fghij",
#     "abcde xyz ecdab",
#     "a ab abc abd abf abj",
#     "iiii oiii ooii oooi oooo",
#     "oiii ioii iioi iiio",
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
        word = "".join(sorted(word))
        if used_words.get(word):
            invalid = True
            break
        else:
            used_words[word] = 1
    if not invalid:
        VALID += 1

print(VALID)
