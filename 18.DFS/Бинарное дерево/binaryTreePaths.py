"""
Ссылка: https://leetcode.com/problems/binary-tree-paths/


Алгоритм решения
1. В стэк кладем наш корень и пустой массив, который будешь содержать путь до текущего узла.
2. Пока стэк не пустой, мы достаем из него последний кортеж. Проверяем, является текущий элемент листом
(не содержит потомков). Если да, кладем путь в массив ответов ans.
3. Если элемент не лист, значит проверяем левого и правого потоком, что они существуют.
4. После проверки кладем в стэк существующего потомка и путь, НО тут важно, что нужно класть именно копию,
так как если мы и туда и туда положим один и тот же массив, не копировав его, то ссылка у двух разных потомков
будет на один и тот же элемент, что при изменении пути, даст эти изменения и в том месте, где мы не ожидаем.



Сложность по памяти O(h^2)
Сложность по времени O(n^2)
"""

class TreeNode:
    pass


class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:

        stack = [(root, [])] if root else []
        ans = []

        while stack:

            cur, path = stack.pop()

            path.append(str(cur.val))

            if not cur.left and not cur.right:
                ans.append("->".join(path))

            if cur.left:
                stack.append((cur.left, path[:]))
            if cur.right:
                stack.append((cur.right, path[:]))

        return ans


# Запустить на leetcode
