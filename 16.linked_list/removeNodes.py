"""
Ссылка:


Алгоритм решения
1. 
2. 
3. 



Сложность по памяти O(1)
Сложность по времени O(n)
"""

from typing import Optional
import json
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def prettyPrintLinkedList(node):
    while node and node.next:
        print(str(node.val) + "->", end='')
        node = node.next

    if node:
        print(node.val)
    else:
        print("Empty LinkedList")


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            head.next = self.removeNodes(head.next)
            if head.next and head.val < head.next.val:
                return head.next
        return head


inst = Solution()
prettyPrintLinkedList(inst.removeNodes(stringToListNode('[1,2,6,3,4,5,6]')))
prettyPrintLinkedList(inst.removeNodes(stringToListNode('[5,2,13,3,8]')))
