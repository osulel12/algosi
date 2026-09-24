"""
Ссылка:


Алгоритм решения
1. Итерируемся по списку и сдвигаем на 1 бит вправо.

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
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        while head:
            num = (num << 1) | head.val
            head = head.next
        return num


inst = Solution()
print(inst.getDecimalValue(stringToListNode('[1,0,1]')))
print(inst.getDecimalValue(stringToListNode('[1,0]')))
