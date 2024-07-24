from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        if target in nums:
            value = nums.index(target)
            return value
        else:
            while nums[i] < target:
                if nums[i] < target and (i == n - 1 or nums[i + 1] >= target):
                    return i + 1
                i += 1
            return 0


target = 7
nums = [1, 3, 5, 6]
sol = Solution()
print(sol.searchInsert(nums, target))
