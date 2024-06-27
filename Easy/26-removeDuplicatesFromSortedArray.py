from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        j = 1
        n = len(nums)

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1

        for k in range(j, n):
            nums[k] = "_"

        return j


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
sol = Solution()
print(sol.removeDuplicates(nums))
