"""
Ссылка: https://leetcode.com/problems/next-greater-element-i/


Алгоритм решения
1. Инициализируем наш стэк и словарь.
2. Итерируемся по второму массиву и если выполняется условие, что стэк не пустой и последний элемент стэка
меньше, чем текущий, то удаляем последний элемент из стэка и добавляем его в словарь. Где ключом будет наш последний
элемент стека на текущей итерации, а значением текущий элемент массива.
3. На каждой итерации добавляем элемент в стэк.
4. Возвращаем список, где берем значения из перового массива и находим их в нашем словаре, если таких значений нет в словаре,
возвращаем -1.



Сложность по памяти O(n)
Сложность по времени O(n)
"""


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        stack = []
        pair = {}

        for value in nums2:

            while stack and stack[-1] < value:
                pair[stack.pop()] = value
            stack.append(value)
        return [pair.get(i, -1) for i in nums1]



inst = Solution()
print(inst.nextGreaterElement([4,1,2], [1,3,4,5]))
print(inst.nextGreaterElement([2,4], [1,2,3,4]))
