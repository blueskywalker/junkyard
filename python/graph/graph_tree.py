from collections import deque
import itertools

class Node(object):

    def __init__(self, value):
        self.value=value
        self.children=[]

    def add(self, value):
        v=Node(value)
        self.children.append(v)
        return v

    def __str__(self):
        return str(self.value)

    def show(self):
        print(self.value, end=",")


class Tree(object):
    def __init__(self):
        self.root=None

    def _add(self, node, value):
        if node is None:
            return Node(value)

        return node.add(value)

    def _height(self, node):
        if node is None:
            return 0

        if len(node.children) == 0:
            return 1

        return max(map(self.height, node.children)) + 1

    def __height(self, node):
        q = deque()
        height = 0
        q.append(node)

        while True:
            node_count = len(q)
            if node_count == 0:
                return height

            height += 1

            while node_count > 0:
                n = q.popleft()
                for child in n.children:
                    q.append(child)
                node_count -= 1

    def height(self, node, stack=0):
        if node is None:
            return stack

        if len(node.children) == 0:
            return stack + 1

        return max([self.height(c, stack+1) for c in node.children]) + 1

    def max_height(self):
        if self.root is None:
            return 0
        return self.height(self.root)

    def diameter(self):
        def calc_diameter(node):
            if node is None:
                return 0

            if len(node.children) == 0:
                return 1

            distance = sum(sorted(map(self.height, node.children), reverse=True)[:2])
            max_diameter = max(map(calc_diameter, node.children))
            return max(distance, max_diameter )

        return calc_diameter(self.root)


    def show(self):
        queue = deque()
        queue.append(self.root)
        queue.append('\n')

        while len(queue) > 0:
            node = queue.popleft()
            if isinstance(node, Node):
                print(node.value, end=',')
                for child in node.children:
                    queue.append(child)

            if isinstance(node, str):
                print()
                if len(queue) > 0:
                    queue.append('\n')

class graph(object):

    def __init__(self):
        self.vertics={}
        self.diameter=0

    def _add(self, v1, v2):
        if v1 in self.vertics:
            self.vertics[v1].add(v2)
        else:
            self.vertics[v1]=set([v2])

    def add(self, v1, v2):
        self._add(v1, v2)
        self._add(v2, v1)

    def from_edges(self, edges):
        for e in edges:
            self.add(*e)

    def show(self):
        for k in self.vertics:
            print(k, self.vertics[k])

    def travel(self):
        # for s in self.vertics:
        #     track=[]
        #     self.dfs(s, track)
        #     print()
        # print()

        for s in self.vertics:
            self.bfs(s)
            break

    def dfs(self, start, track=[]):
        v = start
        track.append(v)
        for n in self.vertics[v]:
            if n in track:
                continue
            print("{v}->{n}".format(**locals()), end=',')
            self.dfs(n, track)
        track.pop()

    def bfs(self, start):
        v = start
        track = set()
        queue = deque()
        queue.append(v)
        diameter = 0
        while len(queue) > 0:
            v = queue.popleft()
            track.add(v)
            diameter += 1
            for n in self.vertics[v]:
                print("{v}->{n}".format(**locals()), end=',')
                if n in track:
                    continue
                queue.append(n)
            print()
        return diameter

    def toTree(self, start):
        out = Tree()


        # DFS
        # def build_tree(node, track=[]):
        #     v = node.value
        #     track.append(v)
        #     for n in self.vertics[v]:
        #         if n in track:
        #             continue
        #         child=node.add(n)
        #         build_tree(child, track)
        #     track.pop()
        #
        # out.root = Node(start)
        # build_tree(out.root)

        def build_tree(node):
            track = set()
            queue = deque()
            queue.append(node)
            track.add(node.value)

            while len(queue) > 0:
                node = queue.popleft()
                for n in self.vertics[node.value]:
                    if n in track:
                        continue
                    child = node.add(n)
                    queue.append(child)
                    track.add(child.value)

        out.root = Node(start)
        build_tree(out.root)
        return out


    def show_vertics(self):
        print(self.vertics.keys())

    def all_pairs(self):
        return itertools.combinations(self.vertics.keys(),2)


    def distance(self, a, b):
        q = deque()
        q.append(a)
        track=set()
        d = 0
        while len(q) > 0:
            v = q.popleft()
            for n in self.vertics[v]:
                if n == b:
                    return d

                if n in track:
                    continue


def treeDiameter(n, tree):
    if len(tree) == 0:
        return 0
    g = graph()
    g.from_edges(tree)
    g.travel()

if __name__ == "__main__":
    import json
    with open('/tmp/test-11.json') as f:
        test_data = json.load(f)
        n = test_data['input']['n']
        data=test_data['input']['tree']
        print(n, treeDiameter(n, data))


    # n =40
    # tree = [[28, 26],
    #        [26, 18],
    #        [18, 10],
    #        [10, 3],
    #        [3, 32],
    #        [32, 22],
    #        [22, 14],
    #        [14, 38],
    #        [38, 13],
    #        [13, 25],
    #        [25, 19],
    #        [19, 12],
    #        [12, 6],
    #        [6, 34],
    #        [34, 23],
    #        [23, 1],
    #        [1, 20],
    #        [20, 9],
    #        [9, 36],
    #        [36, 17],
    #        [17, 16],
    #        [16, 5],
    #        [5, 2],
    #        [2, 39],
    #        [39, 30],
    #        [30, 0],
    #        [0, 21],
    #        [21, 24],
    #        [24, 8],
    #        [8, 27],
    #        [27, 33],
    #        [33, 15],
    #        [15, 7],
    #        [7, 37],
    #        [37, 31],
    #        [31, 29],
    #        [29, 4],
    #        [4, 35],
    #        [35, 11]]
    #
    # g = graph()
    # for e in tree:
    #     g.add(*e)
    #
    # for e in tree:
    #     t= g.toTree(e[0])
    #     print(e[0], t.max_height())

