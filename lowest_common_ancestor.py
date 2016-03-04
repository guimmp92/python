#!/usr/bin/python

"""
https://www.codeeval.com/open_challenges/11/

"""
import sys


def build_tree():
    return [30, [[8, [[3, []], [20, [[10, []], [29, []]]]]], [52, []]]]


def traverse(node, x, y):
    value, children = node
    if x <= value <= y:
        return value
    if value > y:
        return traverse(children[0], x, y)
    if value < x:
        return traverse(children[1], x, y)


def solution(root, x, y):
    """
    >>> solution(8, 52)
    30
    >>> solution(3, 29)
    8
    """
    x, y = min(x, y), max(x, y)
    return traverse(root, x, y)


def main():
    tree = build_tree()
    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = [int(i) for i in line.split(' ')]
            print solution(tree, *line)


if __name__ == "__main__":
    main()
