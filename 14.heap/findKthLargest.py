"""
Ссылка: https://leetcode.com/problems/kth-largest-element-in-an-array/


Алгоритм решения
1. Находим k наибольших элементов используя кучу и в ней находим минимум


Сложность по памяти O(k)
Сложность по времени O(n * log(k))
"""

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return min(heapq.nlargest(k, nums))

inst = Solution()
print(inst.findKthLargest([3,2,1,5,6,4], 2))
print(inst.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
