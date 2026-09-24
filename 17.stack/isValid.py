"""
Ссылка: https://leetcode.com/problems/valid-parentheses/


Алгоритм решения
1. Создаем стэк и словарь со скобками, где ключи это закрывающие скобки, а значения открывающие.
2. Итерируемся по последовательности скобок, если текущая скобка открывающая, не входит во множество brackets.keys,
добавляем ее в стэк.
3. Иначе проверяем, если стэк не пустой и последнее значение в стэке равно brackets[текущее_значение], т.е получили
корректную пару скобок, то удаляем последнее значение из стэка. Иначе возвращаем false, так как уже получили
не валидную пару скобок.
4. Возвращаем результат сравнение длины стэка с 0.


Сложность по памяти O(n)
Сложность по времени O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c not in brackets:
                stack.append(c)
            else:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


inst = Solution()
print(inst.isValid("()[]{}"))
print(inst.isValid("([])"))
