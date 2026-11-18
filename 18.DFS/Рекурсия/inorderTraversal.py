"""
Ссылка: https://leetcode.com/problems/binary-tree-inorder-traversal/


Алгоритм решения
1. Для inorderTraversal Сначала посещаем L узел, после ROOT и после R узел.


Сложность по памяти O(h)
Сложность по времени O(n)
"""

class TreeNode:
    pass


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


# Запустить на leetcode
