"""
Ссылка: https://leetcode.com/problems/invert-binary-tree/


Алгоритм решения
1. Заводим стэк, куда кладем корень нашего дерева.
2. Основная задача сводится к тому, что после получения последнего элемента из стэка, нам нужно поменять местами его
потомков и после добавить каждого в стэк, если такой есть.


Сложность по памяти O(h)
Сложность по времени O(n)
"""

class TreeNode:
    pass

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:

        stack = [root] if root else []

        while stack:

            cur = stack.pop()

            cur.left, cur.right = cur.right, cur.left

            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return root


# Запустить на leetcode
