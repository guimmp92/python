#!/usr/bin/python

"""
Find pairs in an integer array whose sum is equal to 10 (in linear time).
"""

from collections import (defaultdict, namedtuple)
import random

arr = []
for i in range(50):
    arr.append(random.randint(0, 10))
print "The array: {0}".format(arr)

d = defaultdict(list)
pair = namedtuple('Pair', ('a', 'b'))
pairs = []

for idx, elem in enumerate(arr):
    if len(d[10-elem]) >= 1:
        new_pair = pair((elem, idx), (10-elem, d[10-elem].pop()))
        pairs.append(new_pair)
    else:
        d[elem].append(idx)

print "\nThe pairs whose sum is equal to 10:"
for p in pairs:
    print p
