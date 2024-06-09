from typing import List



class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        resto_count = {0: 1}

        for num in nums:
            prefix_sum += num
            resto = prefix_sum % k
            if resto < 0:
                resto += k  

            if resto in resto_count:
                count += resto_count[resto]
                resto_count[resto] += 1
            else:
                resto_count[resto] = 1

        return count


nums = [4, 5, 0, -2, -3, 1]
k = 5
sol = Solution()
sol.subarraysDivByK(nums, k)
