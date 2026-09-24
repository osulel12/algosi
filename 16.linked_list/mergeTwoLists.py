"""
Ссылка: https://leetcode.com/problems/merge-two-sorted-lists/description/


Алгоритм решения
1. Создаем объект пустого узла. На него ссылаются переменные dummy и prev.
2. В цикле, пока есть список 1 и 2 начинаем итерироваться.
3. К предыдущему элементу приклеиваем текущий меньший элемент из двух списков. После чего меняем значение предыдущего элемента
и указателя текущего списка.
4. В конце приклеиваем к prev на котором остановился цикл остаток списка.


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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                prev.next = list2
                prev = list2
                list2 = list2.next

        prev.next = list1 if list1 else list2

        return dummy.next



inst = Solution()
prettyPrintLinkedList(inst.mergeTwoLists(stringToListNode('[1,2,6,3,4,5,6]'), stringToListNode('[1, 2]')))
prettyPrintLinkedList(inst.mergeTwoLists(stringToListNode('[1, 2]'), stringToListNode('[1, 2]')))
