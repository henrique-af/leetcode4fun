from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sums = []
        mod = 10**9 + 7
        for i in range(n):
            current = 0
            for j in range(i, n):
                current = (current + nums[j]) % mod
                subarray_sums.append(current)
        subarray_sums.sort()
        res = 0
        for i in range(left - 1, right):
            res = (res + subarray_sums[i]) % mod
        return res


nums = [1, 2, 3, 4]
n = 4
left = 1
right = 5
sol = Solution()
sol.rangeSum(nums, n, left, right)
