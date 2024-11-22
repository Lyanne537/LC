from collections import deque

# 用链表实现的队列和栈
class LinkedQueue:
    def __init__(self):
        self.list = deque()
    
    def push(self, e):
        self.list.append(e)
    
    def pop(self):
        return self.list.popleft()
    
    def peek(self):
        return self.list[0]
    
    def size(self):
        return len(self.list)
    
class LinkedStack:
    def __init__(self):
        self.list = deque()

    
    def push(self, e):
        self.list.append(e)
    
    def pop(self):
        return self.list.pop()
    
    def peek(self):
        return self.list[-1]
    
    def size(self):
        return len(self.list)
