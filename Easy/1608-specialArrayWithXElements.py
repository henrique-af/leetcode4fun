from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        for i in range(n):
            x = n - i
            if (i == 0 or nums[i - 1] < x) and nums[i] >= x:
                return x

        return -1


nums = [3, 5]
sol = Solution()
sol.specialArray(nums)
