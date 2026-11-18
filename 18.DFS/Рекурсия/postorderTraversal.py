"""
Ссылка: https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/2156058590/


Алгоритм решения
1. Идея обхода дерева зависит от того, в какой момент мы добавляем элементы в результирующий список.
2. Для решения текущей задачи, нам необходимо добавлять текущий элемент после вызова функции для левого и правого потомков.
L узел, после R узел и после ROOT

Сложность по памяти O(h)
Сложность по времени O(n)
"""

class TreeNode:
    pass


class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []


# Запустить на leetcode
