from collections import deque

class ListDeque:
    def __init__(self):
        self.deque = deque()
    
    def add_first(self, e):
        self.deque.addleft(e)

    def add_last(self, e):
        self.deque.append(e)
    
    def remove_first(self):
        self.deque.popleft()
    
    def remove_last(self):
        self.deque.pop()
    
    def peel_first(self):
        return self.deque[0]
    
    def peek_last(self):
        return self.deque[-1]

class CycleArray:
        def __init__(self, size=1):
            self.size = size
            self.arr = [None] * size
            self.start = 0
            self.end = 0
            self.count = 0
        
        def resize(self, newSize):
            new_arr = [None] * newSize
            for i in range(self.count):
                new_arr[i] = self.arr[(self.start + i) % self.size]
            self.arr = new_arr
            self.start = 0
            self.end = self.count
            self.size = newSize

        def add_first(self, val):         
            if self.is_full():
                self.resize(self.size * 2)
            
            self.start = (self.start -1 + self.size) % self.size
            self.arr[self.start] = val
            self.count += 1
        
        def remove_first(self):
            if self.is_empty():
                raise Exception("Array is empty")
            self.arr[self.start] = None
            self.start = (self.start + 1) % self.size
            self.count -= 1
            if self.count > 0 and self.count == self.size //4:
                self.resize(self.size // 2)
        
        def add_last(self, val):
            if self.is_full():
                self.resize(self.size * 2)
            self.arr[self.end] = val
            self.end = (self.end +1) % self.size
            self.count += 1
        
        def remove_last(self):
            if self.is_empty():
                raise Exception("Array is empty")
            self.end = (self.end -1 + self.size) % self.size
            self.arr[self.end] = None
            self.count -= 1

            if self.count >0 and self.count == self.size // 4:
                self.resize(self.size // 2)
    
        def get_first(self):
            if self.is_empty():
                raise Exception("Array is empty")
            return self.arr[self.start]
        
        def get_last(self):
            if self.is_empty():
                raise Exception("Array is empty")
            return self.arr[(self.end -1 + self.size) % self.size]
        
        def is_full(self):
            return self.count == self.size
        
        def is_empty(self):
            return self.count == 0
        
        def size(self):
            return self.count
        

            



class ArrayDeque:

    def __init__(self):
        self.arr = CycleArray()
    
    def add_first(self, e):
        self.arr.add_first(e)
    
    def add_last(self, e):
        self.arr.add_last(e)

    def remove_first(self):
        return self.arr.remove_first()
    
    def remove_last(self):
        return self.arr.remove_last()