#!/usr/bin/env python3

from queue import PriorityQueue

pq = PriorityQueue(10)

def print_queue(pq):
    data=[]
    while not pq.empty():
        data.append(pq.get())
    print(data)

for i in range(1, 16):
    if pq.full():
        pq.get()
        pq.put(i)
    else:
        pq.put(i)

print_queue(pq)

