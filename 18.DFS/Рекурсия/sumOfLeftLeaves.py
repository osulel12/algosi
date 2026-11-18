"""
Ссылка: https://leetcode.com/problems/sum-of-left-leaves/


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
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:

        def dfs(node, is_left):
            if not node:
                return 0

            if is_left and not node.left and not node.right:
                return node.val

            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)


# Запустить на leetcode
