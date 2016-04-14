#!/usr/bin/python

"""
Find the longest substring with k unique characters.

Example: If the string is "aabbccdd", if K is 1, the longest substring can be "aa".
If K is 2, the longest substring can be "aabb".
If K is 3, the longest substring can be "aabbcc".

http://blog.gainlo.co/index.php/2016/04/12/find-the-longest-substring-with-k-unique-characters/
"""
from collections import deque


def solution(text, k):
    """
    >>> solution("aabbccdd", 1)
    'aa'
    >>> solution("aabbccdd", 2)
    'aabb'
    >>> solution("aabbccdd", 3)
    'aabbcc'
    """
    max_substring = ""
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
                if i - start_index + 1 > len(max_substring):
                    max_substring = text[start_index:i+1]
            else:
                char = queue.pop()
                del indices[char]
    return max_substring


if __name__ == "__main__":
    import doctest
    doctest.testmod()
