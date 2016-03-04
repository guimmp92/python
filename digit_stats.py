#!/usr/bin/python

"""
https://www.codeeval.com/open_challenges/144/

Given the numbers "a" and "n" find out how many times each digit from zero to nine is
the last digit of the number in a sequence [ a, a2, a3, ... an-1, an ].
"""
from collections import defaultdict
import sys


def correct_but_inefficient(a, n):
    counter = defaultdict(int)
    for i in range(1, n+1):
        num = pow(a, i)
        counter[num % 10] += 1
    return counter


def solution(a, n):
    series = []
    last_digit = None
    for i in xrange(1, n+1):
        last_digit = pow(a, i) % 10
        if last_digit not in series:
            series.append(last_digit)
        else:
            break

    counter = defaultdict(int)
    q, r = divmod(n, len(series))
    for i in series:
        counter[i] = q
    for i in range(r):
        counter[series[i]] += 1

    return counter

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as infile:
        for line in infile:
            data = map(int, line.strip().split())
            counter = solution(data[0], data[1])
            res = []
            for i in range(10):
                res.append("{0}: {1}".format(i, counter[i]))
            print ", ".join(res)
