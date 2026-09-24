"""
Ссылка: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


Алгоритм решения
1. Заводим левый указатель, словарь. Правым указателем будет выступать цикл.
2. Начинаем итерироваться по последовательности. Если текущее значение итерации есть в словаре и значение больше или равно
левому указателю, увеличиваем значение левого указателя на индекс текущей итерации + 1.
3. Для текущего символа ставим индекс равный текущей итерации.
4. Находим максимум межу предыдущим ответом и разностью правого и левого указателя + 1.


Сложность по памяти O(n)
Сложность по времени O(n)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        l = 0
        dict_char = {}

        for r in range(len(s)):

            if s[r] in dict_char and dict_char[s[r]] >= l:
                l = dict_char[s[r]] + 1

            dict_char[s[r]] = r

            ans = max(ans, r-l+1)

        return ans



inst = Solution()
print(inst.lengthOfLongestSubstring("abcabcbb"))
print(inst.lengthOfLongestSubstring("bbbbb"))