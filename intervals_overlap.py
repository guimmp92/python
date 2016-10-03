#!/usr/bin/python
# vim: foldlevel=0

"""
Consider a big party where a log register for guest's entry and exit times is maintained.
Find the time at which there are maximum guests in the party. Note that entries in
register are not in any order.

Example:

Input: arrl[] = {1, 2, 9, 5, 5}
       exit[] = {4, 5, 12, 9, 12}
       First guest in array arrives at 1 and leaves at 4, second guest arrives at 2 and
       leaves at 5, and so on.

       Output: 5
       There are maximum 3 guests at time 5.

http://www.geeksforgeeks.org/find-the-point-where-maximum-intervals-overlap/
"""


def solution1(arrl, exit):
    """
    Time complexity: O(k*n) where k is average interval length and n is number of
    intervals.
    >>> solution1([1, 2, 9, 5, 5], [4, 5, 12, 9, 12])
    5
    """
    min_arrl, max_exit = min(arrl), max(exit)

    # Allocate count array
    count = []
    for i in range(max_exit - min_arrl + 1):
        count.append(0)

    # Traverse all intervals and increment count accordingly
    for interval in zip(arrl, exit):
        for i in range(interval[0], interval[1]+1):
            count[i-min_arrl] += 1  # offset min_arr

    # Find max count
    maxidx = 0
    for i in range(len(count)):
        if count[i] > count[maxidx]:
            maxidx = i

    return min_arrl + maxidx
    # Alternatively:
    #return min_arrl+next(i for i, c in enumerate(count) if c == max(count))


def solution2(arrl, exit):
    """
    Time complexity: O(nlog(n)) for the sorting
    Traverse both arrival and exit lists in parallel using merge portion of mergesort
    and keep track of max number of overlap.
    >>> solution2([1, 2, 9, 5, 5], [4, 5, 12, 9, 12])
    5
    """
    arrl.sort()
    exit.sort()

    # 1, 2, 5, 5, 9
    # 4, 5, 9, 12, 12

    i, j = 0, 0
    count, maxcount = 0, 0
    res = 0
    while i < len(arrl) and j < len(exit):
        if arrl[i] <= exit[j]:
            count += 1
            if count > maxcount:
                maxcount = count
                res = arrl[i]
            i += 1
        else:
            count -= 1
            j += 1

    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
