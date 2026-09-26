"""
Ссылка: https://leetcode.com/problems/power-of-three/


Алгоритм решения
1. Находим сначала базу рекурсии. Для нас это либо число равно 1, либо число меньше 1.
2. Рекурсивный случай это где число всегда больше 1. В таком случае еще раз вызываем нашу функцию, куда на вход передаем
число деленное на 3.


Сложность по памяти O(1)
Сложность по времени O(log(n))
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        if n == 1:
            return True

        return self.isPowerOfThree(n/3)




inst = Solution()
print(inst.isPowerOfThree(27))
print(inst.isPowerOfThree(-1))
