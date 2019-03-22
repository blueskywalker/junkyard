
from queue import PriorityQueue


pq = PriorityQueue(10)

for i in range(1,16):
    if pq.full():
        pq.get()
    pq.put(i, timeout=True)


while not pq.empty():
    print(pq.get())
