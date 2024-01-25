"""
Write a program to implement queue data structure. Queue is a First in First Out(FIFO) list.
In which adding take place at the rear end of the queue and deletion take place at the front end of queue.
"""
import collections

q = collections.deque()
# adding data to the q
q.append("Vikash")
q.append("Vicky")
q.append("Vishal")
q.append("Vinay")
q.append("Viswas")
q.append("Suman")
q.append("Satish")

print(q)
# pop up the data from the queue
print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q)
