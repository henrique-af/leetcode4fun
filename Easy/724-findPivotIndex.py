from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        n = len(nums)
        i = 0
        sumLeft, sumRight = 0, 0
        for i in range(n):
            sumRight = total_sum - sumLeft - nums[i]
            if sumRight == sumLeft:
                return i
            sumLeft += nums[i]
        return -1
        

sol = Solution()
nums = [1,7,3,6,5,6]
sol.pivotIndex(nums)