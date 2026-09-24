"""
Ссылка: https://leetcode.com/problems/merge-intervals/


Алгоритм решения
1. Сортируем наши интервалы по начал.
2. Начинаем итерироваться и сравнивать конец последнего интервала с началом текущего, если у текущего начало интервала
меньше или равно концу предыдущего, до мы обновляем конец предыдущего интервала выбирая максимум из конца предыдущего и
начала текущего интервалов.


Сложность по памяти O(n)
Сложность по времени O(n * log n)
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        ans = []

        for i in intervals:
            if ans and ans[-1][1] >= i[0]:
                ans[-1][1] = max(ans[-1][1], i[1])
            else:
                ans.append(i)
        return ans


inst = Solution()
print(inst.merge([[1,3],[2,6],[8,10],[15,18]]))
print(inst.merge([[1,4],[4,5]]))
