from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        n = len(nums)

        for i in range(n):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + nums[i])

        return True

nums = [2,3,1,1,4]
sol = Solution()
sol.canJump(nums)
