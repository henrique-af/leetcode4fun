from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(nums: List[int], k: int) -> int:
            count = 0
            left = 0
            current_odds = 0

            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    current_odds += 1

                while current_odds > k:
                    if nums[left] % 2 == 1:
                        current_odds -= 1
                    left += 1

                count += right - left + 1

            return count

        return atMost(nums, k) - atMost(nums, k - 1)


nums = [1, 1, 2, 1, 1]
k = 3
sol = Solution()
sol.numberOfSubarrays(nums, k)
