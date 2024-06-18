from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyerMoore
        candidate = nums[0]
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


nums = [3, 2, 3]
sol = Solution()
sol.majorityElement(nums)
