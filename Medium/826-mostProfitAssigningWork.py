from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(profit)
        jobs = [(difficulty[i], profit[i]) for i in range(n)]
        jobs.sort()
        worker.sort()

        profit_sum = 0
        current_profit = 0
        j = 0

        for i in worker:
            while j < n and jobs[j][0] <= i:
                current_profit = max(current_profit, jobs[j][1])
                j += 1
            
            profit_sum += current_profit
        
        return profit_sum
            

difficulty = [2,4,6,8,10] 
profit = [10,20,30,40,50]
worker = [4,5,6,7]
sol = Solution()
sol.maxProfitAssignment(difficulty, profit, worker)