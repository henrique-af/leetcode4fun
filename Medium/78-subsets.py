from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index: int, current: List[int]) -> List[List[int]]:
            if index == len(nums):
                return [current]
            with_current = dfs(index + 1, current + [nums[index]])
            without_current = dfs(index + 1, current)
            return with_current + without_current

        return dfs(0, [])


nums = [1,2,3]
sol = Solution()
sol.subsets(nums)
