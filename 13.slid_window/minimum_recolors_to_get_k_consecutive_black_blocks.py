"""
https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/

Алгоритм решения
1. Находим сумму W в первом окне.
2. Заводим временный счетчик.
3. Итерируемся по blocks и вычитаем из суммы 1 если вышедшее из кона значение равно W, а после прибавляем 1,
если новое значение в окне равно W


Сложность по памяти O(1)
Сложность по времени O(n)
"""

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        ans = 0
        for i in range(k):
            if blocks[i] == "W":
                ans += 1

        w_cnt = ans

        for i in range(1, len(blocks) - k + 1):

            if blocks[i-1] == "W":
                w_cnt -= 1

            if blocks[i+k-1] == "W":
                w_cnt += 1

            ans = min(w_cnt, ans)

        return ans

inst = Solution()
print(inst.minimumRecolors("WBBWWBBWBW", 7))
print(inst.minimumRecolors("WBWBBBW", 2))