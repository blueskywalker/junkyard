
class CacheValue(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Node(object):
    def __init__(self, value: CacheValue, prevN=None, nextN=None):
        self.value = value
        self.prev = prevN
        self.next = nextN

    def __repr__(self):
        return 'Node(value={value})'.format(value=self.value)
    

class DLL(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def _add(self, node: Node, newNode: Node):
        if node is None:
            return newNode
        nextNode = node.next
        if newNode:
            newNode.prev = newNode
        newNode.prev = node            
        node.next = newNode
        return newNode

    def add(self, node: Node):
        self.tail = self._add(self.tail, node)
        if self.head is None:
            self.head = self.tail
    
    def remove(self):
        node = self.head
        self.head = self.delete(self.head)
        if self.head is None:
            self.tail = self.head
        return node

    def delete(self, node):
        if node is None:
            return None
        
        nextNode = node.next
        if node.prev:
            node.prev.next = nextNode
        if nextNode:
            nextNode.prev = node.prev
        node.prev = None
        node.next = None
        return nextNode

class LRU(object):
    def __init__(self, capacity=10):
        self.data = dict()
        self.lru = DLL()
        self.size = capacity

    def set(self, value: CacheValue):
        if len(self.data) == self.size and value.key not in self.data:
            node = self.lru.remove()
            del self.data[node.value.key]
        
        if value.key in self.data:
            oldNode = self.data[value.key]
            self.lru.delete(oldNode)

        node = Node(value)
        self.data[value.key] = node
        self.lru.add(node)

    def get(self, key):
        if key in self.data:
            node = self.data[key]
            self.lru.delete(node)
            self.lru.add(node)
            return node.value.value        
        return None


if __name__ == "__main__":
    data = [ 1, 3, 5, 7, 9]

    cache = LRU(5)

    for item in data:
        cache.set(CacheValue(item,item))

    print(cache.get(5))
    cache.set(CacheValue(10, 10))
    print(cache.get(1))