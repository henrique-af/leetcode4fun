from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        expected_sum = n * (n + 1) // 2
        expected_sum_squares = n * (n + 1) * (2 * n + 1) // 6

        actual_sum = sum(nums)
        actual_sum_squares = sum(x * x for x in nums)

        diff_sum = actual_sum - expected_sum
        diff_sum_squares = actual_sum_squares - expected_sum_squares

        sum_dup_missing = diff_sum_squares // diff_sum

        duplicate = (diff_sum + sum_dup_missing) // 2
        missing = sum_dup_missing - duplicate

        return [duplicate, missing]


nums = [1, 2, 2, 4]
sol = Solution()
print(sol.findErrorNums(nums))  # Output should be [2, 3]
