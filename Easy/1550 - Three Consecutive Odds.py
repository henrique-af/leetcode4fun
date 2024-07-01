from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n - 2):
            if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
                return True
        return False


arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
sol = Solution()
print(sol.threeConsecutiveOdds(arr))
