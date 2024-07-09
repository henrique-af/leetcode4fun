from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        available_at = 0
        total_wait = 0
        for arrival, t in customers:
            available_at = max(available_at, arrival) + t
            total_wait += available_at - arrival

        return total_wait / len(customers)

customers = [[1, 2], [2, 5], [4, 3]]
sol = Solution()
print(sol.averageWaitingTime(customers))
