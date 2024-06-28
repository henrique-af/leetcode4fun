from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        answer = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if digits[k] % 2 == 0 and digits[i] != 0:
                        number = digits[i] * 100 + digits[j] * 10 + digits[k]
                        answer.add(number)
        return sorted(answer)


digits = [2,1,3,0]    
sol = Solution()
sol.findEvenNumbers(digits)
