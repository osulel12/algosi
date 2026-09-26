"""
Ссылка: https://leetcode.com/problems/count-good-nodes-in-binary-tree/


Алгоритм решения
1. Так как по условия корень всегда есть, то формируем такой стэк [(root, -float('inf'))], это важно, чтобы корректно
найти максимум.
2. Начинаем обход нашего дерева и достаем из стэк последний элемент и максимальное значение на пути к узлу.
3. Проверяем, если текущее значение узла, больше или равно текущему максимуму, то увеличиваем наш счетчик хороших узлов.
4. На каждом шаге обновляем максимум
5. Проверяем есть ли правый или левый потомки и записываем их в стэк вместе с текущим максимумом.


Сложность по памяти O(h)
Сложность по времени O(n)
"""

class TreeNode:
    pass


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = [(root, -float("inf"))]

        ans = 0

        while stack:

            cur, path_val_max = stack.pop()

            if cur.val >= path_val_max:
                ans += 1

            path_val_max = max(cur.val, path_val_max)

            if cur.left:
                stack.append((cur.left, path_val_max))
            if cur.right:
                stack.append((cur.right, path_val_max))

        return ans

# Запустить на leetcode

