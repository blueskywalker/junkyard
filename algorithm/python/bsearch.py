
#import random

#data = [random.randint(0,100) for _ in range(10)]
#print(sorted(data))

data = [0, 18, 20, 28, 40, 50, 59, 60, 67, 73]

def bsearch(data, value, start=0, end=len(data)-1) :

    if start > end:
        return False

    mid = (start + end) // 2

    if data[mid] < value:
        return bsearch(data, value, mid + 1, end)
    elif data[mid] > value:
        return bsearch(data, value, start, mid - 1)

    return True

print(bsearch(data, 21))

