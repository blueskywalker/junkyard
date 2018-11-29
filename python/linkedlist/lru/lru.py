import sys

from double import DoubleLinkedList, Node

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

    def get(self, key_value):
        if key_value in self.htable:
            node = self.htable[key_value]
            node = self.dlist.delete(node)
            self.dlist._push(node)
            return node.data
        else:
            return None

    def _set(self, new_node):
        if new_node.key_value() in self.htable:
            old_node=self.htable[new_node.key_value()]
            self.dlist.delete(old_node) 
            del self.htable[new_node.key_value()]

        if len(self.htable) == self.max:
            node = self.dlist._remove()
            del self.htable[node.key_value()]

        self.htable[new_node.key_value()] = new_node
        self.dlist._push(new_node)
        return new_node

    def set(self, data=None, key=str):
        return self._set(LRUNode(data=data, key=key))


    def show(self):
        #print('{head}:{tail}'.format(**self.dlist.__dict__))
        node = self.dlist.head
        while node is not None:
            print(node.data)
            node = node.next
        print()



def lru_cache(max_size=128):
    def  cache_decorator(func):
        def wrapper(*args, **kwargs):
            params=str(locals())
            result = wrapper.cache.get(params)
            if result is not None:
                return result[1]
            ret_value=func(*args, **kwargs)
            wrapper.cache.set(data=(params, ret_value), key=lambda x: x[0])
            return ret_value

        wrapper.cache = LRUCache(max_size=max_size)
        return wrapper
    return cache_decorator

if __name__ == '__main__':

    import random

    def main():
        test_data = [ random.randint(1, 20) for _ in range(30) ]
        cache = LRUCache(max_size=10)

        for item in test_data:
            print("IN {}".format(cache.get(data=item)))

        cache.show()

        test(10);

    main()
