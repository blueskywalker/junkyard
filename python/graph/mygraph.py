

class Vertex(object):
    def __init__(self, id):
        self._id = id
        self._neighbor = set()

    def __eq__(self, other):
        return self._id == other._id

    def __hash__(self):
        return hash(self._id)


class Graph(object):

    def __init__(self):
        self.vertics = {}

    def add_vertex(v1,v2):
        if v1 in self.vertics:
            self.vertics[v1].append(Vertex(v2))
        else:
            self.vertics[v1]=[Vertex(v2)]

    def from_edge(v1, v2):
        self.add_vertex(v1, v2)
        self.add_vertex(v2, v1)

    def show_vertics():
        for k, v in self.vertics.items():
            print(k, v)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []

class Nary(object):
    def __init__(self):
        self.root = None

    def walk(self, value):
        def find(node, value):
            if node == None:
                return None    
            
            if node.value == value:
                return node
            
            for item in node.children:
                return find(item, value)
            
            return None

        return find(self.root, value)

    def build_from_graph(self, vertics):
        for v in vertics:
            neighbor = vertics[v]
            if len(neighbor) > 1:
                walk(v)

def main():
    data=[[1,3], [7,3], [5,3], [8,7], [4,1], [2,3], [9,4], [0,8], [6,8]]
    graph = Graph()
    for item in data:
        graph.from_edge(*list(item))

    graph.show_vertics()

if __name__ == "__main__":
    main()
