"""
Ссылка: https://leetcode.com/problems/running-sum-of-1d-array/


Алгоритм решения
1. Идея в том, что создаем функцию хелпер, где базой рекурсии будет равенство текущего индекса и длинны массива, а
рекурсивный случай это увеличение накопленной суммы и возвращение [cur_sum] + вызов нашего хелпера, куда мы передаем
увеличенный на 1 индекс и текущую накопленную сумму.


Сложность по памяти O(n)
Сложность по времени O(n^2)
"""


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        def helper(i, cur_sum):
            if i == len(nums):
                return []

            cur_sum += nums[i]

            return [cur_sum] + helper(i + 1, cur_sum)

        return helper(0, 0)


inst = Solution()
print(inst.runningSum([1,2,3,4]))
print(inst.runningSum([1,1,1,1,1]))
