


class Node(object):
    def __init__(self, data=None, lnext=None):
        self.data = data
        self.next = lnext

    def __str__(self):
        return '{data}:{next}'.format(**self.__dict__)


class LinkedList(object):

    def __init__(self):
        self.head=None

    def _push(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def push(self, value):
        self._push(Node(data=value))

    def _pop(self):
        node = self.head
        self.head = node.next
        return node

    def pop(self):
        node = self._pop()
        return node.data


    def show(self):
        node = self.head

        while node is not None:
            print(node.data, end= ' ')
            node = node.next
        print()

def main():
    test_data = [ x for x in range(100) ]

    llist = LinkedList()

    for item in test_data:
        llist.push(item)

    llist.show()

    for _ in range(50):
        llist.pop()

    llist.show()
    
if __name__ == '__main__':
    main()