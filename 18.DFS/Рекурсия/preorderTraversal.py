"""
Ссылка: https://leetcode.com/problems/binary-tree-preorder-traversal/


Алгоритм решения
1. Создадим функцию хелпер. Рекурсивным случаем для нас будет None значение. В остальных случаях случах вызовем хелпер
для левого и правого потомков
Сначала ROOT, после L узел, после R узел

Сложность по памяти O(h)
Сложность по времени O(n)
"""

class TreeNode:
    pass


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:

        ans = []

        def helper(node: TreeNode | None):
            if not node:
                return

            ans.append(node.val)

            helper(node.left)
            helper(node.right)

        helper(root)

        return ans


# Запустить на leetcode
