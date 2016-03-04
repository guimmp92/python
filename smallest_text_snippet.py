#!/usr/bin/python

"""
Given a search string of three words, find the smallest snippet of the document that
contains all three of the search words---i.e., the snippet with smallest number of
words in it. You are given the index positions where these words occur in the document,
such as word1: (1, 4, 5), word2: (3, 9, 10), and word3: (2, 6, 15).
Each of the lists are in sorted order, as above.

http://nbl.cewit.stonybrook.edu/algowiki/index.php/TADM2E_4.45
"""

from operator import itemgetter


def find_smallest_snippet(*args):
    """
    >>> find_smallest_snippet([1,10], [2,20], [3,30])
    [1, 3]
    >>> find_smallest_snippet([1,9,27], [6,10,19], [8,12,14])
    [8, 10]
    >>> find_smallest_snippet([1,4,11,27], [3,6,10,19], [5,8,12,14])
    [3, 5]
    >>> find_smallest_snippet([1,4,5], [3,9,10], [2,6,15])
    [1, 3]
    """
    master = []
    for word, indeces in enumerate(args):
        master.extend([word, i] for i in indeces)  # [word number, index]
    master.sort(key=itemgetter(1))

    tops = {}
    lower_bound = master[0][1]
    upper_bound = master[-1][1]
    min_span = upper_bound - lower_bound + 1
    for word, index in master:
        tops[word] = index
        if len(tops) == len(args):
            cur_span = max(tops.values()) - min(tops.values()) + 1
            if cur_span < min_span:
                lower_bound = min(tops.values())
                upper_bound = max(tops.values())
                min_span = cur_span

    return [lower_bound, upper_bound]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
