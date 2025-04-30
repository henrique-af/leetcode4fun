from typing import List



def minimumDifference(nums: List[int], k: int) -> int:
    if len(nums) <= 1:
        return 0
    
    nums.sort() 
    min_diff = float('inf')
    
    for i in range(len(nums) - k + 1):
        diff = nums[i + k - 1] - nums[i]
        min_diff = min(min_diff, diff)
    
    return min_diff

print(minimumDifference([9, 4, 1, 7], 2))