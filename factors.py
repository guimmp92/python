#!/usr/bin/python

"""
https://codility.com/programmers/task/count_factors/
"""


def solution(N):
    candidate = 1
    result = 0
    while candidate * candidate < N:
        # N has two factors: candidate and N // candidate
        if N % candidate == 0:
            result += 2
    candidate += 1

    # If N is square of some value.
    if candidate * candidate == N:
        result += 1

    return result


def solution_slow(N):
    count = 0
    for i in range(1, N+1):
        M = N // i
        if i * M == N:
            count += 1
    return count
