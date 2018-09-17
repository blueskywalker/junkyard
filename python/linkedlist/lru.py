import sys

sys.path.append(".")

from double_linked_list import DoubleLinkedList, Node
import random

class LRUNode(Node):
    def __init__(self, data=None, key=str):
        super().__init__(data)
        self.key=key

    def key_value(self):
        return self.key(self.data)


class LRUCache(object):

    def __init__(self, max_size=10):
        self.max = max_size
        self.htable = dict()
        self.dlist = DoubleLinkedList()

    def _get(self, new_node):
        if new_node.key_value() in self.htable:
            node = self.htable[new_node.key_value()]
            node = self.dlist.delete(node)
            self.dlist._push(node)
            return node
        else:
            if len(self.htable) == self.max:
                node = self.dlist._remove()
                del self.htable[node.key_value()]

            self.htable[new_node.key_value()] = new_node
            self.dlist._push(new_node)
            return new_node

    def get(self, data=None, key=str):
        return self._get(LRUNode(data=data, key=key)).data


    def show(self):
        print('{head}:{tail}'.format(**self.dlist.__dict__))
        node = self.dlist.head
        while node is not None:
            print(node.data, end=' ')
            node = node.next
        print()

def main():
    test_data = [ random.randint(1, 20) for _ in range(30) ]

    cache = LRUCache(max_size=10)

    for item in test_data:
        print("IN {}".format(cache.get(data=item)))


    cache.show()

if __name__ == '__main__':
    main()