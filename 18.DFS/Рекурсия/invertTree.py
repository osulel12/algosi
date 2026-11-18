"""
Ссылка: https://leetcode.com/problems/invert-binary-tree/


Алгоритм решения
1. 
2. 
3. 



Сложность по памяти O(h)
Сложность по времени O(n)
"""

class TreeNode:
    pass


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:

        if not root:
            return

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# Запустить на leetcode
