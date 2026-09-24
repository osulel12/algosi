"""
Ссылка: https://leetcode.com/problems/maximum-depth-of-binary-tree/


Алгоритм решения
1. Тут порядок добавления не важен, поэтому можно добавлять потомков в любом порядке. Создаем стэк следующей структуры:
([root, 1]).
2. Начинаем проходить дерево. На каждой итерации находим максимум между текущим ответом и depth полученным из tuple
в стэке.
3. Добавляем правого и левого потомков в стэк, если такие есть.
4. Возвращаем результат.



Сложность по памяти O(h)
Сложность по времени O(n)
"""

class TreeNode:
    pass


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        if root:
            stack = [(root, 1)]
            ans = 0
        else:
            stack = []
            ans = 0

        while stack:

            cur, depth = stack.pop()
            ans = max(ans, depth)

            if cur.left:
                stack.append((cur.left, depth+1))
            if cur.right:
                stack.append((cur.right, depth+1))

        return ans


# Запустить на leetcode
