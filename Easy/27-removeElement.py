from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j


sol = Solution()
nums = [3,2,2,3]
val = 3
print(sol.removeElement(nums, val))
