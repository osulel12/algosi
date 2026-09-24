"""
Ссылка: https://leetcode.com/problems/minimum-string-length-after-removing-substrings/


Алгоритм решения
1. Инициализируем наш стэк.
2. В цикле проходимся по каждому из значений. Если стэк не пустой, а комбинация последнего символа в стэк и текущего
символа равна AB или CD, в таком случае удаляем последний символ из стэк и пропускаем текущий символ.
Если условие не выполнилось, значит добавляем символ в стэк.
3. Возвращаем длину текущего стэка.


Сложность по памяти O(n)
Сложность по времени O(n)
"""



class Solution:
    def minLength(self, s: str) -> int:

        stack = []

        for c in s:

            if stack and (stack[-1] + c == "AB" or stack[-1] + c == "CD"):
                print(stack[-1] + c)
                stack.pop()
            else:
                stack.append(c)

        return len(stack)


inst = Solution()
print(inst.minLength("ABFCACDB"))
print(inst.minLength("ACBBD"))
