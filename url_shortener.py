#!/usr/bin/python

"""
Design a system that takes big URLs like
"http://www.geeksforgeeks.org/count-sum-of-digits-in-numbers-from-1-to-n/" and converts
them into a short 6 character URL. It is given that URLs are stored in database and
every URL has an associated integer id. So your program should take an integer id and
generate a 6 character long URL.

A URL character can be one of the following
1) A lower case alphabet ['a' to 'z'], total 26 characters
2) An upper case alphabet ['A' to 'Z'], total 26 characters
3) A digit ['0' to '9'], total 10 characters

There are total 26 + 26 + 10 = 62 possible characters.

So the task is to convert an integer (database id) to a base 62 number where digits of
62 base are "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

http://www.geeksforgeeks.org/how-to-design-a-tiny-url-or-url-shortener/
"""


def solution(number):
    """
    >>> solution(12345)
    ('dnh', 12345)
    """

    # Convert int to base62 string.
    base62_map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    base62 = list()
    q = number
    while q:
        q, r = divmod(q, 62)
        base62.append(base62_map[r])
    base62.reverse()

    # Convert base62 string back to int.
    base10 = 0
    for d in base62:
        base10 *= 62
        if 'a' <= d <= 'z':
            base10 += ord(d) - ord('a')
        if 'A' <= d <= 'Z':
            base10 += ord(d) - ord('A') + 26
        if '0' <= d <= '9':
            base10 += ord(d) - ord('0') + 52

    return ("".join([str(c) for c in base62]), base10)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
