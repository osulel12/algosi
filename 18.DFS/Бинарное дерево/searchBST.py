"""
Ссылка: https://leetcode.com/problems/search-in-a-binary-search-tree/


Алгоритм решения
1. Воспользуемся преимуществом бинарного дерева. Все левые узлы, меньше родительского, все правые узлы больше родительского.
2. Присваиваем текущему элементу корень дерева и итерируемся по нему, пока текущий элемент не None.
3. Проверяем, если значение текущего элемента = val, то нужный нам узел, возвращаем его.
4. Если значение не равны, то проверям, val меньше текущего элемента, если да, то идем в левую ветку,
если больше, то идем в правую ветку.


Сложность по памяти O(1)
Сложность по времени O(log(n))
"""

class TreeNode:
    pass


class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        cur = root if root else None

        while cur:

            if cur.val == val:
                return cur

            if val < cur.val:
                cur =  cur.left
            else:
                cur = cur.right

        return None

# Запустить на leetcode
