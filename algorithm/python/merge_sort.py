#!/usr/bin/env python
import random

def merge_sort(data):

    def split(data):
        pivot = len(data) // 2
        return data[:pivot], data[pivot:]

    def merge(left, right):
        i = 0
        j = 0
        ret = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ret.append(left[i])
                i+=1
            else:
                ret.append(right[j])
                j+=1

        while i < len(left):
            ret.append(left[i])
            i+=1
        
        while j < len(right):
            ret.append(right[j])
            j+=1

        return ret

    if len(data) < 2:
        return data

    left, right = split(data)

    return merge(merge_sort(left), merge_sort(right))


def main():
    data = [ i for i in range(100) ]

    random.shuffle(data)

    print( merge_sort(data) )

if __name__ == '__main__':
    main()