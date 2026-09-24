"""
Ссылка: https://leetcode.com/problems/k-closest-points-to-origin/


Алгоритм решения
1. Воспользуемся методом nsmallest у кучи, который возвращает минимальные К значений,
где в ключ передадим формулу нахождения расстояния между точками


Сложность по памяти O(n)
Сложность по времени O(n log k)
"""

from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=lambda point: point[0] ** 2 + point[1] ** 2)


inst = Solution()
print(inst.kClosest([[1,3],[-2,2]], 1))
print(inst.kClosest([[3,3],[5,-1],[-2,4]], 2))
