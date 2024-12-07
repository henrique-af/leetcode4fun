from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        
        def can_achieve_penalty(penalty):
            operations = sum((num - 1) // penalty for num in nums)
            return operations <= maxOperations
        
        while left < right:
            mid = (left + right) // 2
            if can_achieve_penalty(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
    
sol = Solution()
print(sol.minimumSize([9], 2))