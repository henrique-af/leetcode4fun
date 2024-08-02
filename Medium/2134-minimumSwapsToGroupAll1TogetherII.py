from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)

        if total_ones == 0 or total_ones == len(nums):
            return 0

        max_ones_in_window = 0
        current_ones_in_window = 0
        n = len(nums)

        for i in range(total_ones):
            if nums[i] == 1:
                current_ones_in_window += 1
        max_ones_in_window = current_ones_in_window

        for i in range(total_ones, n + total_ones):
            if nums[i % n] == 1:
                current_ones_in_window += 1
            if nums[(i - total_ones) % n] == 1:
                current_ones_in_window -= 1

            max_ones_in_window = max(max_ones_in_window, current_ones_in_window)

        min_swaps = total_ones - max_ones_in_window

        return min_swaps
