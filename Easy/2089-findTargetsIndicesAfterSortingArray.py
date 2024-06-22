from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums.sort()
        index = []
        for i in range(n):
            if nums[i] == target:
                index.append(i)
        return index

nums = [1, 2, 5, 2, 3]
target = 2
sol = Solution()
result = sol.targetIndices(nums, target)
print(result)