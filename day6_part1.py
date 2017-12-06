"""
Given the initial block counts in your puzzle input, how many redistribution cycles must be completed before a configuration is produced that has been seen before?
"""
from collections import defaultdict


def find_max(banks: list) -> (int, int):
    m = max(banks)
    return (m, banks.index(m))


def increment_index(nbr: int, index: int) -> int:
    index = index + 1
    return index % nbr


def balance_banks(banks: list):
    number_of_banks = len(banks)
    bank_configurations = defaultdict(int)

    while str(banks) not in bank_configurations:
        bank_configurations[str(banks)] += 1
        value, index = find_max(banks)
        banks[index] = 0
        for i in range(0, value):
            index = increment_index(number_of_banks, index)
            banks[index] += 1
    return len(bank_configurations)

banks = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
# banks = [0, 2, 7, 0]  
print(balance_banks(banks))
