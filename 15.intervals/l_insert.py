"""
Ссылка: https://leetcode.com/problems/insert-interval/


Алгоритм решения
1. Заводим пустой массив для ответа. Указатель равный 0 и получаем длину массива с интервалами.
2. В первом цикле мы добавляем в ответ все интервалы у которых конец, меньше начала newInterval
3. Во втором цикле мы изменяем newInterval при условии, что начало текущего интервала меньше или равно конку newInterval
4. В третьем цикле мы просто добавляем оставшиеся интервалы


Сложность по памяти O(n)
Сложность по времени O(n)
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        ans.append(newInterval)

        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans


inst = Solution()
print(inst.insert([[1,3],[6,9]], [2, 5]))
print(inst.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
