from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for number, value in count.items():
            if value == 1 and value.next == 1:
                return False
            else:
                return number
            

sol = Solution()
sol.singleNumber([2, 2, 1])