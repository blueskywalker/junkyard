from typing import Any


class SimplePriorityQ(object):

    def __init__(self, capacity: int, reverse: bool = False):
        self.capacity = capacity
        self.heap=[]
        self.reverse = reverse

    def _add(self, item: Any) -> None:
        self.heap.append(item)
        self.heap = sorted(self.heap, reverse=self.reverse)

    def _replace(self, item: Any)-> Any:
        out = self.heap.pop()
        self._add(item)
        return out

    def add(self, item: Any) -> Any:
        if len(self.heap) == self.capacity:
            if self.reverse:
                if self.heap[-1].__lt__(item):
                    return self._replace(item)
            else:
                if item.__lt__(self.heap[-1]):
                    return self._replace(item)
        else:
            return self._add(item)

    def get_items(self):
        return self.heap


def main():
    queue = SimplePriorityQ(5)
    data = [1, 11, 5, 43, 23, 22, 15, 7, 13, 33]

    for item in data:
        queue.add(item)

    print(queue.get_items())


if __name__ == '__main__':
    main()