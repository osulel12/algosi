"""
Ссылка: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/


Алгоритм решения
1. Учтем, что у нас всегда правильно выражение, то есть нет кейса, где ")((((". Используем вместо списка (стэка)
переменную счетчик, где при "(" мы увеличиваем счетчик, а при ")" уменьшаем его. Это даст нам константную память.
2. Сравниваем на каждом шаге максимум от нашего ответа и текущего счетчика.


Сложность по памяти O(1)
Сложность по времени O(n)
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        ans = 0

        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1

            ans = max(ans, cnt)

        return ans


inst = Solution()
print(inst.maxDepth("(1+(2*3)+((8)/4))+1"))
print(inst.maxDepth("(1)+((2))+(((3)))"))
