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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
