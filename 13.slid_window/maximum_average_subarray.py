"""
https://leetcode.com/problems/maximum-average-subarray-i/

Алгоритм решения
1. Действуем через накопленный итог. Вначале находим сумму первых k значений нашего окна.
2. Заводим переменную для темпового значения - cur.
3. Итерируемся по списку и из накопленной сумы вычитаем выходящее значение окна и прибавляем входящее значение окна.

Сложность по памяти O(1)
Сложность по времени O(n)
"""

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = 0
        for i in range(k):
            ans += nums[i]

        cur = ans

        for i in range(k, len(nums)):
            cur = cur - nums[i - k] + nums[i]
            ans = max(ans, cur)

        return ans / k


inst = Solution()
print(inst.findMaxAverage([1,12,-5,-6,50,3], 4))
print(inst.findMaxAverage([5], 1))