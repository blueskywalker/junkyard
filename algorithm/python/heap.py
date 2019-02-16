import random


class Heap(object):

    def __init__(self, size=None, cmp=None):
        self.heap = []
        self.cmp_func = cmp
        self.size = size
        if self.cmp_func is None:
            self.cmp_func = lambda x, y : x - y

    def _get_parent(self, index):
        return (index-1)//2

    def _swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]

    def _heap_up(self):
        current = len(self.heap)-1
        while 0 < current:
            parent = self._get_parent(current)
            if self.cmp_func(self.heap[current], self.heap[parent]) > 0:
                self._swap(current, parent)
                current = parent
            else:
                break

    def _get_max_child(self, index):
        base = index * 2
        left, right  =  base+1, base+2

        if left < len(self.heap) and right < len(self.heap):
            if self.cmp_func(self.heap[left], self.heap[right]) >= 0:
                return left
            else:
                return right

        if left < len(self.heap):
            return left

        return -1

    def _has_children(self, current):
        return (current+1)*2 <= len(self.heap)

    def _heap_down(self):
        current = 0
        while self._has_children(current):
            child = self._get_max_child(current)
            if self.cmp_func(self.heap[child], self.heap[current]) > 0:
                self._swap(child, current)
                current = child
            else:
                break

    def _add(self, value):
        self.heap.append(value)
        self._heap_up()

    def add(self, value):
        if self.size is not None and self.size == len(self.heap):
            if self.cmp_func(value, self.peek()) < 0:
                root = self.pop()
                self._add(value)
                return root
        else:
            return self._add(value)

    def pop(self):
        value = self.heap[0]
        self._swap(0, len(self.heap)-1)
        self.heap.pop()
        self._heap_down()
        return value

    def peek(self):
        return self.heap[0]



def gen_data():
    data_size = 20
    number_range = data_size * 10
    data=[]
    for _ in range(data_size):
        data.append(random.randint(0, number_range))

    return data

# data = gen_data()
# print(data)
data = [154, 87, 139, 104, 184, 43, 150, 25, 85, 170, 53, 141, 55, 43, 66, 112, 186, 91, 144, 110]

cmp = lambda x, y: y-x
heap = Heap(size=5, cmp=cmp)

for item in data:
    heap.add(item)

print(sorted(heap.heap, reverse=True))
print(sorted(data, reverse=True)[:5])