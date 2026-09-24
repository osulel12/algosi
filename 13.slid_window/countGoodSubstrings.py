"""
Ссылка: https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/


Алгоритм решения
1. Заводим цикл, в котором сразу обозначаем окно, то есть начинаем проверку с крайнего правого элемента окна.
2. Проверяем все элементы в окна равным 3.
3. Если все элементы разные увеличиваем счетчик



Сложность по памяти O(1)
Сложность по времени O(n)
"""

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(2, len(s)):
            if s[i] != s[i-1] and s[i] != s[i-2] and s[i-1] != s[i-2]:
                ans += 1

        return ans


inst = Solution()
print(inst.countGoodSubstrings("xyzzaz"))
print(inst.countGoodSubstrings("aababcabc"))
