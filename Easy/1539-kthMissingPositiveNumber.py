from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        i = 1
        while True:
            if i not in arr:
                count += 1
                if count == k:
                    return i
            i += 1


arr = [1, 2, 3, 4]
k = 2
sol = Solution()
print(sol.findKthPositive(arr, k))
