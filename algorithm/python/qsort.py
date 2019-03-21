#!/usr/bin/env python

import random

#TEST_DATA=[ 2,5,4,9,7,1,3,6,8 ]
TEST_DATA=[ x for x in range(100)]
random.shuffle(TEST_DATA)

def qsort(data_in):

    if data_in == []:
        return []

    pivot = random.randint(0,len(data_in)-1)
    data_in[0],data_in[pivot] = data_in[pivot],data_in[0]
    return  qsort([ x for x in data_in[1:] if x < data_in[0] ]) + [ data_in[0]] + qsort([ x for x in data_in[1:] if x>= data_in[0]])


def simple_qsort(data):

    if len(data) < 2:
        return data

    index = len(data) // 2

    data[0], data[index] = data[index], data[0]

    pivot = data[0]

    left = [ x for x in data[1:] if x < pivot ]
    right = [ x for x in data[1:] if x >= pivot ]

    return simple_qsort(left) + [pivot] + simple_qsort(right)


def main():
    print qsort(TEST_DATA)
    print simple_qsort(TEST_DATA)

if __name__ == "__main__":
    main()
