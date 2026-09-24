"""
Условие задачи
Дано: массив целых чисел nums и целое число x.
Нужно: найти длину самого длинного непустого непрерывного подотрезка, минимум на котором равен ровно x.
Если такого подотрезка нет, нужно вернуть -1.


Алгоритм решения
1. Будем поддерживать окно [left, right] и два счётчика.
2. После добавления нового элемента справа сжимаем окно слева, пока в нём есть запрещённый элемент меньше x.
После этого все элементы окна не меньше x.
Если при этом count_x > 0, минимум окна равен ровно x, и его длиной можно обновить ответ.


Сложность по памяти O(1)
Сложность по времени O(n)
"""

from typing import List


class Solution:
    def longest_subarray_with_min(self, nums: List[int], x: int) -> int:
        answer = -1
        left = 0
        count_less = 0
        count_x = 0

        for right, num in enumerate(nums):
            if num < x:
                count_less += 1
            elif num == x:
                count_x += 1

            # Восстанавливаем условие: в окне не должно быть чисел < x
            while count_less > 0:
                if nums[left] < x:
                    count_less -= 1
                elif nums[left] == x:
                    count_x -= 1
                left += 1

            # Теперь все элементы >= x, а наличие x даёт минимум ровно x
            if count_x > 0:
                answer = max(answer, right - left + 1)

        return answer


inst = Solution()
print(inst.longest_subarray_with_min([3, 1, 4, 1, 5], 1))
print(inst.longest_subarray_with_min([2, 3, 4], 1))
