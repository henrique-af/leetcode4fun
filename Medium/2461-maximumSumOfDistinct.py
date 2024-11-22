from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0
        
        window_sum = 0
        max_sum = 0
        window = {}
        
        for i in range(k):
            window_sum += nums[i]
            window[nums[i]] = window.get(nums[i], 0) + 1

        if len(window) == k:
            max_sum = window_sum

        for i in range(k, n):
            window_sum -= nums[i - k]
            window[nums[i - k]] -= 1
            if window[nums[i - k]] == 0:
                del window[nums[i - k]]
            
            window_sum += nums[i]
            window[nums[i]] = window.get(nums[i], 0) + 1
            
            if len(window) == k:
                max_sum = max(max_sum, window_sum)
        
        return max_sum
        
nums = [1,5,4,2,9,9,9]
k = 3
sol = Solution()
print(sol.maximumSubarraySum(nums, k)       )