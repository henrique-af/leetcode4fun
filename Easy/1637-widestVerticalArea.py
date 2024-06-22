from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coords = [p[0] for p in points]
        x_coords.sort()

        max_width = 0
        for i in range(1, len(x_coords)):
            max_width = max(max_width, x_coords[i] - x_coords[i - 1])

        return max_width

points = [[8,7],[9,9],[7,4],[9,7]]
sol = Solution()
result = sol.maxWidthOfVerticalArea(points)
print(result)
