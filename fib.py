#!/usr/bin/python

"""
Implement a function which returns fib(N) where:
- fib(0) = 1
- fib(1) = 1
- and fib(N) = fib(N-1) + fib(N-2)
"""









































def fib_recursive(N):
    """
    Time complexity: O(2^n)
    >>> fib_recursive(2)
    2
    >>> fib_recursive(4)
    5
    >>> fib_recursive(12)
    233
    """
    if N == 0 or N == 1:
        return 1
    return fib_recursive(N-1) + fib_recursive(N-2)


def fib_dp(N):
    """
    Time complexity: O(n)
    >>> fib_dp(2)
    2
    >>> fib_dp(4)
    5
    >>> fib_dp(12)
    233
    """
    memo = [0] * (N+1)
    memo[0] = 1
    memo[1] = 1

    for i in range(2, N+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[N]


memo = dict()
memo[0] = 1
memo[1] = 1


def fib_dp_top_down(N):
    """
    Time complexity: O(n)
    >>> fib_dp_top_down(2)
    2
    >>> fib_dp_top_down(4)
    5
    >>> fib_dp_top_down(12)
    233
    """
    if not memo.get(N):
        memo[N] = fib_dp_top_down(N-1) + fib_dp_top_down(N-2)
    return memo[N]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
