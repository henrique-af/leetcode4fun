from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index: int, current_xor: int) -> int:
            if index == len(nums):
                return current_xor
            with_current = dfs(index + 1, current_xor ^ nums[index])
            without_current = dfs(index + 1, current_xor)
            return with_current + without_current
        
        return dfs(0, 0)


nums = [5, 1, 6]
sol = Solution()
sol.subsetXORSum(nums)
