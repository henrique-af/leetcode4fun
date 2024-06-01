from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_result = 0
        num1, num2 = 0, 0

        for num in nums:
            xor_result ^= num
        rightmost_set_bit = xor_result & -xor_result

        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]


nums = [1, 2, 1, 3, 2, 5]
sol = Solution()
print(sol.singleNumber(nums))
