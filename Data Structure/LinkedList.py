from typing import List
#单链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
def createLinkedList(arr:'List[int]') -> 'ListNode':
    if arr is None or len(arr) == 0:
        return None
    
    head = ListNode(arr[0])
    cur = head
    for i in range(1,len(arr)):
        cur.next = arr[i]
        cur = cur.next
    
    return head

head = createLinkedList([1, 2 , 3, 4, 5])
p = head

#遍历
while p is not None:
    print(p.val)
    p = p.next

#增
newHead = ListNode([0])
newHead.next = head
head = newHead