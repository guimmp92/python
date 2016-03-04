#!/usr/bin/python

"""
Reverse the words in a sentence, i.e. My name is Chris becomes Chris is name My.
Optimize for time and space.
http://nbl.cewit.stonybrook.edu/algowiki/index.php/Data-structures-TADM2E-2
"""


def reverse_string(s):
    """ Python style. """
    return s[::-1]


def reverse_string2(s):
    """ C style. """
    s = list(s)
    i, j = 0, len(s)-1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return "".join(s)

print reverse_string("hello")
print reverse_string2("hello")


def reverse_sentence(s):
    s = reverse_string(s)
    words = [reverse_string(w) for w in s.split(" ")]
    return " ".join(words)

print reverse_sentence("My name is Chris")
