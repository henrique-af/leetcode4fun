from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)

        mismatch_count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatch_count += 1

        return mismatch_count

heights = [1,1,4,2,1,3]
sol = Solution()
print(sol.heightChecker(heights))
