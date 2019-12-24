#Import the libraries
import queue
import time
"""
#FIRST EXAMPLE

#This is LIFO. Last item in q.put() and q.get() get the first out of queue's item.
q = queue.LifoQueue()

for i in range(5):
    q.put(i)

while not q.empty():
    # Last item first iteme geçer ve q.get() first itemi okur ve 4-3-2-1-0 şeklinde çıktı sağlar.
    print(q.get(), end = '   ')

print('\n')
"""

"""
#SECOND EXAMPLE
# Variant of Queue that retrieves open entries in priority order (lowest first). Entries are typically tuples of the form: (priority number, data).
q1 = queue.PriorityQueue()

q1.put((1, 'Elma'))
q1.put((3, 'Armut'))
q1.put((4, 'Muz'))
q1.put((2, 'Avokado'))

for i in range(q1.qsize()):
    print(q1.get())
"""