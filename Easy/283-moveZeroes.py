from typing import List
from collections import Counter


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(0)
        print(nums)


nums = [0, 1, 0, 3, 12]
sol = Solution()
sol.moveZeroes(nums)
