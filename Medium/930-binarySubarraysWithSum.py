from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(nums, S):
            if S < 0:
                return 0
            left = 0
            sum_ = 0
            count = 0
            for right in range(len(nums)):
                sum_ += nums[right]
                while sum_ > S:
                    sum_ -= nums[left]
                    left += 1
                count += right - left + 1
            return count

        return atMost(nums, goal) - atMost(nums, goal - 1)


nums = [1,0,1,0,1]
goal = 2
sol = Solution()
sol.numSubarraysWithSum(nums, goal)
