from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for num in nums:
            if (-num) in nums:
                return num
        return -1


nums = [-1, 2, -3, 3]
sol = Solution()
sol.findMaxK(nums)
