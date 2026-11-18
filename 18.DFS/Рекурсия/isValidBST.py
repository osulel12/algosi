"""
Ссылка: https://leetcode.com/problems/validate-binary-search-tree/


Алгоритм решения
1. Необходимо сравнить текущее сначение с минимальным и максимальным значением.
2. Текущее значение не должно быть меньше минимально и быть больше максимального.
3. Для левого потомка максимальное будет как текущее значение элемента, для правого наоборот.



Сложность по памяти O(h)
Сложность по времени O(n)
"""

class TreeNode:
    pass


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def helper(root, lo, hi):

            if not root:
                return True

            if not lo < root.val < hi:
                return False


            return helper(root.left, lo, root.val) and helper(root.right, root.val, hi)

        return helper(root, -float('inf'), float('inf'))


# Запустить на leetcode
