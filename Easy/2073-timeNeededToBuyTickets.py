from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total_time = 0

        for i, ticket_count in enumerate(tickets):
            if i <= k:
                total_time += min(ticket_count, tickets[k])
            else:
                total_time += min(ticket_count, tickets[k] - 1)

        return total_time

sol = Solution()
tickets = [84, 49, 5, 24, 70, 77, 87, 8]
k = 3
print(sol.timeRequiredToBuy(tickets, k))
