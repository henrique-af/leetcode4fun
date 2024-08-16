from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count_pairs_with_distance_leq(distance: int) -> int:
            count = 0
            left = 0

            for right in range(len(nums)):
                while nums[right] - nums[left] > distance:
                    left += 1
                count += right - left

            return count

        nums.sort()

        # Binary search
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            if count_pairs_with_distance_leq(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left

nums = [1,3,1]
k = 1
sol = Solution()
print(sol.smallestDistancePair(nums, k))