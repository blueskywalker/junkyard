
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MemCache(object):
    def __init__(self, size=10*1024*1024):
        self.size = size
        self.current = 0
        self.htable = dict()
        self.lru = list()

    def set(self, key, value):

        while self.current + len(value) > self.size:
            node = self.lru[0]
            self.lru.remove(node)
            del self.htable[node.key]
            self.current = self.current - len(node.value)

        if key in self.htable:
            old_node = self.htable[key]
            self.lru.remove(old_node)
            self.current = self.current - len(old_node.value)

        node = Node(key, value)
        self.lru.append(node)
        self.htable[key] = node
        self.current = self.current + len(value)
        
    def get(self, key):
        if key in self.htable:
            node = self.htable[key]
            self.lru.remove(node)
            self.lru.append(node)
            return node.value

        return None


if __name__ == '__main__':
    cache = MemCache(size=20)

    data = [ ('a', 'a' * 10 ), ('b', 'b' * 10), ('c', 'c' * 10) ]

    for k, v in data:
        cache.set(k,v)

    print(cache.get('a'))
    print(cache.get('b'))
    print(cache.get('c'))
