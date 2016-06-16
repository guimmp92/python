#!/usr/bin/python

"""
Given two strings string1 and string2, find the smallest substring in string1 containing
all characters of string2 efficiently.

http://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/
"""

def _debug(arr):
    for i, c in enumerate(arr):
        if c > 0:
            print chr(i), c
    print


def is_valid(window, count_needed):
    return all([window[i] >= c for i, c in enumerate(count_needed) if c > 0])


def solution(arr, text):
    """
    Time complexity: O(n)
    >>> solution(['t', 'i', 's', 't'], "this is a test string")
    't stri'
    """
    res = ""

    count_needed = [0] * 256
    for c in arr:
        count_needed[ord(c)] += 1


    minsofar = len(text)
    lo = 0
    window = [0] * 256
    for hi in range(len(text)):
        # Add new character to window
        window[ord(text[hi])] += 1

        # Remove trailing characters from window and check if we have a new smallest
        while is_valid(window, count_needed):
            if hi-lo+1 < minsofar:
                minsofar = hi-lo+1
                res = text[lo:hi+1]
            window[ord(text[lo])] -= 1
            lo += 1

    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
