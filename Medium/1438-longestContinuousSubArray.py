from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 1
        minQ = deque()
        maxQ = deque()
        l = 0
        for r, num in enumerate(nums):
            while minQ and num > minQ[-1]:
                minQ.pop()
            minQ.append(num)
            while maxQ and num < maxQ[-1]:
                maxQ.pop()
            maxQ.append(num)
            while minQ[0] - maxQ[0] > limit:
                if minQ[0] == nums[l]:
                    minQ.popleft()
                if maxQ[0] == nums[l]:
                    maxQ.popleft()
                l += 1
            ans = max(ans, r - l + 1)
        return ans


nums = [10, 1, 2, 4, 7, 2]
limit = 5
sol = Solution()
print(sol.longestSubarray(nums, limit))
