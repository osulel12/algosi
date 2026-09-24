"""
Ссылка: https://leetcode.com/problems/palindrome-linked-list/description/


Алгоритм решения
1. Находим середину списка и его вторую половину.
2. Разворачиваем первую половину списка.
3. Проверяем значения у первой и второй половины, если все значения равны, значит список палиндром
4. Восстанавливаем исходный список

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

    def find_middle(self, head: Optional[ListNode]) -> ListNode:
        """
        Возвращает последний узел первой половины.
        """

        slow = head
        fast = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow


    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Разворачивает связный список и возвращает его новую голову.
        """

        prev = None
        cur = head

        while cur:
            next_node = cur.next

            cur.next = prev

            prev = cur
            cur = next_node

        return prev


    def is_palindrome(
        self,
        head: Optional[ListNode]
    ) -> bool:
        """
        Проверяет, является ли список палиндромом.
        После проверки восстанавливает исходный список.
        """

        if not head or not head.next:
            return True

        # 1. Находим конец первой половины
        middle = self.find_middle(head)

        # 2. Начало второй половины
        second_half = middle.next

        # 3. Разворачиваем вторую половину
        reversed_second_half = self.reverse(second_half)

        # 4. Сравниваем половины
        first = head
        second = reversed_second_half

        result = True

        while second:
            if first.val != second.val:
                result = False
                break

            first = first.next
            second = second.next

        # 5. Восстанавливаем исходный список
        self.restore_list(middle, reversed_second_half)

        return result


    def restore_list(
        self,
        middle: ListNode,
        second_half: ListNode
    ) -> None:
        """
        Восстанавливает исходный список.

        Повторно разворачивает вторую половину
        и подключает её обратно к первой.
        """

        restored_second_half = self.reverse(second_half)

        middle.next = restored_second_half


inst = Solution()
print(inst.is_palindrome(stringToListNode('[1,2,6,3,4,5,6]')))
print(inst.is_palindrome(stringToListNode('[1,2,2,1]')))
