
#instead of using a normal queue here 
#we will use deque data struct that is a more optimized version of a queue that allows
#faster deletions and insertions to a queue
from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]
    
    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    q = Queue()
    print(q)
    q.enqueue(3)
    print(q)
    q.enqueue(4)
    print(q.peek())
    print(q.is_empty())

    
