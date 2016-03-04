
class Graph(object):
    def __init__(self):
        self.vertices = {}  # use dict instead of list
        self.num_vertices = 0

    def add_vertex(self, key):
        """ If vertex already exists, return it. Otherwise create new vertex.  """
        if not self.vertices.get(key):
            self.vertices[key] = Vertex(key)
            self.num_vertices += 1
        return self.vertices[key]

    def get_vertex(self, key):
        return self.vertices.get(key, None)

class Vertex(object):
    WHITE = 'white'  # undiscovered
    GRAY = 'gray'  # discovered, e.g. all vertices in the BFS queue are gray
    BLACK = 'black'  # processed
    colors = (WHITE, GRAY, BLACK)

    def __init__(self, key):
        self.key = key
        self.neighbors = {}  # use dict instead of list to hold weight, use list if no weights
        self.color = self.WHITE  # used during traversal to avoid cycles
        self.parent = None  # used during traversal

    def add_neighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight
