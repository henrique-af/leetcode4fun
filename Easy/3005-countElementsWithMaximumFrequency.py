from typing import Counter, List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)

        sorted_items = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        total = 0

        max_freq = sorted_items[0][1]

        for _, freq in sorted_items:
            if freq == max_freq:
                total += freq
        return total

nums = [1, 2, 2, 3, 1, 4]
sol = Solution()
sol.maxFrequencyElements(nums)
