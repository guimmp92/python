#!/usr/bin/python

"""
Count the number of words in a string.

https://github.com/juchem/prep/blob/master/exercises.md

Slightly different problem:

Implement a document scanning engine that receives a text document doc and returns a
list of all unique words in it and their number of occurrences, sorted by the number of
occurrences in descending order.

Example:
for doc: "practice makes perfect. get perfect by practice. just practice!"
the engine returns the list: {practice: 3, perfect: 2,  makes: 1, get: 1, by: 1, just: 1}

The engine should ignore punctuation and white-spaces. Find the minimal runtime
complexity and analyze it.

https://www.pramp.com/question/W5EJq2Jld3t2ny9jyZXG
"""

from collections import Counter, defaultdict
from operator import itemgetter


def count_words_pythonic(s):
    """
    >>> count_words_pythonic("Count the number of words in a string.  ")
    8
    """
    count = Counter(s.strip().split())
    return len(count)


def count_words(s):
    """
    >>> count_words("Count the number of words in a string.  ")
    8
    """
    count = 0
    letters = "abcdefghijklmnopqrstuvwxyz."

    on_word = False
    for c in s.strip().lower():
        if c in letters and not on_word:
            on_word = True
            continue
        if c == ' ' and on_word:
            on_word = False
            count += 1
    count += 1  # account for the last word

    return count


def pramp(doc):
    """
    >>> pramp("Count the number, of words in a string. count the number words!! count?")
    [('count', 3), ('number', 2), ('words', 2), ('the', 2), ('a', 1), ('string', 1), ('of', 1), ('in', 1)]
    """
    punctuation = ",.:;?!"
    words = doc.strip().split()
    words = [w.strip(punctuation).lower() for w in words]
    """
    # Alternate implementation w/o using str.strip:
    clean_words = []
    for w in words:
        w = w.lower()
        i, j = 0, len(w)-1
        while i < len(w) and w[i] in punctuation:
            i += 1
        while j > 0 and w[j] in punctuation:
            j -= 1
        clean_words.append(w[i:j+1])
    """

    count = defaultdict(int)
    for word in words:
        count[word] += 1

    return sorted(count.items(), key=itemgetter(1), reverse=True)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
