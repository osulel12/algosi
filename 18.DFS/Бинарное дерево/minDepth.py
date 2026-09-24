"""
Ссылка: https://leetcode.com/problems/minimum-depth-of-binary-tree/


Алгоритм решения
1. Тут порядок добавления не важен, поэтому можно добавлять потомков в любом порядке. Создаем стэк следующей структуры:
([root, 0]). ans = float('inf') заведем как самое большое число.
2. Начинаем проходить дерево. На каждой итерации проверяем, является ли элемент листом (не имеет потомков).
Если является, то находим минимум между текущим ответом и расстоянием записанным у этого элемента вторым параметром в картеже.
3. Добавляем правого и левого потомков в стэк, если такие есть.
4. Возвращаем результат.



Сложность по памяти O(h)
Сложность по времени O(n)
"""

class TreeNode:
    pass


class Solution:
    def minDepth(self, root: TreeNode | None) -> int:

        if root:
            stack = [(root, 0)]
            ans = float('inf')
        else:
            stack = []
            ans = 0

        while stack:

            cur, depth = stack.pop()

            depth += 1
            if not cur.left and not cur.right:
                ans = min(ans, depth)

            if cur.left:
                stack.append((cur.left, depth))
            if cur.right:
                stack.append((cur.right, depth))

        return ans



# Запустить на leetcode
