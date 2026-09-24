"""
Ссылка: https://leetcode.com/problems/daily-temperatures/


Алгоритм решения
1. Заведем наш массив ответов и стэк.
2. В цикле начнем перебирать значения температур. Если стэк не пустой и текущее значение температуры больше,
чем последнее значение температуры в стэке, в таком случае мы удаляем последнее значение температуры из стэка.
А в массив ответов меняем значение индекса температур на разность индекса текущего дня и дня, который мы удалили из стэка.
3. Добавляем текущий день в стэк.



Сложность по памяти O(n)
Сложность по времени O(n)
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        ans = [0] * len(temperatures)

        stack = []

        for day, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:

                last_day = stack.pop()

                ans[last_day] = day - last_day

            stack.append(day)

        return ans


inst = Solution()
print(inst.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(inst.dailyTemperatures([30,60,90]))
