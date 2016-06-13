#!/usr/bin/python

"""
Itertools recipes

https://docs.python.org/2/library/itertools.html#recipes
"""
from itertools import chain, combinations, count, imap, islice
import operator


def take(n, iterable):
    """ Return the first n elements of the iterable as a list.
    >>> take(4, [1, 2, 3, 4, 5, 6, 7])
    [1, 2, 3, 4]
    """
    return list(islice(iterable, n))


def tabulate(function, start=0):
    """ Return function(0), function(1), ...
    """
    return imap(function, count(start))


def flatten(list_of_lists):
    """ Flatten one level of nesting.
    >>> flatten([[1, 3, 4], [5, 6, 7, 8], [9, 0]])
    [1, 3, 4, 5, 6, 7, 8, 9, 0]
    """
    # return list(chain(*list_of_lists))
    # or:
    return list(chain.from_iterable(list_of_lists))


def dotproduct(vec1, vec2):
    """ Sum of the dot product.
    >>> dotproduct([1, 2, 3], [4, 5, 6])
    32
    """
    return sum(imap(operator.mul, vec1, vec2))


def powerset(iterable):
    """
    >>> powerset([1, 2, 3])
    [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    """
    return list(chain.from_iterable([combinations(iterable, i) for i in range(len(iterable)+1)]))


"""
# Warmup

You are given two iterators. Exhaust both iterators in any order and return the
unique elements as another iterator.

e.g.
it1 = iter([9,0,1,3,3])
it2 = iter([1,3,5,6,0,2])
your_it = ([9,0,1,3,5,6,2])

# Followup

Your solution uses O(n+m) space in the worst case. Can you do better if the
lists are always sorted?

# Difficulties

* Know about iterators (the only way to know they're empty is if they throw an exception)

# Solutions

* Warmup - use a set() to store seen numbers, exhaust both iterators in order
* Followup - grab an element, exhaust both iterators of this element (use caching)
* Followup - implement via a peeking iterator https://leetcode.com/problems/peeking-iterator/
"""


def warmup(it1, it2):
    uniques = set()
    for element in chain(it1, it2):
        if element not in uniques:
            uniques.add(element)
            yield element


def followup(it1, it2):
    pit1 = PeekingIterator(it1)
    pit2 = PeekingIterator(it2)
    while pit1.has_next() and pit2.has_next():
        if pit1.peek() <= pit2.peek():
            yield pit1.next()
        else:
            yield pit2.next()
    while pit1.has_next():
        yield pit1.next()
    while pit2.has_next():
        yield pit2.next()


class PeekingIterator(object):
    """ https://github.com/kamyu104/LeetCode/blob/master/Python/peeking-iterator.py """
    def __init__(self, iterator):
        self.iterator = iterator
        self._get_next()

    def _get_next(self):
        try:
            self._next = next(self.iterator)
        except StopIteration:
            self._next = None

    def has_next(self):
        return True if self._next else False

    def next(self):
        res = None
        if self._next:
            res = self._next
            self._get_next()
        return res

    def peek(self):
        return self._next


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    pi = PeekingIterator(iter([1, 2, 3]))
    print pi.next()
    print pi.has_next()
    print pi.peek()
    print pi.next()
    print pi.peek()
    print pi.next()
    print pi.has_next()
    print pi.peek()
    print pi.next()
