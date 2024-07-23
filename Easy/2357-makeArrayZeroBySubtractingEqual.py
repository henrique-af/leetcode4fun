from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = [num for num in nums if num != 0]
        return len(set(nums))

nums = [0]
sol = Solution()
print(sol.minimumOperations(nums))
