"""
Ссылка: https://leetcode.com/problems/remove-linked-list-elements/description/


Алгоритм решения. DummyNode
1. Прикрепляем с левой стороны к голове списка пустой элемент.
2. Заводим два указателя, на предыдущий элемент и текущий элемент.
3. Пока текущий указатель не None, мы итерируемся по списку и проверяем значение каждой итерации.
Если текущее значение = нашему val, то мы перелинковываем ссылку у предыдущего элемента на следующий от текущего.
Т.е есть список [1, 2, 3, 4, 4, 5]. Мы находимся сейчас на итерации, где cur = 3, а prev 2 и нам нужно удалить все
val = 4. Для текущей итерации мы просто двигаем наши указатели, cur = 4, а prev = 3. Видим, что текущее значение = 4, значите
prev теперь должен ссылаться на следующее значение от текущего, а значит наш список будет выглядеть так [1, 2, 3, 4, 5].
Cur двигаем всегда и оно снова становится равным 4, значит проделываем туже операцию, prev теперь ссылается на 5, таким образом
наш список выглядит так [1, 2, 3, 5]
4. cur мы всегда двигаем, а prev двигаем только в том случае, если cur.val не равно нашему переданному параметру.



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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        prev, cur = dummy, head

        while cur:

            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur

            cur = cur.next
        return dummy.next


inst = Solution()
prettyPrintLinkedList(inst.removeElements(stringToListNode('[1,2,6,3,4,5,6]'), 6))
prettyPrintLinkedList(inst.removeElements(stringToListNode('[]'), 1))
