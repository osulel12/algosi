"""
Ссылка: https://leetcode.com/problems/fruit-into-baskets/description/


Алгоритм решения
1. Заводим словарь в котором будем хранить наше окно из уникальных значений.
2. Заводим два указателя левый = 0 и правый равный текущему индексу массива.
3. Двигаем правый указатель и на каждой итерации добавляем значение массива в наш словарь window
4. Если уникальных значений в словаре больше 2х уменьшаем сначало кол-во этих значений и как уменьшим счетчик значения до 0
удаляем его из словаря, на каждой такой итерации увеличиваем левый указатель.
5. Сравниваем предыдущее значение длинны окна с текущим значением.

*P.S Есть решение оптимальнее, через хранение текущего и предыдущего значения фрукта и длинный самой длинной
не прерывной последовательности. Но если условие изменится и к примеру, надо будет найти максимальную длину уже 3х
уникальных деревьев, то такое решение не подойдет, а в текущем решении просто нужно будет изменить условие на
while len(window) > 3:



Сложность по памяти O(1)
Сложность по времени O(n)
"""

from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        ans = 0

        window = defaultdict(int)

        for right in range(len(fruits)):
            window[fruits[right]] += 1

            while len(window) > 2:
                window[fruits[left]] -= 1

                if window[fruits[left]] == 0:
                    del window[fruits[left]]

                left += 1

            ans = max(ans, right - left + 1)

        return ans


inst = Solution()
print(inst.totalFruit())
print(inst.totalFruit())
