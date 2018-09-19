


class Node(object):
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return "{data}".format(**self.__dict__)

class DoubleLinkedList(object):
    def __init__(self):
        self.head=None
        self.tail=None

    def _add_first(self, node):
        self.head = node
        self.tail = node

    def _insert(self, prev, node):
        if prev.next is not None:
            prev.next.prev = node
        node.next = prev.next
        prev.next = node
        node.prev = prev
        return node

    def _push(self, node):
        if self.head is None:
            self._add_first(node)
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def push(self, value):
        self._push(Node(data=value))


    def _add(self, node):
        if self.tail is None:
            self._add_first(node)
        else:
            self.tail = self._insert(self.tail, node)

    def add(self, value):
        self._add(Node(data=value))


    def show(self):
        node = self.head
        print('{head}:{tail}'.format(**self.__dict__))
        while node is not None:
            print(node.data, end= ' ')
            node = node.next
        print()

    def _pop(self):
        node = self.head
        self.head = node.next
        self.head.prev = None
        return node

    def pop(self):
        return self._pop().data


    def _remove(self):
        node = self.tail
        self.tail = node.prev
        self.tail.next = None
        return node

    def remove(self):
        return self._remove().data

    def delete(self, node):
        prev_node = node.prev
        next_node = node.next

        if prev_node is not None:
            prev_node.next = next_node
        else:
            self.head = next_node

        if next_node is not None:
            next_node.prev = prev_node
        else:
            self.tail = prev_node
        node.prev = None
        node.next = None
        return node

# def main():
#     data = [ x for x in range(30) ]
#
#     dlist = DoubleLinkedList()
#
#     for item in data:
#         dlist.add(item)
#
#     dlist.show()
#
#     for _ in range(10):
#         dlist.remove()
#
#     dlist.show()
#
# if __name__ == '__main__':
#     main()