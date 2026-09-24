"""
Ссылка: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/


Алгоритм решения
1. Создаем пустой список (стэк)
2. Если стэк не пустой и последний элемент равен текущему удаляем последний элемент из стэка и пропускаем текущий.
3. Если стэк пустой и последний элемент стека не равен текущему элементу добавляем элемент в стэк
4. Возвращаем строку из элементов, который остались в стэке


Сложность по памяти O(n)
Сложность по времени O(n)
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for l in s:

            if stack and stack[-1] == l:
                stack.pop()
            else:
                stack.append(l)
        return ''.join(stack)


inst = Solution()
print(inst.removeDuplicates("abbaca"))
print(inst.removeDuplicates("azxxzy"))
