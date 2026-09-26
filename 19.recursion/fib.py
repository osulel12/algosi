"""
Ссылка: https://leetcode.com/problems/fibonacci-number/


Алгоритм решения
1. 
2. 
3. 



Сложность по памяти O(n)
Сложность по времени O(n^2)
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        return self.fib(n-1) + self.fib(n-2)


inst = Solution()
print(inst.fib(2))
print(inst.fib(3))
