"""
Ссылка: https://leetcode.com/problems/sum-of-left-leaves/


Алгоритм решения
1. Заводим переменную стэк и переменную, в которой будет наш ответ.
2. Пока стэк не пустой итерируемся по нему.
3. Находим потомка удовлетворяющего условию: это левый потомок и у него нет ни левого ни правого ребенка.
4. Добавляем стэк левого и правого потомком, если они есть.

Сложность по памяти O(h)
Сложность по времени O(n)
"""

class TreeNode:
    pass


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        ans = 0
        stack = [(root, False)] if root else []

        while stack:

            cur, is_left = stack.pop()

            if not cur.left and not cur.right and is_left:
                ans += cur.val

            if cur.left:
                stack.append((cur.left, True))
            if cur.right:
                stack.append((cur.right, False))

        return ans

# Запустить на leetcode
