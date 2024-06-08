from typing import List


class Solution(object):
    def checkSubarraySum(self, nums, k):
        map = {0: -1} 
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            rem = sum % k

            if rem in map:
                if i - map[rem] > 1:
                    return True
            else:
                map[rem] = i

        return False


nums = [23,2,4,6,7]
k = 6       
sol = Solution()
print(sol.checkSubarraySum(nums, k))
