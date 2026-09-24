"""
Ссылка: https://leetcode.com/problems/interval-list-intersections/


Алгоритм решения
1. Заводим переменную под ответ и два указателя равные 0.
2. В цикле, пока оба указателя меньше длинны своих списков мы итерируемся и находит начало и конец первого интервала
начало и конец второго интервала.
3. Далее находим максимальное начало и минимальное окончание, после этого сравниваем и если максимальное начало меньше или равно
минимальному окончанию, то записываем эти значения в наш ответ, как новый интервал.
4. Проверяем, если окончание первого интервала, меньше второго, то увеличиваем первый указатель, так как первый интервал
мы уже прошли, во всех иных случаях увеличиваем указатель для второго списка интервалов.



Сложность по памяти O(m + n)
Сложность по времени O(m + n)
"""

from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        first = second = 0

        while first < len(firstList) and second < len(secondList):
            start1, end1 = firstList[first]
            start2, end2 = secondList[second]

            max_start = max(start1, start2)
            min_end = min(end1, end2)

            if max_start < min_end:
                ans.append([max_start, min_end])
            if end1 < end2:
                first += 1
            else:
                second += 1

        return ans


inst = Solution()
print(inst.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
