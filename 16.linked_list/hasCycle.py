"""
Ссылка: https://leetcode.com/problems/linked-list-cycle/


Алгоритм решения
1. Создаем два указателя, медленный и быстрый.
2. Медленный идет на один шаг, быстрый на два.
3. Если быстрый указатель нагоняет медленный, то цикл есть, возвращаем True, если этого не произошло, цикла нет вернем
False


Сложность по памяти O(1)
Сложность по времени O(n)
"""

from typing import Optional
import json

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = head.next
        slow = head

        while fast and fast.next and head:

            if fast == slow:
                return True

            fast = fast.next.next
            slow = slow.next

        return False



inst = Solution()
print(inst.hasCycle(stringToListNode('[3,2,0,-4]')))
print(inst.hasCycle(stringToListNode('[1,2]')))
