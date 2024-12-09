from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        parityDiff = []
        n = len(nums)
        for i in range(n - 1):
            if nums[i] % 2 != nums[i + 1] % 2:
                parityDiff.append(1)
            else:
                parityDiff.append(0)
        
        # Create prefix sum array
        prefixSum = [0] * (n + 1)
        for i in range(1, n):
            prefixSum[i] = prefixSum[i-1] + parityDiff[i-1]
        
        # Process queries
        answer = []
        for from_idx, to_idx in queries:
            length = to_idx - from_idx + 1
            parity_changes = prefixSum[to_idx] - prefixSum[from_idx]
            answer.append(parity_changes == length - 1)
        
        return answer
        
sol = Solution()
sol.isArraySpecial([3,4,1,2,6], [[0,4]])