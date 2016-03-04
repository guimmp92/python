#!/usr/bin/python

"""
https://www.codeeval.com/open_challenges/211/

Guess a wine name.
"""
import sys


def guess_wines(wines, chars):
    res = []
    for wine in wines:
        for char in chars:
            if char.lower() not in wine.lower():
                break
            wine.replace(char, '', 1)
        else:  # nobreak
            res.append(wine)
    return res


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        for line in f:
            input = line.split('|')
            wines = [w.strip() for w in input[0].split()]
            chars = [c for c in input[1].strip()]
            matches = guess_wines(wines, chars)
            if matches:
                print " ".join(matches)
            else:
                print "False"
