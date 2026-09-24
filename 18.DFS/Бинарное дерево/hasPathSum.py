"""
Ссылка: https://leetcode.com/problems/path-sum/


Алгоритм решения
1. Создаем стэк и помещаем в него кортеж из корня нашего дерева и значения targetSum.
2. Пока стэк не пустой, мы берем текущий элемент и текущую сумму. Проверяем есть ли у текущего элемента дети и не равна ли
текущая сумма - значение текущего элемента 0, если равна возвращаем True.
3. Если условие не выполнилось, добавляем в стэк кортежи с потомком текущего элемента и текущей суммой - значение текущего
элемента.

Сложность по памяти O(h)
Сложность по времени O(n)
"""

class TreeNode:
    pass


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        stack = [(root, targetSum)] if root else []

        while stack:

            cur, cur_sum = stack.pop()

            cur_sum -= cur.val

            if not cur.left and not cur.right and not cur_sum:
                return True

            if cur.left:
                stack.append((cur.left, cur_sum))
            if cur.right:
                stack.append((cur.right, cur_sum))

        return False

# Запустить на leetcode