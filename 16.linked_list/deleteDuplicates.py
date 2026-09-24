"""
Ссылка: https://leetcode.com/problems/remove-duplicates-from-sorted-list/


Алгоритм решения. DummyNode
1. Заводим пустой элемент, который прикрепляем к голове списка слева. Важно, чтобы его val был не числом, иначе в ситуации,
когда наш список равное [0, 0, 0] и наше DummyNode тоже = 0, мы удалим все элементы.
2. Заводим два указателя, на предыдущий и текущий элементы.
3. В цикле проверяем, равно ли значение текущего элемента, значению предыдущего, если равно, то перелинковываем
сслку предыдущего элемента на следующий элемент от текущего и двигаем позицию текущего элемента.
4. Предыдущий элемент двигаем только в случае, когда его значение не равно текущему.



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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, next=head)

        prev, cur = dummy, head

        while cur:

            if cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return dummy.next


inst = Solution()
prettyPrintLinkedList(inst.deleteDuplicates(stringToListNode('[1,2,6,3,4,5,6]')))
prettyPrintLinkedList(inst.deleteDuplicates(stringToListNode('[0, 0, 0]')))
