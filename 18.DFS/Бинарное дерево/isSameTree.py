"""
Ссылка: https://leetcode.com/problems/same-tree/


Алгоритм решения
1. Кладем в стэк кортеж из первого и второго дерева.
2. Пока стек не пустой начинаем его обходить и на каждом шаге доставать последний кортеж.
3. Делаем ряд проверок:
    3.1. p and not q -> False
    3.2. not p and q -> False
    3.3. not p and not q -> pass
    3.4. p and q -> False
        3.4.1 p.val != q.val -> False
4. Если же на есть обо узла и их значения равны, мы добавляем в стэк следующих потомков текущих узлов.


Сложность по памяти O(min(h1, h2))
Сложность по времени O(min(n, m))
"""

class TreeNode:
    pass


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        stack = [(p, q)]

        while stack:

            p, q = stack.pop()

            if p and not q:
                return False

            if not p and q:
                return False

            if not p and not q:
                pass
            if p and q:
                if p.val != q.val:
                    return False

                stack.append((p.left, q.left))
                stack.append((p.right, q.right))
        return True


# Запустить на leetcode
