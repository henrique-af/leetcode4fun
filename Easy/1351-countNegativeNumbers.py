from typing import List


class Solution:
    def countNegatives(self, grids: List[List[int]]) -> int:
        count = 0 
        i = 0
        for grid in grids:
            for i in range(len(grid)):
                if grid[i] < 0:
                    count += 1
        return count

grids = [[5, 1, 0], [-5, -5, -5]]
sol = Solution()
result = sol.countNegatives(grids)
print(result)
