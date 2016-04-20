#!/usr/bin/python

"""
Given two strings str1 and str2 and below operations that can performed on str1.
Find minimum number of edits (operations) required to convert 'str1' into 'str2'.
- Insert
- Remove
- Replace
All of the above operations are of equal cost.

http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
https://web.stanford.edu/class/cs124/lec/med.pdf
"""


def edit_distance(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return edit_distance(str1, str2, m-1, n-1)
    return 1 + min(edit_distance(str1, str2, m, n-1),    # insert
                   edit_distance(str1, str2, m-1, n),    # remove
                   edit_distance(str1, str2, m-1, n-1))  # replace


def recursive(str1, str2):
    """
    Time complexity: O(3^m)
    >>> recursive("geek", "gesek")
    1
    >>> recursive("cat", "cut")
    1
    >>> recursive("cat", "put")
    2
    >>> recursive("sunday", "saturday")
    3
    """
    return edit_distance(str1, str2, len(str1), len(str2))


def dp(str1, str2):
    """
    Bottom-up dynamic programming.
    Time complexity: O(m*n)
    Space complexity: O(m*n)
    >>> dp("geek", "gesek")
    1
    >>> dp("cat", "cut")
    1
    >>> dp("sunday", "saturday")
    3
    """
    # Memoized computations
    memo = [[0 for j in range(len(str2))] for i in range(len(str1))]

    # Base cases
    for i in range(len(str1)):
        memo[i][0] = i
    for i in range(len(str2)):
        memo[0][i] = i

    # Build up from base cases (bottom-up dp)
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                memo[i][j] = memo[i-1][j-1]
            else:
                memo[i][j] = 1 + min(memo[i][j-1], memo[i-1][j], memo[i-1][j-1])

    return memo[len(str1)-1][len(str2)-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
