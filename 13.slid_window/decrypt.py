"""
Ссылка: https://leetcode.com/problems/defuse-the-bomb/description/


Алгоритм решения
1. Заводим массив с кол-вом 0 равным длине массива.
2. Проверяем, если k больше 0, значит двигаемся в правую сторону от текущего элемента массива. Где 0 элемент мы считаем
до цикла, а цикл начинаем со 2-го элемента (индекс = 1). Левая граница окна это идекс текущей итерации, правая граница
находится как индекс текущего элемента + или - размер окна (k) деленные с остатком на длину массива.
3. Сумма элемента находится, как предыдущая сумма окна минус значение текущего элемента + значение правого элемента.



Сложность по памяти O(1)
Сложность по времени O(n)
"""

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n

        if k > 0:
            ans[0] = wsum = sum(code[1:k + 1])
            for l in range(1, n):
                r = (l + k) % n
                wsum += -code[l] + code[r]
                ans[l] = wsum

        if k < 0:
            ans[0] = wsum = sum(code[-1: k - 1: -1])
            for l in range(1, n):
                r = (l - k) % n
                wsum += -code[-l] + code[-r]
                ans[-l] = wsum

        return ans


inst = Solution()
print(inst.decrypt([5,7,1,4], 3))
print(inst.decrypt([1,2,3,4], 0))
print(inst.decrypt([2,4,9,3], -2))










