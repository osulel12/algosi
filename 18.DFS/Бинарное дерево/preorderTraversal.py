"""
Ссылка: https://leetcode.com/problems/binary-tree-preorder-traversal/


Алгоритм решения
1. Нам необходимо обойти дерево используя метод DFS Preorder, то есть добавлять в стэк сначала правого потомка,
потом левого. Для этого создаем наш массив со сначала дерева и стэк, куда кладем начало дерева.
2. Начинаем идти по дереву с помощью цикла while, пока стэк не пустой.
3. Сначала кладем в стэк правого потомка, если такой есть.
4. Кладем левого потомка, если есть.
5. Возвращаем массив со значениями дерева.



Сложность по памяти O(h) - сложно будет равна высоте дерева.
Сложность по времени O(n)
"""

class TreeNode:
    pass


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:

        stack = [root] if root else []
        ans = []

        while stack:

            cur = stack.pop()
            ans.append(cur.val)

            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return ans


# Запустить на leetcode
