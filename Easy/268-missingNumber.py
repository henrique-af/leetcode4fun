from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        for i in range(n + 1):
            if i in nums:
                nums.remove(i)
                i += 1
            else:
                return int(i)

nums = [9,6,4,2,3,5,7,0,1]
sol = Solution()
print(sol.missingNumber(nums))
