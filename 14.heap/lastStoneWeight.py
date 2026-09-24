"""
Ссылка: https://leetcode.com/problems/last-stone-weight/description/


Алгоритм решения
1. Так как в python куча выдает минимумы, для начала мы меняем знак элемента на противоположный.
2. Преобразуем наш инвертированный список в кучу и в цикле while находим два самых больших элемента.
3. Если элементы не равны, то находим их разность и добавляем в кучу.
4. В конце возвращаем 0, если элементов не осталось или инвертированный первый элемента получившегося массива.



Сложность по памяти O(1)
Сложность по времени O(n * log(n))
"""
import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, -(y-x))

        return -stones[0] if len(stones) > 0 else 0


inst = Solution()
print(inst.lastStoneWeight([2,7,4,1,8,1]))
print(inst.lastStoneWeight([1]))
