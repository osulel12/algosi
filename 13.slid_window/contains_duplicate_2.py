"""
https://leetcode.com/problems/contains-duplicate-ii/

Алгоритм решения
1. Заводим наше окно в виде множества.
2. Итерируемся по массиву и проверяем, есть ли i элемент в нашем окне. Если элемент есть, возвращаем True.
3. Если элемента нет в нашем окне, то мы добавляем i элемент в window и проверяем, не превышает ли длинна window значение k,
если превышает, то удаляем элемент i-k, который вывалился из окна длинной в k.

Сложность по памяти O(min(n, k))
Сложность по времени O(n)
"""

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):

            if nums[i] in window:
                return True

            window.add(nums[i])

            if len(window) > k:
                window.remove(nums[i - k])
        return False


inst = Solution()
print(inst.containsNearbyDuplicate([1,2,3,1], 3))
print(inst.containsNearbyDuplicate([1,0,1,1], 1))