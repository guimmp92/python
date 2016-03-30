#!/usr/bin/python

"""
Given two integers 'n' and 'sum', find count of all n digit numbers with sum of digits
as 'sum'. Leading 0's are not counted as digits. Return -1 if not possible.

http://www.geeksforgeeks.org/count-of-n-digit-numbers-whose-sum-of-digits-equals-to-given-sum/
"""


def digits_sum(n, target_sum, cur):
    if n == 0:
        if target_sum == 0 and cur[0] != 0:
            return 1
        else:
            return 0
    count = 0
    for i in range(10):
        if i <= target_sum:
            cur.append(i)
            count += digits_sum(n-1, target_sum-i, cur)
            cur.pop()
    return count


def recursive(n, target_sum):
    """
    >>> recursive(2, 2)
    2
    >>> recursive(2, 5)
    5
    >>> recursive(3, 6)
    21
    """
    print digits_sum(n, target_sum, [])


def digits_sum_memo(n, target_sum, cur, memo):
    if n == 0:
        if target_sum == 0 and cur[0] != 0:
            return 1
        else:
            return 0

    if memo.get((n, target_sum)):
        return memo[(n, target_sum)]

    count = 0
    for i in range(10):
        if i <= target_sum:
            cur.append(i)
            count += digits_sum_memo(n-1, target_sum-i, cur, memo)
            cur.pop()

    memo[(n, target_sum)] = count
    return count


def dp(n, target_sum):
    """
    >>> dp(2, 2)
    2
    >>> dp(2, 5)
    5
    >>> dp(3, 6)
    21
    """
    memo = dict()
    print digits_sum_memo(n, target_sum, [], memo)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
