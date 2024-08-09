from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        i = 0
        n = len(nums)
        
        while i < n:
            num = nums[i]
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
            i += 1
        
        return False

nums = [2, 1, 5, 0, 4, 6]
sol = Solution()
sol.increasingTriplet(nums)