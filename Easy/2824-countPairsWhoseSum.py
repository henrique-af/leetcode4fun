from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    count += 1
        return count


nums = [-1, 1, 2, 3, 1]
target = 2
sol = Solution()
result = sol.countPairs(nums, target)
print(result)
