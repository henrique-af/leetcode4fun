from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_array = []
        for i in range(len(nums)):
            new_array.append(nums[i] ** 2)
        
        new_array.sort()
        return new_array


nums = [-4,-1,0,3,10]        
sol = Solution()
print(sol.sortedSquares(nums))