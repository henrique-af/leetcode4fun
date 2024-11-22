from functools import cmp_to_key
from typing import List


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        nums_list = list(map(str, nums))
        
        def compare(x: str, y: str) -> int:
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
            
        nums_list.sort(key=cmp_to_key(compare))
        largest_num = ''.join(nums_list)
        
        if largest_num[0] == '0':
            return "0"
        
        return largest_num
        
sol = Solution()