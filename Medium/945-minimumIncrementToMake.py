from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums or len(nums) <= 1:
            return 0

        nums.sort()
        numOfMoves = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                numOfMoves += increment

        return numOfMoves


nums = [1, 2, 2]
sol = Solution()
print(sol.minIncrementForUnique(nums))