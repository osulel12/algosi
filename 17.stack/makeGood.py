"""
Ссылка: https://leetcode.com/problems/make-the-string-great/


Алгоритм решения
1. 
2. 
3. 



Сложность по памяти O(n)
Сложность по времени O(n)
"""


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for l in s:
            if stack and stack[-1].lower() == l.lower() and stack[-1].islower() != l.islower():
                stack.pop()
            else:
                stack.append(l)
        return ''.join(stack)


inst = Solution()
print(inst.makeGood("leEeetcode"))
print(inst.makeGood("abBAcC"))
