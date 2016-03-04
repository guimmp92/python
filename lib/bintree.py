import random


def randbintree(size=10):
    root_key = random.randint(20, 30)
    added = []
    added.append(root_key)
    tree = BinTree(root_key)
    for i in range(size-1):
        while True:
            new_key = random.randint(0, 50)
            if new_key not in added:
                added.append(new_key)
                tree.insert(new_key)
                break
    return tree


class BinTree(object):
    """ Implementation of a binary tree as nodes and references. """
    def __init__(self, root):
        if isinstance(root, Node):
            self.root = root
        else:
            self.root = Node(root)
        self.size = 1

    def find(self, key):
        """ Find a key in the binary tree. Return None if not found. """
        cur = self.root
        while cur:
            if cur.key == key:
                return cur
            if cur.key < key:
                cur = cur.right
            else:
                cur = cur.left

    def find_min(self):
        # Follow the left references.
        cur = self.root
        while cur:
            if cur.left is None:
                return cur.key
            cur = cur.left

    def insert(self, key):
        new_node = None
        cur = self.root
        parent = None  # we need to keep track of the parent to do the final insertion
        while cur:
            if cur.key == key:
                raise KeyError("Key already exists {0}".format(key))
            parent = cur
            if cur.key < key:
                cur = cur.right
            else:
                cur = cur.left

        new_node = Node(key)
        if parent.key < key:
            parent.right = new_node
        else:
            parent.left = new_node
        self.size += 1

        return new_node

    def remove(self, key):
        """ Noop - too many cases to handle. """
        raise RuntimeError("Not implemented")

    def _print(self, node):
        """ In-order traversal of the tree. """
        if node is None:
            return
        self._print(node.left)
        print node.key
        self._print(node.right)

    def print_tree(self):
        """ Print binary tree in ascending order. """
        self._print(self.root)

    def _copy(self, source):
        if source is None:
            return
        target = Node(source.key)
        target.left = self._copy(source.left)
        target.right = self._copy(source.right)
        return target

    def duplicate(self):
        """ Could also use the copy.deepcopy() function. """
        root = self._copy(self.root)
        tree = BinTree(root)
        tree.size = self.size
        return tree


class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
