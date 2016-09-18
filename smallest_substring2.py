#!/usr/bin/python
# vim: foldlevel=0

"""
Given two strings string1 and string2, find the smallest substring in string1 containing
all characters of string2 efficiently.

http://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/
"""


def solution(arr, text):
    """
    Time complexity: O(n)
    >>> solution(['t', 'i', 's', 't'], "this is a test string")
    't stri'
    """
    def _has_all_chars(needed, tracker):
        return all(x <= y for x, y in zip(needed, tracker))

    res = text

    count_needed = [0] * 256
    for c in arr:
        count_needed[ord(c)] += 1

    lo = 0
    window = [0] * 256
    for hi in range(len(text)):
        # Add new character to window
        window[ord(text[hi])] += 1

        # Remove trailing characters from window and check if we have a new smallest
        while _has_all_chars(count_needed, window):
            if hi-lo+1 < len(res):
                res = text[lo:hi+1]
            window[ord(text[lo])] -= 1
            lo += 1

    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
