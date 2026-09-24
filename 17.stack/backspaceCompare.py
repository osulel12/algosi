"""
Ссылка: https://leetcode.com/problems/backspace-string-compare/


Алгоритм решения
1. Создаем стэк под каждый из списков.
2. Проверяем, если символ "#", то проверяем не пустой ли стэк, если стэк не пустой убираем последний элемент.
Иначе добавляем элемент в стэк. Важно, в стэк нельзя добавлять символ #.
3. Возвращаем результат сравнения полученных строк.



Сложность по памяти O(max(m, n))
Сложность по времени O(n + m)
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def typing(s):

            stack = []

            for c in s:
                if c == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return ''.join(stack)

        return typing(s) == typing(t)


inst = Solution()
print(inst.backspaceCompare(s="ab##", t="c#d#"))
print(inst.backspaceCompare(s="a#c", t="b"))
