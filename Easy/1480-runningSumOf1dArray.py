from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        sumNum = 0
        for num in nums:
            sumNum += num
            res.append(sumNum)

        return res

sol = Solution()
nums = [1, 2, 3, 4]
sol.runningSum(nums)