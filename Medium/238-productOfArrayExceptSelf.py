from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [1] * n
        answer = [1] * n

        left_product = 1
        for i in range(n):
            left[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] = left[i] * right_product
            right_product *= nums[i]

        return answer


nums = [1, 2, 3, 4]
sol = Solution()
print(sol.productExceptSelf(nums))
