
from collections import deque

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
        self.node=None

    def _add(self, node, value):
        if node is None:
            return Node(value)

        return node.add(value)

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
            self.node = self.root
        else:
            self.node = self.node.add(value)

        return self.node

    def height(self, node):

        if node is None:
            return 0

        q = deque()
        h = 0

        q.append(node)

        while True:

            count = len(q)
            if count == 0:
                return h

            h += 1

            while count > 0:
                v = q.popleft()
                for c in v.children:
                    q.append(c)
                count -= 1

        return h

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


from functools import reduce

def len_list(data):
    return reduce(lambda d, n: d+1, data, 0)

def main():
    nary = Tree()
    data = [ x for x in range(1000) ]
    for item in data:
        nary.add(item)

    print(nary.diameter())

if __name__ == '__main__':
    main()