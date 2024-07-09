from copy import copy
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums[-1])
            nums.pop()


nums = [1,2,3,4,5,6,7]
k = 3    
sol = Solution()
sol.rotate(nums, k)

nums.insert(0, nums[-1])
nums.remove(nums[-1])