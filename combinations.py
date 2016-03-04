#!/usr/bin/python

"""
Find all combinations of a string.
"""


def find_combinations(chars, cur):
    if cur == len(chars):
        return
    combinations = [chars[cur]]
    if cur+1 < len(chars):
        next_combs = find_combinations(chars, cur+1)
        for c in next_combs:
            new_comb = chars[cur] + c
            combinations.append(new_comb)
        combinations.extend(next_combs)
    return combinations

text = "wxyz"
print find_combinations(list(text), 0)
