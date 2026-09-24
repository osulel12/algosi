"""
Ссылка: https://leetcode.com/problems/reverse-linked-list/


Алгоритм решения
1. Заводим два указателя, предыдущий смотрит на None и текущий, голова нашего списка.
2. Итерируемся по списку. Сохраняем ссылку текущего элемента на следующий во временную переменную
3. Перединковываем, теперь ссылка текущего элемента смотрит на предыдущий элемент.
Предыдущий элемент становится текущим (двигаем наш указатель вправо). А текущий элемент становится равный элементу,
который мы положили во временную переменную (это сделано для того, чтобы не потерять свзять при перекидывании ссылки).


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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, cur = None, head

        while cur:
            tmp_value = cur.next

            cur.next = prev
            prev = cur
            cur = tmp_value
        return prev


inst = Solution()
prettyPrintLinkedList(inst.reverseList(stringToListNode('[1,2,6,3,4,5,6]')))
prettyPrintLinkedList(inst.reverseList(stringToListNode('[1, 2]')))
