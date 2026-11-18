"""
Ссылка: https://leetcode.com/problems/maximum-depth-of-binary-tree/


Алгоритм решения
1. Находим максимум между левой веткой и правой веткой, на каждом шаге прибавляем 1.

Сложность по памяти O(h)
Сложность по времени O(n)
"""

class TreeNode:
    pass


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0

# Запустить на leetcode
