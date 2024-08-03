from typing import List
from collections import Counter

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_counter = Counter(target)
        arr_counter = Counter(arr)

        return target_counter == arr_counter

target = [1,2,3,4]
arr = [2,4,1,3]
sol = Solution()
sol.canBeEqual(target, arr)
