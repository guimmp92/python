#!/usr/bin/python

"""
Find the longest substring with k unique characters.

Example: If the string is "aabbccdd", if K is 1, the longest substring can be "aa".
If K is 2, the longest substring can be "aabb".
If K is 3, the longest substring can be "aabbcc".

http://blog.gainlo.co/index.php/2016/04/12/find-the-longest-substring-with-k-unique-characters/
"""
from collections import deque
from collections import defaultdict


def solution(text, k):
    """
    >>> solution("aabbccdd", 1)
    'aa'
    >>> solution("aabbccdd", 2)
    'aabb'
    >>> solution("aabbccdd", 3)
    'aabbcc'
    >>> solution("abacbebebe", 3)
    'cbebebe'
    >>> solution("ababebebe", 4)
    ''
    """
    longest = ""
    start = 0
    tracker = defaultdict(list)
    for i, c in enumerate(text):  # loop invariant: tracker contains k or less elements
        if len(tracker) < k:
            tracker[c].append(i)
        else:
            if c not in tracker:  # remove trailing character
                new_start = max(tracker[text[start]])
                tracker.pop(text[start])
                start = new_start+1
            tracker[c].append(i)
            if i-start+1 > len(longest):
                longest = text[start:i+1]
    return longest


def incorrect(text, k):
    """
    >>> incorrect("aabbccdd", 1)
    'aa'
    >>> incorrect("aabbccdd", 2)
    'aabb'
    >>> incorrect("aabbaccd", 3)
    'aabbacc'
    >>> incorrect("abacbebebe", 3)
    'cbebebe'
    """
    longest = ""
    queue = deque()
    indices = dict()
    for i in range(len(text)):
        if len(queue) < k:
            if text[i] not in queue:
                queue.appendleft(text[i])
                indices[text[i]] = i
        else:
            if text[i] in queue:
                start_index = indices[queue[-1]]
                if i - start_index + 1 > len(longest):
                    longest = text[start_index:i+1]
            else:
                char = queue.pop()
                del indices[char]
    return longest


if __name__ == "__main__":
    import doctest
    doctest.testmod()
