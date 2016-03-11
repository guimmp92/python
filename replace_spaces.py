#!/usr/bin/python

"""
Write a function to replace all spaces in a text string with '%20'.
"""


def solution1(text):
    """
    Multi-pass solution O(n).

    >>> solution1("let's replace all whitespaces with %20")
    "let's%20replace%20all%20whitespaces%20with%20%20"
    """
    # Count space characters in input string
    text = list(text)
    old_len = len(text)
    space_count = sum(map(lambda x: 1 if x == ' ' else 0, text))

    # Expand input string to accomodate for %20
    for i in range(space_count * 2):
        text.append("_")  # dummy character

    # Traverse the string in reverse and replace characters accordingly
    idx = len(text)-1
    for i in range(old_len-1, -1, -1):
        if text[i] == ' ':
            text[idx] = '0'
            text[idx-1] = '2'
            text[idx-2] = '%'
            idx -= 3
        else:
            text[idx] = text[i]
            idx -= 1

    return "".join(text)


def solution2(text):
    """
    Single pass w/ queue solution O(n).

    >>> solution1("let's replace all whitespaces with %20")
    "let's%20replace%20all%20whitespaces%20with%20%20"
    """
    from collections import dequeue
    text = list(text)
    queue = dequeue()
    old_len, idx = len(text), 0
    for i in range(old_len):
        if text[i] == ' ':
            queue.appendleft('%')
            queue.appendleft('2')
            queue.appendleft('0')
        else:
            queue.appendleft(text[i])
        text[idx] = queue.pop()
        idx += 1
    while queue:
        text.append(queue.pop())
    return "".join(text)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
