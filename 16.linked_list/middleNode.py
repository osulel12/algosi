"""
Ссылка: https://leetcode.com/problems/middle-of-the-linked-list/description/


Алгоритм решения
1. В первом цикле считаем длину связанного списка. Находим середину.
2. Во втором цикле снова идем по связанному списку, но только до средины.
3. Возвращаем результат от середины списка.


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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt  = 0

        node = head
        while node:
            cnt += 1
            node = node.next

        steps_to_mid = cnt // 2

        while steps_to_mid:
            steps_to_mid -= 1
            head = head.next

        return head

    def fast_slow_pointers(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Суть метода, что есть два указателя, быстрый и медленный. Быстрый идет всегда на 2 индекса вперед, медленный на один.
        И как только быстрый указатель доходит до конца, медленный указатель всегда оказывается в середине списка.
        """

        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


inst = Solution()
prettyPrintLinkedList(inst.middleNode(stringToListNode("[1,2,3,4,5]")))
prettyPrintLinkedList(inst.middleNode(stringToListNode("[1,2,3,4,5,6]")))

prettyPrintLinkedList(inst.fast_slow_pointers(stringToListNode("[1,2,3,4,5]")))
prettyPrintLinkedList(inst.fast_slow_pointers(stringToListNode("[1,2,3,4,5,6]")))