"""
Ссылка: https://leetcode.com/problems/binary-tree-paths/


Алгоритм решения
1. 
2. 
3. 



Сложность по памяти O(1)
Сложность по времени O(n)
"""

class TreeNode:
    pass


class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:

        stack = [(root, [])] if root else []

        while stack:

            cur, path = stack.pop()

            path.append(cur.val)




# Запустить на leetcode
