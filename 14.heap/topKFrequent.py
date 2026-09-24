"""
Ссылка: https://leetcode.com/problems/top-k-frequent-words/


Алгоритм решения
1. Заводит словарь с подсчитанным кол-во слов
2. Превращаем его в кучу инвертируя значение count
3. Отбираем K наибольших элементов из кучу



Сложность по памяти O(n)
Сложность по времени O(n + k * log(n))
"""
import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)

        heap = [(-v, k) for k, v in cnt.items()]

        heapq.heapify(heap)

        ans = []

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans


inst = Solution()
print(inst.topKFrequent(["i","love","leetcode","i","love","coding"], 2))
print(inst.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))

print(3**2)