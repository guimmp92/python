import random


def randlist(size=50, upper=10):
    arr = []
    for i in range(size):
        arr.append(random.randint(0, upper))
    return arr
