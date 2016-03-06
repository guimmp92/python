"""
Implementation of a binary heap using level ordering. Assuming 1-index:
- Children of k are at position 2k and 2k+1
- Parent of k is at position k/2

http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html
"""


class BinHeap(object):
    def __init__(self):
        self.data = [0]  # start at index 1
        self.size = 0

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _bubbleup(self, idx):
        parent = idx//2
        while parent > 0 and self.data[idx] < self.data[parent]:
            self._swap(idx, parent)
            idx, parent = parent, parent//2

    def insert(self, elem):
        self.data.append(elem)
        self.size += 1
        self._bubbleup(self.size)

    def getmin(self):
        return self.data[1]

    def _minchild(self, idx):
        if 2*idx+1 > self.size:
            if 2*idx > self.size:
                return
            else:
                return 2*idx
        if self.data[2*idx] <= self.data[2*idx+1]:
            return 2*idx
        else:
            return 2*idx+1

    def _bubbledown(self, idx):
        min_child = self._minchild(idx)
        if not min_child:
            return
        if self.data[idx] > self.data[min_child]:
            if self.data[2*idx] <= self.data[2*idx+1]:
                self._swap(idx, 2*idx)
                self._bubbledown(2*idx)
            else:
                self._swap(idx, 2*idx+1)
                self._bubbledown(2*idx+1)

    def delmin(self):
        if self.size <= 0:
          return

        min_elem = self.data[1]

        self.data[1] = self.data[self.size]
        del self.data[self.size]
        self.size -= 1

        self._bubbledown(1)

        return min_elem
