from typing import List
from collections import Counter, defaultdict

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_counter = Counter(target)
        arr_counter = Counter(arr)

        return target_counter == arr_counter

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = defaultdict(int), defaultdict(int)
        for n1, n2 in zip(target, arr):
            count[n1] += 1
            count[n2] -= 1
        for n in count:
            if count[n] != 0:
                return False
        return True


target = [1,2,3,4]
arr = [2,4,1,3]
sol = Solution()
sol.canBeEqual(target, arr)
