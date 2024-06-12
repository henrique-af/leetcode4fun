from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeros = 0
        ones = 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1

        for i in range(0, zeros):
            nums[i] = 0

        for i in range(zeros, zeros + ones):
            nums[i] = 1

        for i in range(zeros + ones, len(nums)):
            nums[i] = 2

nums = [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]
sol = Solution()
print(sol.sortColors(nums))