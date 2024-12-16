from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k > 0:
            min_value = min(nums)
            min_index = nums.index(min_value)
            
            nums[min_index] = min_value * multiplier
            
            k -= 1
        
        return nums
            
        
Solution.getFinalState([2, 1, 3, 5, 6], 5, 2)