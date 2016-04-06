#!/usr/bin/python

"""
Given a sorted dictionary (array of words) of an alien language, find order of
characters in the language.

For example if the given arrays is {"baa", "abcd", "abca", "cab", "cad"}, then order of
characters is 'b', 'd', 'a', 'c'.
"""
from graph import Graph, Vertex


def visit(vertex, stack):
    vertex.color = Vertex.GRAY

    for v in vertex.neighbors:
        if v.color == Vertex.WHITE:
            visit(v, stack)

    stack.append(vertex.key)


def build_graph(words):
    graph = Graph()
    for i in range(1, len(words)):
        word1 = words[i-1]
        word2 = words[i]
        j, k = 0, 0
        while j < len(word1) and k < len(word2):
            if word1[j] == word2[k]:
                j += 1
                k += 1
            else:
                v1 = graph.add_vertex(word1[j])
                v2 = graph.add_vertex(word2[k])
                v1.add_neighbor(v2)
                break
    return graph


def language_order(words):
    """
    >>> language_order(["baa", "abcd", "abca", "cab", "cad"])
    ['b', 'd', 'a', 'c']
    """
    graph = build_graph(words)

    stack = list()
    for key, vertex in graph.vertices.iteritems():
        if vertex.color == Vertex.WHITE:
            visit(vertex, stack)

    return list(reversed(stack))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
