"""
Ссылка: https://leetcode.com/problems/intersection-of-two-linked-lists/


Алгоритм решения
1. Находим длину каждого из связанных списков.
2. Находим наиболее длинный список и равняем указатели, перемещаясь на столько элементов, сколько равна разность длин списков.
3. Проверяем, есть ли в этих списках одинаковые элементы на одной и той же позиции указателей. Если да, то вернем True,
если пройдя все списки мы не нашли одинаковых элементов, возвращаем None.


Сложность по памяти O(1)
Сложность по времени O(n + m)
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        len_a = 0
        cur = headA

        while cur:
            cur = cur.next
            len_a += 1

        len_b = 0
        cur = headB

        while cur:
            cur = cur.next
            len_b += 1

        if len_a > len_b:
            n = len_a - len_b
            head_long = headA
            head_short = headB
        else:
            n = len_b - len_a
            head_long = headB
            head_short = headA

        while n:
            head_long = head_long.next
            n -= 1

        while head_long:
            if head_long == head_short:
                return head_long
            head_long = head_long.next
            head_short = head_short.next

        return None

inst = Solution()
prettyPrintLinkedList(inst.getIntersectionNode(stringToListNode('[4,1,8,4,5]'), stringToListNode('[5,6,1,8,4,5]')))
prettyPrintLinkedList(inst.getIntersectionNode(stringToListNode('[1,9,1,2,4]'), stringToListNode('[3,2,4]')))
