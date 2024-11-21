from typing import List, Optional
#单链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None
    
def createLinkedList(arr:'List[int]') -> Optional[ListNode]:
    if not arr:
        return None
    
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    
    return head

head = createLinkedList([1, 2 , 3, 4, 5])
p = head

# 遍历
while p:
    print(p.val)
    p = p.next

# 查
## 查找第三个节点
index = 3
if index < 0:
    target_node = None
else:
    p = head
    count = 0
    while p:
        if count == index:
            target_node = p
            break
        p = p.next
        count += 1
    else:
        target_node = None
if target_node:
    print(f"Node at index {index}:{target_node.val}")
else:
    print(f"Index{index} is out of range")

# 增
## 头部
newHead = ListNode([0])
newHead.next = head
head = newHead

## 尾部
head = createLinkedList([1, 2 , 3, 4, 5])
p = head
while p.next:
    p = p.next
p.next = ListNode([6])

## 中间
### 在第3个节点后插入新节点537
head = createLinkedList([1, 2 , 3, 4, 5])
p = head
for i in range(2):
    p = p.next

new_node = ListNode([537])
new_node.next = p.next

p.next = new_node

# 删
## 头部
head = createLinkedList([1, 2 , 3, 4, 5])
head = head.next

## 尾部
head = createLinkedList([1, 2 , 3, 4, 5])
p = head
while p.next.next:
    p = p.next

p.next = None

## 中间
### 删除第 4 个节点
head = createLinkedList([1, 2 , 3, 4, 5])
p = head
for i in range(2):
    p = p.next

p.next = p.next.next

class DoublyListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[DoublyListNode] = None
        self.prev: Optional[DoublyListNode]  = None

def createDoublyLinkedList(arr: List[int]) -> Optional[DoublyListNode]:
    if not arr:
        return None
    
    head = DoublyListNode(arr[0])
    cur = head

    for val in arr[1:]:
        new_node = DoublyListNode(val)
        cur.next = new_node
        new_node.prev = cur
        cur = cur.next
    
    return head

# 遍历

head = createDoublyLinkedList([1, 2, 3, 4, 5])
tail = None

## 向后
p = head
while p:
    print(p.val)
    tail = p
    p = p.next

## 向前
p = tail
while p:
    print(p.val)
    p = p.prev


# 增
# 头部
head = createDoublyLinkedList([1, 2, 3, 4, 5])
new_head = DoublyListNode([0])
new_head.next = head
head.prev = new_head
head = new_head

#尾部
head = createDoublyLinkedList([1, 2, 3, 4, 5])
tail = head

while tail.next:
    tail = tail.next

new_node = DoublyListNode([6])
tail.next = new_node
new_node.prev = tail
tail= new_node

# 中间
### 在第3个节点后插入新节点537
head = createDoublyLinkedList([1, 2, 3, 4, 5])
p = head

for _ in range(2):
    p = p.next

new_node = DoublyListNode([537])
new_node.next = p.next
new_node.prev = p

p.next.prev = new_node
p.next = new_node

# 删
#头部
head = createDoublyLinkedList([1, 2, 3, 4, 5])

to_Delete = head
head = head.next
head.prev = None

to_Delete.next = None

#尾部
head = createDoublyLinkedList([1, 2, 3, 4, 5])
p = head
while p.next:
    p = p.next

p.prev.next = None

p.prev = None

## 中间
### 删除第 4 个节点
head = createDoublyLinkedList([1, 2, 3, 4, 5])
p = head

for _ in range(2):
    p = p.next

to_Delete = p.next

p.next = to_Delete.next
to_Delete.next.prev = p

to_Delete.next = None
to_Delete.prev = None


# Dummy
## DoublyLinkedList
class Node:
    def __init__(self, val):
        self.val = val
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_last(self, e):
        x = Node(e)
        temp = self.tail.prev
        temp.next =x
        x.prev = temp

        x.next = self.tail
        self.tail.prev = x
        self.size += 1
    
    def add_first(self ,e):
        x = Node(e)
        temp = self.head.next
        temp.prev = x
        x.next = temp

        self.head.next = x
        x.prev = self.head
        self.size += 1
    
    def add(self, index, e):
        self.check_position_index(index)
        if index == self.size:
            self.add_last(e)
            return
        
        p = self.get_node(index)
        temp = p.prev


        x = Node(e)
        
        p.prev = x
        temp.next = x

        x.prev = temp
        x.next = p

        self.size += 1
    
    def remove_first(self):
        if self.size < 1:
            raise IndexError("No Elements to remove")
        
        x = self.head.next
        temp = x.next

        self.head.next = temp
        temp.prev = self.head

        self.size -= 1
        return x.val
    
    def remove_last(self):
        if self.size < 1:
            raise IndexError("No Elements to remove")

        x = self.tail.prev
        temp = x.prev

        self.tail.prev = temp
        temp.next = tail

        self.size -= 1
        return x.val
    
    def remove(self, index):
        self.check_element_index(index)
        
        x = self.get_node(index)
        prev = x.prev
        next = x.next

        prev.next = next
        next.prev = prev

        self.size -= 1
        
        return x.val
    
    def get(self, index):
        self.check_element_index(index)
        p = self.get_node(index)

        return p.val
    
    def get_first(self):
        if self.size<1:
            return IndexError("No elements in the list")
        return self.head.val
    
    def get_last(self):
        if self.size<1:
            return IndexError("No elements in the list")
        return self.tail.val
    
    def set(self, index, val):
        self.check_element_index(index)
        p = self.get_node(index)

        old_val = p.val
        p.val = val

        return old_val
    
    def size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def get_node(self, index):
        self.check_element_index(index)
        p = self.head.next

        for _ in range(index):
            p = p.next
        
        return p
    
    def is_element_index(self, index):
        return 0 <= index < self.size

    def is_position_index(self, index):
        return 0 <= index <= self.size   
    
    def check_element_index(self, index):
        if not self.is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")
    
    def check_position_index(self, index):
        if not self.is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")
    
    def display(self):
        print(f"size = {self.size}")
        p = self.head.next
        while p != self.tail:
            print(f"p.val <->", end= "")
            p= p.next
        print("null\n")








    



        










