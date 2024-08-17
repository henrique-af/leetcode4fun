from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0][:]

        for i in range(1, m):
            left_max = [0] * n
            right_max = [0] * n

            left_max[0] = dp[0]
            for j in range(1, n):
                left_max[j] = max(left_max[j - 1] - 1, dp[j])
            right_max[-1] = dp[-1]
            for j in range(n - 2, -1, -1):
                right_max[j] = max(right_max[j + 1] - 1, dp[j])
            for j in range(n):
                dp[j] = points[i][j] + max(left_max[j], right_max[j])

        return max(dp)

  
points = [[1,2,3],[1,5,1],[3,1,1]]
sol = Solution()
print(sol.maxPoints(points))