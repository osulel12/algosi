"""
Ссылка: https://leetcode.com/problems/search-in-a-binary-search-tree/


Алгоритм решения
1. 
2. 
3. 



Сложность по памяти O(1)
Сложность по времени O(log(n))
"""

class TreeNode:
    pass


class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:

        if not root:
            return

        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)

        if val > root.val:
            return self.searchBST(root.right, val)

        return


# Запустить на leetcode
