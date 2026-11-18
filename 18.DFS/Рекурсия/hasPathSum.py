"""
Ссылка: https://leetcode.com/problems/path-sum/


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
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        if not root:
            return False

        targetSum -= root.val

        if not root.left and not root.right and targetSum == 0:
            return True

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


# Запустить на leetcode