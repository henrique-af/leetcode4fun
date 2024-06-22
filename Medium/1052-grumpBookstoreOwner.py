from typing import List

from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        n = len(customers)
        total_satisfied = 0
        max_extra_satisfied = 0
        current_extra_satisfied = 0

        for i in range(n):
            if grumpy[i] == 0:
                total_satisfied += customers[i]

        for i in range(n):
            if grumpy[i] == 1:
                current_extra_satisfied += customers[i]
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    current_extra_satisfied -= customers[i - minutes]
            max_extra_satisfied = max(max_extra_satisfied, current_extra_satisfied)

        return total_satisfied + max_extra_satisfied


customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3
sol = Solution()
result = sol.maxSatisfied(customers, grumpy, minutes)
print(result) 
