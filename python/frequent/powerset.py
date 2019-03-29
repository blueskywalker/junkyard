from typing import List


def powerset(src: List) -> List[List]:
    if len(src) == 0:
        return [[]]
    pivot = src[0]
    prev = powerset(src[1:])
    prev.extend([[pivot] + item for item in powerset(src[1:])])
    return prev

if __name__ == '__main__':
    data = range(3)
    print(powerset(data))
