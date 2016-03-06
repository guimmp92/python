#!/usr/bin/python

"""
Find the k most frequent elements i) in an array and ii) in a stream.
"""
from collections import defaultdict


def k_modes_array(arr, k):
    """
    Implementation with an array to keep track of most frequent elements.
    >>> k_modes_array([3, 2, 9, 4, 5, 1, 2, 3, 5, 7, 9, 8, 9, 0, 9, 8, 7, 9, 5, 6, 2, 3, 4, 6, 5, 4, 5, 6, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 3)
    [0, 5, 9]
    """
    most_frequent = list()
    cur_min = None
    counter = defaultdict(int)
    for i in range(len(arr)):
        x = arr[i]
        counter[x] += 1
        if x not in most_frequent:
            if len(most_frequent) < k:
                most_frequent.append(x)
            elif counter[x] > cur_min:
                to_del = filter(lambda y: counter[y] == cur_min, most_frequent)[0]
                most_frequent.remove(to_del)
                most_frequent.append(x)
        idx = reduce(lambda x, y: x if counter[x] <= counter[y] else y, most_frequent)
        cur_min = counter[idx]
    return sorted(most_frequent)


def heappush(heap, x):
    cur = len(heap)
    heap.append(x)
    parent = cur//2
    while parent > 0 and heap[cur] < heap[parent]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        parent, cur = parent//2, parent


def heappop(heap):
    # Pop root and replace with last element.
    root = heap[1]
    heap[1] = heap[len(heap)-1]
    heap.pop()

    # Heapify.
    def _min_child(heap, child1, child2):
        if child2 > len(heap)-1:
            if child1 > len(heap)-1:
                return
            else:
                return child1
        if heap[child1] <= heap[child2]:
            return child1
        else:
            return child2

    cur = 1
    children = 2*cur, 2*cur+1
    min_child = _min_child(heap, *children)
    while min_child and heap[cur] > heap[min_child]:
        heap[cur], heap[min_child] = heap[min_child], heap[cur]
        cur, children = min_child, (2*min_child, 2*min_child+1)
        min_child = _min_child(heap, *children)

    return root


def k_modes_array2(arr, k):
    """
    Alternate implementation with a min-heap to keep track of most frequent elements.
    >>> k_modes_array([3, 2, 9, 4, 5, 1, 2, 3, 5, 7, 9, 8, 9, 0, 9, 8, 7, 9, 5, 6, 2, 3, 4, 6, 5, 4, 5, 6, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 3)
    [0, 5, 9]
    """
    most_frequent = list()  # min-heap
    most_frequent.append(0)  # 1-indexed
    counter = defaultdict(int)
    for i in range(len(arr)):
        x = arr[i]
        counter[x] += 1
        if x not in most_frequent[1:]:
            if len(most_frequent)-1 < k:
                heappush(most_frequent, x)
            elif counter[x] > most_frequent[1]:
                heappop(most_frequent)
                heappush(most_frequent, x)
    return sorted(most_frequent[1:])


arr = [9, 5, 3, 5, 9, 8, 9, 0, 9, 8, 9, 5, 6, 2, 3, 5, 4, 5, 6, 0, 1, 0, 0, 0, 0, 0, 0]
stream = (x for x in arr)


def k_modes_stream(stream, k):
    """
    The above solutions for a fixed input array can be generalized for a stream.
    """
    most_frequent = list()
    cur_min = None
    counter = defaultdict(int)
    x = stream.next()
    while x:
        counter[x] += 1
        if x not in most_frequent:
            if len(most_frequent) < k:
                most_frequent.append(x)
            elif counter[x] > cur_min:
                to_del = filter(lambda y: counter[y] == cur_min, most_frequent)[0]
                most_frequent.remove(to_del)
                most_frequent.append(x)
        idx = reduce(lambda x, y: x if counter[x] <= counter[y] else y, most_frequent)
        cur_min = counter[idx]
        x = stream.next()
    return sorted(most_frequent)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
